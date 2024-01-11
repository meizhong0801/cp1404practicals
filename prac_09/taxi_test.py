from prac_09.taxi import Taxi


def run_tests():
    """Run simple tests/demos on Texi class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


if __name__ == "__main__":
    run_tests()





