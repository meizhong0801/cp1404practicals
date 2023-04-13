"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
Use a separate function to extract a name from the email as in the example below.
You should find the following methods useful: split, join, title.

Notice the prompt to check if the name is correct: Y/n
This is used in console programs (like in Linux etc.) so you can just press Enter to accept the default of (Y)es.
Example from Linux:

> sudo apt-get upgrade
...
After this operation, 267 kB of additional disk space will be used.
Do you want to continue? [Y/n] blah
Abort.
"""


def main():
    emails_and_names = {}

    email = input("Email: ")
    while email != "":
        name_in_email = " ".join(email.split("@")[0].split("."))
        is_correct = input(f"Is your name {name_in_email}? (Y/n)").lower()
        if is_correct == "n" or is_correct == "no":
            name = input("Name: ")
        else:
            name = name_in_email
        emails_and_names[name] = email
        email = input("Email: ")

    print()
    for key in emails_and_names:
        print(f"{key.title()} ({emails_and_names[key]})")


main()

# test

# Email: lindsay.ward@jcu.edu.au
# Is your name lindsay ward? (Y/n)y
# Email: abe@gmail.com
# Is your name abe? (Y/n)y
# Email: jimbo546@hotmail.com
# Is your name jimbo546? (Y/n)no
# Name: Jim Boh
# Email:
#
# Lindsay Ward (lindsay.ward@jcu.edu.au)
# Abe (abe@gmail.com)
# Jim Boh (jimbo546@hotmail.com)
