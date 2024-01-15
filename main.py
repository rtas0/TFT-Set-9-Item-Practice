# import random function
import random

# Initialize lists
Current_Components = []
Current_Items = []
Carousel_Options = []

# Define constants
components = ["sword", "vest", "belt", "rod", "cloak", "bow", "glove", "tear"]
combined_names = {
     "sword+sword": "DB",
     "sword+vest": "EoN",
     "sword+belt": "Zekes",
     "sword+rod": "Gunblade",
     "sword+cloak": "BT",
     "sword+bow": "GS",
     "sword+glove": "IE",
     "sword+tear": "Shojin",
     "vest+sword": "EoN",
     "vest+vest": "Bramble",
     "vest+belt": "Sunfire",
     "vest+rod": "Locket",
     "vest+cloak": "Gargoyles",
     "vest+bow": "Titans",
     "vest+glove": "Shroud",
     "vest+tear": "Vow",
     "belt+sword": "Zekes",
     "belt+vest": "Sunfire",
     "belt+belt": "Warmogs",
     "belt+rod": "Morello",
     "belt+cloak": "Zephyr",
     "belt+bow": "Zzrot",
     "belt+glove": "Guardbreaker",
     "belt+tear": "Redemption",
     "rod+sword": "Gunblade",
     "rod+vest": "Locket",
     "rod+belt": "Morello",
     "rod+rod": "Deathcap",
     "rod+cloak": "Spark",
     "rod+bow": "Guinsoos",
     "rod+glove": "JG",
     "rod+tear": "Archangels",
     "cloak+sword": "BT",
     "cloak+vest": "Gargoyles",
     "cloak+belt": "Zephyr",
     "cloak+rod": "Spark",
     "cloak+cloak": "D Claw",
     "cloak+bow": "Runaans",
     "cloak+glove": "QSS",
     "cloak+tear": "Chalice",
     "bow+sword": "GS",
     "bow+vest": "Titans",
     "bow+belt": "Zzrot",
     "bow+rod": "Guinsoos",
     "bow+cloak": "Runaans",
     "bow+bow": "RFC",
     "bow+glove": "LW",
     "bow+tear": "Shiv",
     "glove+sword": "IE",
     "glove+vest": "Shroud",
     "glove+belt": "Guardbreaker",
     "glove+rod": "JG",
     "glove+cloak": "QSS",
     "glove+bow": "LW",
     "glove+glove": "TG",
     "glove+tear": "HoJ",
     "tear+sword": "Shojin",
     "tear+vest": "Vow",
     "tear+belt": "Redemption",
     "tear+rod": "Archangels",
     "tear+cloak": "Chalice",
     "tear+bow": "Shiv",
     "tear+glove": "HoJ",
     "tear+tear": "BB",
}


# Function to print information about the status of all variables
def print_current_items():

    print("Current components:", Current_Components)
    print("Current items:", Current_Items)
    # only print the carousel options if there are carousel options
    if len(Carousel_Options) != 0:
        print("Options from the Carousel are:", Carousel_Options)


# run until user chooses to stop the program
while True:
    command = input("Enter a command: (type 'help' to see a list of commands) ").lower()

    # show possible commands if the user enters the command "help"
    if command == "help":
        print("Possible commands: generate X, combine X+Y, reset, quit, carousel X")

    # if command starts with carousel
    elif command.startswith("carousel"):
        # split up the command into a list
        tokens = command.split()
        # if the command is asking to
        if len(tokens) == 2 and tokens[1].isdigit() and 3 <= int(tokens[1]) <= 9:
            num_carousel = int(tokens[1])
            new_carousel = random.choices(components, k=num_carousel)
            Carousel_Options.extend(new_carousel)
            print(num_carousel, "Carousel Options have been generated:", new_carousel)
            print_current_items()
        elif len(tokens) == 2 and tokens[1] in Carousel_Options:
            Current_Components.append(tokens[1])
            Carousel_Options = []
            print_current_items()
        else:
            print("Incorrect carousel command")

    elif command.startswith("generate"):
        tokens = command.split()
        if len(tokens) == 2 and tokens[1].isdigit():
            num_components = int(tokens[1])
            new_components = random.choices(components, k=num_components)
            Current_Components.extend(new_components)
            print("Generated", num_components, "components:", new_components)
            print_current_items()
        else:
            print("Invalid generate command format. Use 'generate X' where X is an integer.")

    elif command.startswith("combine"):
        tokens = command.split("combine")[1].strip().split("+")
        if len(tokens) == 2 and tokens[0].strip() in Current_Components and tokens[1].strip() in Current_Components:
            item_x = tokens[0].strip()
            item_y = tokens[1].strip()
            combined_key = item_x + "+" + item_y
            if combined_key in combined_names:
                combined_item = combined_names[combined_key]
                Current_Components.remove(item_x)
                Current_Components.remove(item_y)
                Current_Items.append(combined_item)
                print("Combined items", item_x, "and", item_y, "to create", combined_item)
                print_current_items()
            else:
                print("Invalid item combination")
        else:
            print("Invalid item names for combining.")

    # Set all lists back to empty status to start anew
    elif command == "reset":
        Current_Components = []
        Current_Items = []
        print("Items have been reset.")
        print_current_items()

    # if the user enters the command "quit", then the program stops running
    elif command == "quit":
        print("Quitting the game.")
        break
    # if the user enters an incorrect command, redirect the user to enter the command "help" to see the list of commands
    else:
        print("Invalid command. Type 'help' to see a list of commands.")
