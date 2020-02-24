# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Olivia Miranda
# Created: 2020-02-24
def nameforuser():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    uname = first + "." + last
    return uname
def passwrd():
    characters = True
    passwd = input("Create a new password: ")
    characters = False
    if len(passwd) >= 8:
        characters = True
    while characters == False:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
        if len(passwd) >= 8:
            characters = True
    return passwd

def main():
 uname = nameforuser()
 password = passwrd()
 print("The force is strong in this one…")
 print("Account configured. Your new email address is",uname + "1@marist.edu")
main()