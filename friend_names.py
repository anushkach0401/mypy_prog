import random
friends = ["john", "jane", "jacke", "jill"]
print(random.choice(friends))

# ask a list of names from user and then print a random name
names = input("Enter a list of names separated by comma: ").split(",")
print(random.choice(names))