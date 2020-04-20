def superhero_intro(dictionary):
    for key, val in dictionary.items():
        print(f'My superhero name is {key} and my superpower is {val}')


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

superhero_intro(super_heroes)

# name = input("What is your name?")
# print(f'Hello there {name}')
