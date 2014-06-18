#Author: Vedant Nevatia
#Date: 18th June 2014, 3:02PM


#To run, simply open up Terminal and cd to the directory containing
#this file and run 'python mac.py' without the quotes

import os

print("Would you like to encrypt a file or quit? (e or q): ")
choice = raw_input().lower()

if choice == 'e':

	print("Please enter the *full* location of the file: HINT: copy <Where> from Get Info: ")
	path = raw_input()

	print("Please provide file name with appropriate casing and extension:")
	file_name = raw_input()

	#merge path to file and the file name

	full_path = path + "/" + file_name
	
	#perform zip encryption

	os.system("zip -e ~/Desktop/encrypted_file.zip %s" % (full_path))

	print("Encryption complete.")
	os.system("exit")

elif choice == 'q':

	print("Goodbye.")
	os.system("exit")

else:
	print "Invalid command. Quitting..."
	os.system("exit")
