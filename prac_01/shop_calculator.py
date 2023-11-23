"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.

"""

total_price = 0
items = int(input("Enter number of items: "))

while items < 0:
    print("Number of items cannot be negative. Please enter a valid number.")
    items = int(input("Enter number of items: "))

# Get price input and calculate total price
for i in range(items):
    price = float(input("Enter your price: "))

    while price < 0:
        print("Price cannot be negative. Please enter a valid price.")
        price = float(input("Enter your price: "))

        total_price += price

# Apply discount if total price is over $100
if total_price > 100:
    total_price = total_price * 0.9   # Apply a 10% discount

# Display the total price with two decimal places
print(f"Your total price is: ${total_price: .2f} ")



# test

# total price is over $100:
    # Enter number of items: 2
    # Enter your price: 60
    # Enter your price: 60
    # your total price is: $ 108.00

# total price is below $100:
    # Enter number of items: 1
    # Enter your price: 50
    # your total price is: $ 50.00

# total price is $100:
    # Enter number of items: 1
    # Enter your price:100
    # your total price is: $ 100.00


