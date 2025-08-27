import random
print("Random float number",random.random())
print("Random integer number",random.randint(1, 10))

fruits = ["banana", "apple", "orange", "grapes", "mango"]
print("Random fruit",random.choice(fruits))

elm = ["Water", "Fire", "Air", "Earth"]
random.shuffle(elm)
print("Shuffled list",elm)
print("Random sample",random.sample(elm, 2))
