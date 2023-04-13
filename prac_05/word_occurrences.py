"""
Write a program to count the occurrences of words in a string. The program should ask the user for a string,
then print the counts of how many of each word are in the string.
The output should look like this (depending on user input):

Text: this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2

"""


def main():
    text = input("Text: ").lower()
    words = text.split()

    # count the number of each word
    word_summary = {}
    for item in words:
        if item in word_summary:
            word_summary[item] += 1
        else:
            word_summary[item] = 1

    # look for maximum word length
    max_length = 0
    for item in words:
        if len(item) > max_length:
            max_length = len(item)

    # display word and its count ordered alphabetically
    ordered_words = sorted(word_summary.keys())
    for item in ordered_words:
        print(f"{item:{max_length}}: {word_summary[item]}")


main()


# test
# Text: this is a collection of words of nice words this is a fun thing it is
# a         : 2
# collection: 1
# fun       : 1
# is        : 3
# it        : 1
# nice      : 1
# of        : 2
# thing     : 1
# this      : 2
# words     : 2



