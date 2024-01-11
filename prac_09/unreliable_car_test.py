from prac_09.unreliable_car import UnreliableCar


def run_tests():
    """Run simple tests/demos on Unreliable_car class."""
    my_unreliable_car = UnreliableCar("Prius 1", 100, 50.3)
    my_unreliable_car.drive(40)
    print(my_unreliable_car)


if __name__ == "__main__":
    run_tests()


