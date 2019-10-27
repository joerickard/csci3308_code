from sys import argv


# Dictionary of commands that the CLI can perform
command_desc = {
	"-u" : "This signifies that the username follows.",
	"-p" : "The password should follow the -p command.",
	"-extract" : "Following extract there should be a list of at least 1 file to be retrieved from the cloud on the form '-extract file1 file2 ...'.",
	"-push" : "This should have a list of at least 1 file to be put into the cloud. The format is as follows '-push file1 file2 file3'",
	"-share" : "This should be followed a list of files and then the name of the user that the files should be shared with. Format should follow '-share file1 file2 ... username",
	"-unshare" : "This should be followed a list of files and then the name of the user that the files should be unshared with. Format should follow '-share file1 file2 ... username",
	"-h" : "Opens the help menu. If help is desired for a particular command -h should be followed with the command signature i.e. '-h -push'"
}

# This array will tell me whether commands exist in the args and what index they exist at
flags = [-1]*len(command_desc)

# This function will define whether flags are present in the arguments passed.
# Flag is the particular command that is being looked at. flag_num is where it
# appears in the argv array.
def flag_set(flag, flag_num):
	if (flag in argv):
		flags[flag_num] = argv.index(flag)

# Helps locate the index of a flag in the dictionary.
def flag_index(flag):
	counter = 0
	for command in command_desc:
		if command == flag:
			return counter
		else:
			counter+=1

	return -1

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


if len(argv) == 1:
	print_help()
else:
	# Define the flags array
	counter = 0
	for flag in command_desc:
		flag_set(flag, counter)
		counter+=1

	help_command = len(argv)
	try:
		help_command = argv.index("-h")
	except:
		help_command = -1

	if help_command != -1:
		if (len(argv) == help_command + 1) or (argv[help_command + 1] not in command_desc):
			print_help()
		else:
			print_help_for(argv[help_command + 1])
