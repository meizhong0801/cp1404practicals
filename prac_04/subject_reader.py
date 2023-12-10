"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print("----------")
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            print(line)  # See what a line looks like
            print(repr(line))  # See what a line really looks like
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            print(parts)  # See what the parts look like (notice the integer is a string)
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            print(parts)  # See if that worked
            print("----------")
            data.append(parts)
    return data


def display_subject_details(data):
    """display subject details(data)"""

    for row in data:
        print(f"{row[0]} is taught by {row[1]:12} and has {row[2]:3} students")


main()

