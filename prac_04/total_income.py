"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_num = int(input("How many months? "))

    for month in range(1, months_num + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_report(incomes, months_num)


def print_report(incomes, months_num):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months_num + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()


# test

# How many months? 5
# Enter income for month 1: 10000
# Enter income for month 2: 22000
# Enter income for month 3: 33300
# Enter income for month 4: 22222
# Enter income for month 5: 30000
#
# Income Report
# -------------
# Month  1 - Income: $  10000.00 Total: $  10000.00
# Month  2 - Income: $  22000.00 Total: $  32000.00
# Month  3 - Income: $  33300.00 Total: $  65300.00
# Month  4 - Income: $  22222.00 Total: $  87522.00
# Month  5 - Income: $  30000.00 Total: $ 117522.00
