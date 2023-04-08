# Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
# The program should then output information about these numbers, as in the output below.
# Note that you can use the functions min, max, sum and len, and you can use the append method to add number to a list.
#
#    Number: 5
#    Number: 20
#    Number: 1
#    Number: 2
#    Number: 3
#    The first number is 5
#    The last number is 3
#    The smallest number is 1
#    The largest number is 20
#    The average of the numbers is 6.2

def main():
    numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    for i in range(5):
        number = int(input("Numbers: "))
        numbers.append(number)

    print("The first number is", numbers[0])
    print("The last number is ", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the number is", sum(numbers) / len(numbers))

    username = input("Please enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()


# test
# Numbers: 5
# Numbers: 20
# Numbers: 1
# Numbers: 2
# Numbers: 3
# The first number is 5
# The last number is  3
# The smallest number is 1
# The largest number is 20
# The average of the number is 6.2
# Please enter your username: jimbo
# Access granted

# Please enter your username: mia
# Access denied
