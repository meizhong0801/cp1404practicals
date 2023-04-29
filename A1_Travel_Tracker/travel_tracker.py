from operator import itemgetter
from random import randint

MY_NAME = "Mei Zhong"
FILE = "places.csv"
MENU = """Menu:
L - List places
R - Recommend random place
A - Add new place
M - Mark a place as visited
Q - Quit"""

# Set places as global varialbe
# places = read_data(FILE)

def main():
    print(f"Travel Tracker 1.0 - by {MY_NAME}")
    print(MENU)
    places = read_data(FILE)
    choice = input(">>> ").upper()
    while choice.upper() not in "L R M A Q".split():
        print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            list_places(places)
        elif choice == "R":
            recommend_random_place(places)
        elif choice == "M":
            places = mark_place_visited(places)
        elif choice == "A":
            add_place(places)
        print(MENU)
        choice = input(">>> ").upper()
    
    save_data(places, FILE)
    print("Have a nice day :)")


def read_data(file):
    places = []
    with open(file, "r") as f:
        
        for line in f.readlines():
            a_dict = {}
            a_list = line.strip().split(",")
            a_dict['city'] = a_list[0]
            a_dict['country'] = a_list[1]
            a_dict['priority'] = int(a_list[2])
            a_dict['visited'] = a_list[3]
            places.append(a_dict)
    return places

def sort_places_by_visited_priority(places):
    return sorted(places, key=itemgetter('visited', 'priority'))

def list_places(places):
    places = sort_places_by_visited_priority(places)
    for i, place in enumerate(places, 1):
        star = "*" if place["visited"] == "n" else " "
        print(f"{star}{i}. {place['city']:>10} in {place['country']:>15} {place['priority']:>3}")
    unvisited = check_unvisited(places)
    if unvisited > 0:
        print(f"{len(places)} places. You still want to visit {unvisited} places.")
    else:
        print(f"{len(places)} places. No places left to visit. Why not add a new place?")
    return places

def check_unvisited(places):
    unvisited = 0
    for place in places:
        if place["visited"] == "n":
            unvisited += 1
    return unvisited

    
def recommend_random_place(places):
    if check_unvisited(places) > 0:
        unvisited_places = [ place for place in places if place["visited"] == "n"]
        random_num = randint(0, len(unvisited_places) - 1)
        print("Not sure where to visit next?")
        print(f"How about... {unvisited_places[random_num]['city']} in {unvisited_places[random_num]['country']}?")
    else:
        print("No places left to visit!")


def mark_place_visited(places):
    if check_unvisited(places) == 0:
        print("No unvisited places")
    else:
        places = list_places(places)
        print("Enert the number of a place to mark as visited")
        is_valid = False
        while not is_valid:
            try:
                number = int(input(">>> "))
            except:
                print("Invalid input; enter a valid number")
            else:
                if number <= 0:
                    print("Number must be > 0")
                elif number > len(places):
                    print("Invalid place number")
                else:
                    is_valid = True
        
        if places[number - 1]['visited'] == "v":
            print(f"You have already visited {places[number - 1]['city']}")
        else:
            places[number - 1]['visited'] = "v"
            print(f"{places[number - 1]['city']} in {places[number - 1]['country']} visited")
    
    return places


def get_valid_input(input_name, type="STR"):
    prompt_str = input_name.title() + ": "  
    is_valid = False
    
    while not is_valid:
        user_input = input(prompt_str)  
        if user_input == "":
            print("Input can not be blank")
        elif type.upper() != "INT":
            is_valid = True
        elif not user_input.isnumeric():
            print("Priority must be a whole number")
        else:
            is_valid = True
        
    if type.upper() == "INT":
            user_input = int(user_input)

    return user_input


def add_place(places):
    name = get_valid_input("name").title()
    country = get_valid_input("country").title()
    priority = get_valid_input("priority", type="int")
    places.append(
        {
            "city": name,
            "country": country,
            "priority": priority,
            "visited": "n"
        }
    ) 
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")
    return places


def save_data(places, file):
    with open(file, "w") as f:
        for place in places:
            f.write(f"{place['city']},{place['country']},{place['priority']}, {place['visited']}\n")
    print(f"{len(places)} places saved to {file}")
    

main()