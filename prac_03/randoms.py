import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# random integer between 5 and 20, both inclusive.

# What was the smallest number you could have seen, what was the largest?
# the smallest number is 5, and largest number is 20.

# What did you see on line 2?
# random integer between 3 and 10 with a step of 2

# What was the smallest number you could have seen, what was the largest?
# the smallest number is 3, and largest number is 9.
# Could line 2 have produced a 4?
# could not produce 4.

# What did you see on line 3?
# random floating-point number between 2.5 (inclusive) and 5.5 (exclusive)

# What was the smallest number you could have seen, what was the largest?
# the smallest number is 2.5, and largest number is less than 5.5.


# produce a random number between 1 and 100 inclusive
import random

random_number = random.randint(1, 100)
print(random_number)
