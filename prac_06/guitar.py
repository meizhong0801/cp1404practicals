class Guitar:
    """Represent a Guiar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Car instance.

        cost: float, the cost of a guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.,2f}"

    def get_age(self):
        return 2022 - self.year

    def is_vintage(self):
        return self.get_age() >= 50


    