"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.

"""


def main():
    emails_and_names = {}

    email = input("Email: ")

    # Continue the loop until the user enters a blank email.
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

    # Loop through the dictionary and print the name and email pairs.
    for key in emails_and_names:
        print(f"{key.title()} ({emails_and_names[key]})")


main()

