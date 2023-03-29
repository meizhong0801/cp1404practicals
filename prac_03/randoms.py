"""
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

What did you see on line 1?
5

What was the smallest number you could have seen, what was the largest?
smallest number is 5, largest number is 20

What did you see on line 2?
9

What was the smallest number you could have seen, what was the largest?
smallest number is 3, largest number is 9

Could line 2 have produced a 4?
No

What did you see on line 3?
4.132195502208947

What was the smallest number you could have seen, what was the largest?
smallest number is 2.5, largest number is 5.5

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""


import random

random_number = random.randint(1, 100)
print(random_number)


# test
# 53
# 45
# 93
