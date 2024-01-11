from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_available_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            bill_to_date += drive_taxi(current_taxi)
        elif choice != "q":
            print("Invalid option")

        display_bill(bill_to_date)
        print(MENU)
        choice = input(">>> ").lower()
    summarize(taxis, bill_to_date)


def drive_taxi(taxi):
    """ simulate driving a taxi and calculate the fare """
    if not taxi:
        print("You need to choose a taxi before you can drive")
        return 0
    else:
        taxi.start_fare()
        distance = float(input("Drive how far? "))
        taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${taxi.get_fare():.2f}")

    return taxi.get_fare()


def display_available_taxis(taxis):
    """ display the available taxis for the user to choose from """
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """ allow the user to choose a taxi """
    taxi_num = int(input("Choose taxi: "))
    if taxi_num < 0 or taxi_num >= len(taxis):
        print("Invalid taxi choice")
        my_taxi = None
    else:
        my_taxi = taxis[taxi_num]

    return my_taxi


def display_bill(current_bill):
    """ display the current bill to the user """
    print(f"Bill to date: ${current_bill:.2f}")


def summarize(taxis, bill):
    """ summarize the total trip cost and display the current state of each taxi """
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()

