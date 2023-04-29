from prac_06.guitar import Guitar


gibson_l5 = Guitar("Gibson L-5", 1922, 16035.50)
another_guitar = Guitar("Another_guitar", 2013, 100.35)

print(f"Gibson L-5 CES get_age() - Expected 100. Got {gibson_l5.get_age()}")
print(f"Another Guitar get_age() - Expected 9. Got {another_guitar.get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson_l5.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")