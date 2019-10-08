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

# This function will define whether flags are present in the arguments passed
def flag_exists(flag, flag_num):
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

def print_help():
	print('%-15s' % 'Commands:', end="")
	print('Usage:\n')
	for command in command_desc:
		print('%-15s' % command, end="")
		print(command_desc[command] + "\n")

if len(argv) == 1:
	print_help()
else:
	# Define the flags array
	counter = 0
	for flag in command_desc:
		flag_exists(flag, counter)
		counter+=1

	help_command = flag_index("-h")
	if flags[help_command] != -1:
		if ((len(argv) != flags[help_command] + 1) and not (argv[flags[help_command] + 1] in command_desc)):
			print_help()
		else:
			print('%-15s' % argv[flags[help_command] + 1], end="")
			print(command_desc[argv[flags[help_command] + 1]])
