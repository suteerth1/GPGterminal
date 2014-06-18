
#Author: Suteerth Vishnu
#Python: version 2.7.4
#Distribution of operating system: Linux Ubuntu 13.04 (Raring Ringtail)


from sys import argv
import os

print("Do you wish to view all the keys you possess: (y/n)")
inK = raw_input().lower()
if inK == "y":
	print("Press q to Quit")
	os.system("gpg --list-keys|less")


print("Do you wish to encrypt\decrypt [Enter e or d]:")
input = raw_input().lower()
if input == "e":
	#encrypt code
	#this is to check for signing
	
	temp = ""
	signing = raw_input("Do you want to sign the message? (y/n)").lower()
	if signing == "y":
		temp = "-s"
	#this is for entering the email adress
	email = (raw_input("Enter email address:"))
	
	#for choosing a location for the output file
	
        sel = raw_input("Do you wish to save the file somwhere else? (y/n)").lower
        if sel == "y":
                output = raw_input("Enter the file PATH in the form [ ../path/name ]"
        else:
       	#use Desktop as default save location
            	output = raw_input("Enter output file NAME:")
            	output = "~/Desktop/" + output
	#the location of the input file
	message = raw_input("Enter the message file PATH:")
	 
	#the actual gpg command
	os.system("gpg --armour --encrypt %s --output ~/%s --recipient %s %s" % (temp, output, email, message))
 

elif input == "d":	
	pass
	#decrypt code
	#path to the encrypted message
	mPath = raw_input("Enter the Message PATH:")
	#decrypting..
	os.system("gpg --decrypt %s" %(mPath));
