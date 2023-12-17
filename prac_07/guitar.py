"""
Guitar class with tests.
"""


class Guitar:
    """Represent information about a guitar."""


    def __init__(self, name, year, cost):
        """Construct a Guitar from the given values."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare two guitars based on their manufacturing year."""
        return self.year < other.year

    def get_age(self):
        """Calculate and return the age of the guitar based on the current year (2022)."""
        return 2022 - self.year

    def is_vintage(self):
        """Determine if the guitar is considered vintage (50 years or older)."""
        return self.get_age() >= 50


def run_tests():
    """Run simple tests/demos on Guitar class."""
    fender = Guitar("Fender", 2014, 765.4)
    gibson = Guitar("Gibson", 1922, 16035.4)
    line = Guitar("Line", 2010, 1512.9)

    guitars = [fender, gibson, line]
    print(fender)

    oldest = fender
    for guitar in guitars:
        if guitar < oldest:
            oldest = guitar
    print(f"The oldest guitars is {oldest.name}")


if __name__ == "__main__":
    run_tests()

