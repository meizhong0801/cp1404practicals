"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# get sales
# while sales >= 0
#     calculate bonus
#     get sales
# do next thing


sales = float(input(" Enter sales: $"))

while sales >=0:
    if sales <= 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Your bonus is: ", bonus)
    sales = float(input(" Enter sales: $"))


"""
test

 Enter sales: $0
Your bonus is:  0.0
 Enter sales: $1000
Your bonus is:  100.0
 Enter sales: $99
Your bonus is:  9.9
 Enter sales: $1001
Your bonus is:  150.15
 Enter sales: $-1

Process finished with exit code 0

"""
