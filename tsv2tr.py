#!/usr/bin/env python
# coding: utf-8

# Takes an input file and convert all tabs to HTML <tr>
# format to include inside an HTML table.
# Output is written to a file name derived from input file.

import sys
import getopt
import os.path

# Set version
__version__ = '1.0.0'

# Given a file_name, find the output file name
# a.tsv -> a.tr
# a.foo -> a.tr
# a.tr -> a.tr.tr
# a -> a.tr
def find_output_file_name(file_name):
	path, file_ext = os.path.splitext(file_name)
	# Error check just in case.
	if path == "":
		print "Missing file name"
		sys.exit(1)
	s = path + ".tr"
	return s

# Replace string 's' using the ignore list
def replace_line(line, ignore_list):
	# Get list of columns to ignore
	ignore_columns = ignore_list.split(",")
	# Convert from list to dictionary, enumerate
	ignored_dictionary = dict(enumerate(ignore_columns))
	# Convert to integers
	for key in ignored_dictionary:
		ignored_dictionary[key] = int(ignored_dictionary[key])
	# Split line by tabs
	split_line = line.split("\t")
	s = "<tr>"
	count = 0
	for element in split_line:
		count = count + 1
		ignore_column = False
		for key in ignored_dictionary:
			if ignored_dictionary[key] == count:
				ignore_column = True
		if ignore_column:
			s = s + element
		else:
			s = s + "<td>" + element + "</td>"
	s = s + "</tr>" + "\n"
	return s


# Given a file name, work out output file name
# Read every line from file_name, convert, output.
def process_arg(file_name, ignore_list):
	output_file_name = find_output_file_name(file_name)
	# Error check
	if not os.path.isfile(file_name):
		print "File %s does not exist" % file_name
		sys.exit(1)
	# Convert ignore list to 
	with open(file_name, "r") as f_in:
		with open(output_file_name, "w") as f_out:
			for line in f_in:
				stripped_line = line.rstrip("\r\n")
				# If there is an ignore list, use it, else do quick
				if (ignore_list == ""):
					s = "<tr><td>" + stripped_line.replace("\t", "</td><td>") + "</td></tr>" + "\n"
				else:
					s = replace_line(stripped_line, ignore_list)
				# Replace start of line with <tr>
				f_out.write(s)

# Print help
def print_help():
	help = """
Usage: tsv2tr [-i col1[, col2]] file1 [file2 ...]
		 tsv2tr -h | --help
		 tsv2tr --version

Options:
	-h --help	 show this screen.
	-i --ignore	 ignore column numbers, first column is 1.
	--version	 show version.

Output written to an extension of file1. Examples:
a.tsv -> a.tr
a.tsv -> a.tr
a.foo -> a.tr
a.tr -> a.tr.tr
a -> a.tr

Ignore column useful if the column already has a <td></td> tag.
Example: sorting cards using AS, KS, QS, JS, ... 2C
The columns would be pre-sorted using
<td sort-order="1">&spades;A</td>

"""[1:-1]
	print(help)

def usage():
	print_help()
	return 0

def version():
	print('tsv2tr {}'.format(__version__))

def main():
	# Parse arguments
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hi:v", ["help", "ignore", "version"])
	except getopt.GetoptError as err:
		# print help information and exit:
		print str(err)	# will print something like "option -a not recognized"
		usage()
		sys.exit(2)
	output = None
	verbose = False
	ignore_list = ""
	for o, a in opts:
		if o == "-v":
			verbose = True
		elif o in ("-i", "--ignore"):
			ignore_list = a
			# Remove all blank space from ignore list
			ignore_list.replace(" ", "")
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("--version"):
			version()
			sys.exit()
		else:
			assert False, "unhandled option"

	# If missing argument
	if len(sys.argv) == 1:
		print "Missing argument"
		usage()
		sys.exit()

	# Process each argument
	for argv in args:
		process_arg(argv, ignore_list)	

	# Happy exit
	sys.exit()

if __name__ == "__main__":
	main()
