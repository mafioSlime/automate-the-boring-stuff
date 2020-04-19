fruits = ['orange', 'pear', 'mango', 'strawberry']

# regular loops
# for fruit in fruits:
#     print(fruit)

# specific range
# for fruit in fruits[1:3]:
#     print(fruit)

for fruit in fruits:
    if fruit == "mango":
        print(f"{fruit} is delicious!")
        break
    else:
        print(fruit)
