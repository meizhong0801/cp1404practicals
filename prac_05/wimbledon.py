"""
Write a program to read this file, process the data and display processed information.
the champions and how many times they have won.
the countries of the champions in alphabetical order

"""


def main():
    filename = "wimbledon.csv"
    data = read_file(filename)    # Read the data from the CSV file.
    champion_to_count = count_champions(data)    # Count how many times each champion has won.
    champion_countries = collect_champion_countries(data)   # Collect the countries of the champions.

    print("Wimbledon Champions: ")
    for champion, wins in champion_to_count.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(champion_countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(champion_countries)))


# Read data from a CSV file and return it as a list of lists.
def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
    results = []
    for line in lines[1:]:
        results.append(line.strip().split(","))
    return results


# Count how many times each champion has won and store the results in a dictionary.
def count_champions(data):
    a_dict = {}
    for line in data:
        name = line[2]
        if name in a_dict:
            a_dict[name] += 1
        else:
            a_dict[name] = 1
    return a_dict


# Collect the unique countries of the champions and return them as a set.
def collect_champion_countries(data):
    countries = set()
    for line in data:
        country = line[1]
        if country not in countries:
            countries.add(country)
    return countries


main()


