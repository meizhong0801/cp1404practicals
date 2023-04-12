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
    emails_to_name = {}

    email =input("Email: ")
    while email:
        name = get_name_from_email(email)
        correct_name = input(f"Is your name {name}? (Y/n)").lower()
        if correct_name == "n" or correct_name == "no":
            name = input("Name: ")

        emails_to_name = name
        email = input("Email: ")

    for email, name in emails_to_name.items():
        print(f"{name}({email})")


def get_name_from_email(email):
    parts = email.split("@")[0].split(".")
    name = "".join(parts).title()
    return name


main()

