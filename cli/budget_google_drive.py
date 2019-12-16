from sys import argv
from sys import exit
import os
import requests
import json

# This is the URL where info will be passed.
destination = 'http://127.0.0.1:5000/api/'

# Dictionary of commands that the CLI can perform
command_desc = {
	"-u" : "This signifies that the username follows.",
	"-p" : "The password should follow the -p command.",
	"-extract" : "Following extract there should be a list of at least 1 file to be retrieved from the cloud on the form '-extract file1 file2 ...'.",
	"-push" : "This should have a list of at least 1 file to be put into the cloud. The format is as follows '-push file1 file2 file3'",
	"-share" : "This should be followed a list of files and then the name of the user that the files should be shared with. Format should follow '-share file1 file2 ... username",
	"-unshare" : "This should be followed a list of files and then the name of the user that the files should be unshared with. Format should follow '-share file1 file2 ... username",
	"-h" : "Opens the help menu. If help is desired for a particular command -h should be followed with the command signature i.e. '-h -push'",
	"-login" : "Should be followed by a username '-u' tag and a password 'p' tag each with corresponding login credentials. If both -u and -p are present the -login command will be signaled implicitly.",
	"-logout" : "Removes stored credentials",
	"-create" : "Indicates a new account should be made with given password and username./",
	"-delete" : "Used with a logged in account. Deletes the account."
}


# This uses the dictionary at the top and will print out all commands and descriptions.
def print_help():
	print('%-15s' % 'Commands:', end="")
	print('Usage:\n')
	for command in command_desc:
		print('%-15s' % command, end="")
		print(command_desc[command] + "\n")

# This is used to print help for just one command.
def print_help_for(command):
	print('%-15s' % command, end="")
	print(command_desc[command] + "\n")

def send_req(t, request):
	
	r = requests.post(destination + t, json=request)

	return r

def send_file(t, request, filename):
	if (t == 'upload'):
		files = [
			('file', (os.path.basename(filename), open(filename, 'rb'), 'application/octet')),
			('json', ('json', json.dumps(request), 'application/json')),
		]
		r = requests.post(destination + t, files=files)

	return r

# After this line is the main execution of the program. All functions above are auxillary to these tasks.

print('\n')
if len(argv) == 1:
	print_help()
else:

	# # # # # # # # Help Command # # # # # # # #

	# Identifies whether (and where if applicable) the help command appears.
	help_command = len(argv)
	try:
		help_command = argv.index("-h")
	except:
		help_command = -1

	# Will execute the desired print statement for help if one is required.
	if help_command != -1:
		# Help menu that prints everything. Only happens when -h is not followed by another valid command.
		if (len(argv) == help_command + 1) or (argv[help_command + 1] not in command_desc):
			print_help()
		else: #Case where only one command is printed out. Occurs when -h is followed by valid command.
			print_help_for(argv[help_command + 1])

		print('\n')


	# # # # # # # # Login User Command # # # # # # # #

	# This first try clause will see if a username and password are provided. If they are update the credentials file and store these for later use.
	try:
		user = argv[argv.index("-u") + 1]
		password = argv[argv.index("-p") + 1]

		credentials = open('auth.txt', 'w')

		credentials.write(user + '\n')
		credentials.write(password)
		if '-create' in argv:
			# json_NewUser = '{"Auth":' + Auth + '}'
			json_newUser = {"username": user, "password": password}
			status = send_req('newUser',json_newUser)
			if (json.loads(status.text)['created']):
				print('Account creaetd successfully! Username: %s\t Password: %s' % (user, password))
			else:
				print('There is already a user with that name!')
	except:
	# In the event that no user and password is provided it will check for previously stored credentials here.
		try:
			credentials = open('auth.txt', 'r')
			user = credentials.readline().replace('\n', '')
			password = credentials.readline()
		except:
			# Throw error message if no user or pass is provided.
			print('You need to provide both the username and password in order to manipulate files')
			exit(1)

	# This is where the auth will be provided to the database.
	# json_login = '{"Auth":'+Auth + '}'
	json_login = {"username": user, "password": password}
	status = send_req('login', json_login)

	if (json.loads(status.text)['loggedin']):
		print('Successfully logged in!')
	else:
		print('Not logged in! You must log in to use this service!')
		exit(1)
	# # # # # # # # Delete User Command # # # # # # # #
	if '-delete' in argv:
		# json_Delete = '{"Auth":'+Auth+', "UID":'+status.raw+'}'
		json_delete = {"username": user, "password": password}
		status = send_req('deleteUser', json_delete)
		if (json.loads(status.text)['deleted']):
			print('The account %s has been successfully deleted.' % (user))
		else:
			print('Error. Account not delted')

	# # # # # # # # Logout User Command # # # # # # # #
	#local log-out by removing credentials from environment
	if '-logout' in argv:
		try:
			os.remove('auth.txt')
			print('You are now logged out')
		except:
			print('You are already logged out')

	# # # # # # # # Push Command # # # # # # # #
	if '-push' in argv:
		index = argv.index('-push') + 1
		while (index < len(argv) and argv[index] not in command_desc):
			if (os.path.exists(argv[index])):
				json_push = {"username": user, "password": password, "file": argv[index]}
				resp = send_file('upload', json_push, argv[index])
				print(resp)
			else:
				print('%s is not a valid file' % argv[index])

			index += 1

	# # # # # # # # Extract Command # # # # # # # #
	if '-extract' in argv:
		index = argv.index('-extract') + 1
		while (index < len(argv) and argv[index] not in command_desc):
			json_extract = {"username": user, "password": password, "file": argv[index]}
			status = send_req('download', json_extract)

			try:
				json.loads(status.text)
				print('File doesn\'t exist')
			except:
				print('Successfully obtained file %s' % argv[index])
				# print(status.content)
				with open(argv[index], 'wb') as f:
					f.write(status.content)

			index += 1

	# # # # # # # # Share Command # # # # # # # #
	if '-share' in argv:
		index = user_index = argv.index('-share') + 1
		while (user_index < len(argv) and argv[user_index] not in command_desc):
			user_index += 1

		user_index -= 1

		while index < user_index:
			json_share = {"username": user, "password": password, "file": os.path.basename(argv[index]), "recipient": argv[user_index]}
			status = send_req('share', json_share)
			resp = json.loads(status.text)['status']
			if (resp):
				print('file %s was successfully shared with %s' % (os.path.basename(argv[index]), argv[user_index]))
			else:
				print('failed to share file %s' % os.path.basename(argv[index]))
			index += 1

	# # # # # # # # Share Command # # # # # # # #
	if '-unshare' in argv:
		index = user_index = argv.index('-unshare') + 1
		while (user_index < len(argv) and argv[user_index] not in command_desc):
			user_index += 1

		user_index -= 1

		while index < user_index:
			json_unshare = {"username": user, "password": password, "file": argv[index], "recipient": argv[user_index]}
			status = send_req('unshare', json_unshare)
			resp = json.loads(status.text)['status']
			if (resp):
				print('permissions to file %s was successfully revoked from %s' % (os.path.basename(argv[index]), argv[user_index]))
			else:
				print('failed to revoke permissions of file %s' % os.path.basename(argv[index]))

			index += 1









