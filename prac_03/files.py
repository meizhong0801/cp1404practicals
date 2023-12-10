"""
do all the following separate questions in it:
Make sure you're confident with:

read()
readline()
readlines()
for line in file

"""


# 1.Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

name = input("Please enter your name: ")
out_file = open("name.txt", "w")
print(f"{name}", file=out_file)
out_file.close()


# 2.(In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name
# (as above) then prints,"Your name is Bob" (or whatever the name is in the file).

file = open("name.txt", "r")
name = file.read()
print(f"Your name is {name}")
file.close()


# 3.Create a text file called numbers.txt and save it in directory. Put the following three numbers on
# separate lines in the file and save it:

file = open("numbers.txt", "r")
numbers = file.readlines()
number_1 = int(numbers[0])
number_2 = int(numbers[1])
print(number_1 + number_2)
file.close()


# 4.write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers

sum = 0
file = open("numbers.txt", "r")
for line in file:
    number = int(line)
    sum += number
print(sum)
file.close()