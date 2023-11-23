"""
Move all the code inside a main() function and call main() at the bottom. Run it to make sure it works.
Refactor the part that gets the password into a separate function

"""


MINIMUM_LENGTH = 8


def main():
    password = input("Enter your password: ")
    password = get_password(password)
    print_password(password)

# prints the password with asterisks (*) to hide it.
def print_password(password):
    print("*" * len(password))


# checks if the provided password meets the minimum length requirement
def get_password(password):
    while len(password) < MINIMUM_LENGTH:
        print("The password length is too short")
        password = input("Enter your password: ")
    return password


main()


"""
Testing


Enter your password: 2333
The password length is too short
Enter your password: hhhh11
The password length is too short
Enter your password: 119992h5h
*********


"""