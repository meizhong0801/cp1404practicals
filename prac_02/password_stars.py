"""
Now let's modify this program.

Move all the code inside a main() function and call main() at the bottom. Run it to make sure it works.
Note: if you don't have a main function, the refactoring below will use global variables.
So, it's an important first step to use main before adding other functions.

"""

MINIMUM_LENGTH = 8


def main():
    password = input("Enter your password: ")
    password = get_password(password)
    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password(password):
    while len(password) < MINIMUM_LENGTH:
        print("The password length is too short")
        password = input("Enter your password: ")
    return password


main()


# Test
# Enter your password: 3
# The password length is too short
# Enter your password: 44446677
# ********
# Enter your password: 0
# The password length is too short
# Enter your password: 123456789000
# ************
