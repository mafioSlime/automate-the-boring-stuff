# def greet(name, time):
#     print(f"Good {time}, {name}, hope you are well...")


# greet("Waka", "Night")

# name = input("Enter your name>")
# time = input("Enter time of the day>")


# def greet(name, time):
#     print(f"Hello there {name}, Good {time}, to you... ")


# greet(name, time)

# DEFAULT

# def greet(name="Little one", time="Life"):
#     print(f"Hello there {name}, Good {time} to you...")


# greet("Ebi", "Night")

# RADIUS

radius = int(input("Enter radius>"))
length = int(input("Enter length>"))


def area(radius):
    return (3.142 * radius * radius)


given_area = area(radius)


def vol(given_area, length):
    print(given_area * length)


vol(area(radius), length)
