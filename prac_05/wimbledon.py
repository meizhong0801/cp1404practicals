"""
Write a program to read this file, process the data and display processed information.

the champions and how many times they have won.
the countries of the champions in alphabetical order
Requirements and Hints
You need to store the data in appropriate data structures.
The solution uses: a list of lists, a dictionary and a set.

The file is not in simple ASCII format but UTF-8 with a byte order mark, or BOM.
You can account for this by setting the encoding like:

with open(filename, "r", encoding="utf-8-sig") as in_file:
For the final output of countries, use the join method to create a single string.

Use functions for each logical step/chunk of the program.
If you write it all in main to start with, that's fine, but then refactor it.
The solution uses 4 functions including main.
"""


def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)
    champion_to_count = count_champions(data)
    champion_countries = collect_champion_countries(data)

    print("Wimbledon Champions: ")
    for champion, wins in champion_to_count.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(champion_countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(champion_countries)))


def read_csv(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
    results = []
    for line in lines[1:]:
        results.append(line.strip().split(","))
    return results


def count_champions(data):
    a_dict = {}
    for line in data:
        name = line[2]
        if name in a_dict:
            a_dict[name] += 1
        else:
            a_dict[name] = 1
    return a_dict


def collect_champion_countries(data):
    countries = set()
    for line in data:
        country = line[1]
        if country not in countries:
            countries.add(country)
    return countries


main()


# test
# Wimbledon Champions:
# Rod Laver 2
# John Newcombe 2
# Stan Smith 1
# Jan Kodeš 1
# Jimmy Connors 2
# Arthur Ashe 1
# Björn Borg 5
# John McEnroe 3
# Boris Becker 3
# Pat Cash 1
# Stefan Edberg 2
# Michael Stich 1
# Andre Agassi 1
# Pete Sampras 7
# Richard Krajicek 1
# Goran Ivanišević 1
# Lleyton Hewitt 1
# Roger Federer 8
# Rafael Nadal 2
# Novak Djokovic 7
# Andy Murray 2
#
# These 12 countries have won Wimbledon:
# AUS, CRO, ESP, FRG, GBR, GER, NED, SRB, SUI, SWE, TCH, USA
