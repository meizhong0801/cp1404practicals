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

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.keys())
    longest_word_length = max(len(word) for word in sorted_words)

    for word in sorted_words:
        print(f"{word:{longest_word_length}}: {word_count[word]}")


main()







