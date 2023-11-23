"""
Use this pattern to create a very simple menu-driven program according to the pseudocode below:
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

"""


# Display the menu options
def display_menu():
    menu = ["(H)ello", "(G)oodbye", "(Q)uit"]
    for item in menu:
        print(item)


def main():
    # Get the user's name
    name = input("Enter name: ")

    while True:
        display_menu()
        your_choice = input(">>> ").upper()
        # Display the corresponding message with the user's name
        if your_choice == "Q":
            break
        elif your_choice == "H":
            print("Hello", name)
        elif your_choice == "G":
            print("Goodbye", name)
        else:
            print("Invalid choice")  # Display the corresponding message with the user's name

    print("Finished.")  # Display a finished message when the program exits


if __name__ == "__main__":
    main()


"""

test

Enter name: mia
(H)ello
(G)oodbye
(Q)uit
>>> h
Hello mia
(H)ello
(G)oodbye
(Q)uit
>>> g
Goodbye mia
(H)ello
(G)oodbye
(Q)uit
>>> q
Finished.


"""