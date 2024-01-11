"""
Unreliable_car class
"""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability attribute."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """generate a random number between 0 and 100, and only drive the car if that number is less than the
        car's reliability."""
        num = random.random() * 100
        if num < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0

        return distance_driven

    