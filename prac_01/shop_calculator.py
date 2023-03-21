"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed
on the screen.

"""


total_price = 0
items = int(input("Enter number of items: "))
# get price input
for i in range(items):
    price = float(input("Enter your price: "))
    total_price = total_price + price
# If the total price is over $100, then a 10% discount is applied
if total_price > 100:
    total_price = total_price * 0.9
print(f"your total price is: ${total_price: .2f} ")


# test

# total price is over $100:
    # Enter number of items: 2
    # Enter your price: 60
    # Enter your price: 50
    # your total price is: $ 99.00

# total price is below $100:
    # Enter number of items: 2
    # Enter your price: 40
    # Enter your price: 20
    # your total price is: $ 60.00

# total price is $100:
    # Enter number of items: 2
    # Enter your price: 50
    # Enter your price: 50
    # your total price is: $ 100.00