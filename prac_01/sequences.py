"""
A simple menu-driven program that has the following choices
(where x and y are inputs the user enters once at the start of the program):
Show the even numbers from x to y
Show the odd numbers from x to y
Show the squares from x to y
Exit the program
"""


menu = """(1)Show the even numbers from x to y
(2)Show the odd numbers from x to y
(3)Show the squares from x to y
(4)Exit the program"""

x = int(input("start: "))
y = int(input("end: "))
print(menu)
choice = input(">>> ")
while choice != "4":
    if choice =="1":
        print(f"Even numbers from {x} to {y}: ")
        for i in range(x, y+1):
            if i % 2 == 0:
                print(i)
    elif choice == "2":
        print(f"Odd numbers from {x} to {y}: ")
        for i in range(x, y+1):
            if i % 2 == 1:
                print(i)
    elif choice =="3":
        print(f"Squares from {x} to {y}: ")
        for i in range(x, y+1):
            print(i**2)
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ")
print("Finished.")


# test
# start: 2
# end: 20
# (1)Show the even numbers from x to y
# (2)Show the odd numbers from x to y
# (3)Show the squares from x to y
# (4)Exit the program
# >>> 1
# Even numbers from 2 to 20:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
# (1)Show the even numbers from x to y
# (2)Show the odd numbers from x to y
# (3)Show the squares from x to y
# (4)Exit the program
# >>> 2
# Odd numbers from 2 to 20:
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
# (1)Show the even numbers from x to y
# (2)Show the odd numbers from x to y
# (3)Show the squares from x to y
# (4)Exit the program
# >>> 3
# Squares from 2 to 20:
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# 121
# 144
# 169
# 196
# 225
# 256
# 289
# 324
# 361
# 400
# (1)Show the even numbers from x to y
# (2)Show the odd numbers from x to y
# (3)Show the squares from x to y
# (4)Exit the program
# >>> 4
# Finished.