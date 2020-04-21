# def superhero_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f'My superhero name is {key} and my superpower is {val}')

# belts = ["black", "black", "red", "white"]
# print(belts.count("black"))
# heroes = {"batman": "black", "robin": "red"}
# print(list(heroes.values()))


def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f"There are {num} {belt} belts")


super_heroes = {}

while True:
    hero_name = input("Enter your hero name>")
    hero_power = input("Enter your super powers>")
    super_heroes[hero_name] = hero_power

    another_hero = input("Do you want to add another hero? (Y/N)")
    if another_hero == "Y":
        continue
    else:
        break

belt_count(super_heroes)

# print(belts)

# superhero_intro(super_heroes)

# name = input("What is your name?")
# print(f'Hello there {name}')
