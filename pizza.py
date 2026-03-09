print("Welcome to python pizza")
size=input("Enter s for small, l for large and m for medium pizza")
bill=0
if size=='s':
    bill+=15
elif size=='m':
    bill+=20
else:
    bill+=25
cheese=input("Do you want to add cheese(y/n)")
if cheese=='y':
    bill+=1
pep=input("Do u want to add pepperoni(y/n)?")
if size=='s':
    if pep=='y':
        bill+=2
else:
 if pep=='y':
        bill+=3
print(f"Your final bill is ${bill}")
   



