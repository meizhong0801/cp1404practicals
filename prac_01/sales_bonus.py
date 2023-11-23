"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

"""


sales = float(input("Enter sales: $ "))

while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(f"You get {bonus} bonus in total! ")
    sales = float(input("Enter sales: $ "))


"""
test

Enter sales: $ 500
You get 50.0 bonus in total! 
Enter sales: $ 1000
You get 150.0 bonus in total! 
Enter sales: $ 2000
You get 300.0 bonus in total! 
Enter sales: $ 999
You get 99.9 bonus in total! 
...

"""