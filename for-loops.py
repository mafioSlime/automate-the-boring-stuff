fruits = ['orange', 'pear', 'mango', 'strawberry']

# regular loops
# for fruit in fruits:
#     print(fruit)

# specific range
# for fruit in fruits[1:3]:
#     print(fruit)

# for fruit in fruits:
#     if fruit == "mango":
#         print(f"{fruit} is delicious!")
#         break
#     else:
#         print(fruit)

# WHILE LOOPS

age = 25
num = 0

# while num < age:
#     if num == 0:
#         num += 1
#         continue
#     if num % 2 == 0:
#         print(num)
#     if num > 10:
#         break
#     num += 1

while num < age:
    if num == 2:
        print(f"{num} is my favorite number")
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num += 1
