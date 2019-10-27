from sys import argv


# Dictionary of commands that the CLI can perform
command_desc = {
	"-u" : "This signifies that the username follows.",
	"-p" : "The password should follow the -p command.",
	"-extract" : "Following extract there should be a list of at least 1 file to be retrieved from the cloud on the form '-extract file1 file2 ...'.",
	"-push" : "This should have a list of at least 1 file to be put into the cloud. The format is as follows '-push file1 file2 file3'",
	"-share" : "This should be followed a list of files and then the name of the user that the files should be shared with. Format should follow '-share file1 file2 ... username",
	"-unshare" : "This should be followed a list of files and then the name of the user that the files should be unshared with. Format should follow '-share file1 file2 ... username",
	"-h" : "Opens the help menu. If help is desired for a particular command -h should be followed with the command signature i.e. '-h -push'",
	"-login" : "Should be followed by a username '-u' tag and a password 'p' tag each with corresponding login credentials."
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

# After this line is the main execution of the program. All functions above are auxillary to these tasks.

print('\n')
if len(argv) == 1:
	print_help()
else:
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
