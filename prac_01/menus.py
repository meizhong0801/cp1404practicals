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


menu = ["(H)ello", "(G)oodbye", "(Q)uit"]
name = input("Enter name: ")
# display menu
for x in menu:
    print(x)
your_choice = input(">>> ").upper()
while your_choice != "Q":
    # process choices
    if your_choice =="H":
        print("hello", name)
    elif your_choice == "G":
        print("goodbye", name)
    else:
        print("Invalid choice")
    # display menu
    for x in menu:
        print(x)
    your_choice = input(">>> ").upper()
print("Finished.")



"""
# Test:

Enter name: simon
(H)ello
(G)oodbye
(Q)uit
>>> a
Invalid choice
(H)ello
(G)oodbye
(Q)uit
>>> h
hello simon
(H)ello
(G)oodbye
(Q)uit
>>> g
goodbye simon
(H)ello
(G)oodbye
(Q)uit
>>> q
Finished.
"""