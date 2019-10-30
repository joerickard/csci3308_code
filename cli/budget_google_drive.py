from sys import argv
from sys import exit
import os
import requests

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
	if (t == 'newUser' or t == 'login' or t == 'deleteUser'):
		r = requests.post(destination + t, json=request)
		print(request)
		print([x for x in r])

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
			send_req('newUser',json_newUser)

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


	# # # # # # # # Delete User Command # # # # # # # #
	if 'delete' in argv:
		# json_Delete = '{"Auth":'+Auth+', "UID":'+status.raw+'}'
		json_delete = {"username": user, "password": password}
		send_req('deleteUser', json_delete)

	# # # # # # # # LogOut User Command # # # # # # # #
	#local log-out by removing credentials from environment
	if '-logout' in argv:
		try:
			os.remove('auth.txt')
			print('You are now logged out')
		except:
			print('You are already logged out')