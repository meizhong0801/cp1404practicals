"""
get score
while score is out of 0 to 100
    print invalid score!
    get score again
if score >= 90
    print your score is excellent
elif score >=50
    print your score is pass
else
    print your score is bad
"""


# get valid score input
score = int(input("Please enter your score:  "))
while score < 0 or score > 100:
    print("Your score is invalid!")
    score = int(input("Please enter your score:  "))

# determine score category
if score >= 90:
    print("Your score is excellent!")
elif score >= 50:
    print("Your score is pass!")
else:
    print("Your score is bad!!")


"""
test 

-1
Please enter your score:  -1
Your score is invalid!
Please enter your score:  

0
Please enter your score:  0
Your score is bad!!

49
Please enter your score:  49
Your score is bad!!

50
Please enter your score:  50
Your score is pass!

89
Please enter your score:  89
Your score is pass!

90
Please enter your score:  90
Your score is excellent!

100
Please enter your score:  100
Your score is excellent!

101
Please enter your score:  101
Your score is invalid!
Please enter your score:  

"""