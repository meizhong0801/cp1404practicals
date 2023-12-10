from prac_06.guitar import Guitar

guitars = []
name_length = 0
cost_length = 0
print("My guitars")
name = input("Name: ")
while name != "":
    if len(name) > name_length:
        name_length = len(name)
    year = int(input("Year: "))
    cost = input("Cost: $")
    if len(cost) > cost_length:
        cost_length = len(cost)
    guitar = Guitar(name, year, float(cost))
    guitars.append(guitar)
    name = input("\nName: ")

print("\n... snip ...")
print("\nThese are my guitars: ")

for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    txt = f"Guitar {i}: " + "{:>" + str(name_length + 1) + "} ({}), worth $ {:>" + str(cost_length + 1) + ",.2f} " + vintage_string
    print(txt.format(guitar.name, guitar.year, guitar.cost))



