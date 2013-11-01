from sys import argv
import os

print("Do you wish to view all the keys you posses(y/n)")
inK=(raw_input().lower())
if inK == "y":
	print("Press q to Quit")
	os.system("gpg --list-keys|less")


print("Do you wish to encrypt\decrypt [enter E or D]:")
input=(raw_input().lower())
if input=="e":
	#encrypt code
	
	#this is to check for signing
	temp=""
	signing=(raw_input("Do you want to sign the message(y/n)").lower())
	if signing=="y":
		temp="-s"
	email=(raw_input("Enter email address:"))
	output=(raw_input("Enter output file NAME:"))
	message=(raw_input("Enter the message file PATH:"))
	os.system("gpg --armour --encrypt %s --output ~/%s --recipient %s %s" % (temp,output,email,message))


elif input == "d":	
	pass
	#decrypt code
	mPath=(raw_input("Enter the Message PATH:"))
	os.system("gpg --decrypt %s" %( mPath));
