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


# print the income report based on the 'incomes' list and the number of months
def print_report(incomes, months_num):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months_num + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()


