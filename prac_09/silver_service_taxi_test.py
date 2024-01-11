from prac_09.silver_service_taxi import SilverServiceTaxi


def run_tests():
    """Run simple tests/demos on Unreliable_car class."""
    my_silver_service_taxi= SilverServiceTaxi("Prius 1", 100, 2)
    my_silver_service_taxi.drive(18)
    print(my_silver_service_taxi)
    print(f"For an 18km trip in a SilverServiceTaxi with fanciness of {my_silver_service_taxi.fanciness}, the fare should be ${my_silver_service_taxi.get_fare():.2f}")


if __name__ == "__main__":
    run_tests()



