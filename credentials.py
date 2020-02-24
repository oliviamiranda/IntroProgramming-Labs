# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Olivia Miranda
# Created: 2020-02-24
def main():
# Get the user's first and last names
 first = input("Enter your first name: ")
 last = input("Enter your last name: ")
# TODO modify this to generate a Marist-style username
 uname = first + "." + last
# ask user to create a new password
 passwd = input("Create a new password: ")
# TODO modify this to ensure the password has at least 8 characters
 characters = False
 if len(passwd) >= 8:
  characters = True
 while characters == False:
  print("Fool of a Took! That password is feeble! Try to make it longer.")
  passwd = input("Create a new password: ")
  if len(passwd) >= 8:
      characters = True
 print("The force is strong in this one…")
 print("Account configured. Your new email address is",
 uname + "1@marist.edu")
main()