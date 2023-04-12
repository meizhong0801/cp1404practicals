"""
Based on the state name example program above, create a program that allows you to look up hexadecimal colour
codes like those at http://www.color-hex.com/color-names.html

Use a constant dictionary of about 10 colour names and write a program that allows a user to enter a name and get
the code, e.g., entering AliceBlue (or aliceblue - make it case-independent) should show #f0f8ff.

Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.
"""

COLOR_TO_CODE = {
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "aqua": "#00ffff",
    "beaver": "#9f8170",
    "blond": "#faf0be",
    "byzantium": "#702963",
    "cadetBlue": "#5f9ea0",
    "crystal": "#a7d8de",
    "darkkhaki": "#bdb76b",
    "cream": "#fffdd0",
}


def main():
    color_name = input("Enter color name (blank to quit): ").lower()
    while color_name != "":
        if color_name in COLOR_TO_CODE:
            print(f"{color_name.capitalize()} is {COLOR_TO_CODE[color_name]}")
        else:
            print("Invalid color name")
        color_name = input("Enter color name (blank to quit): ").lower()


main()
