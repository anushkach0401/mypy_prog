print("Welcome to treasure island, your mission is to find the treasure")
way=input("Left(l) or right(R)")
c=1
if way=='l':
    way=input("Swim(s)or wait(w)?")
else:
    print("Fall in hole, GAME OVER")
    c=0
if c==1:
    if way=='w':
        way=input("Which door(r/b/y)?")
    else:
        print("Attacked by trout, GAME OVER")
        c=0
if c==1:
    if way=='b':
        print("Attacked by Beast, GAME OVER")
        c=0
    elif way=='r':
        print("Burned by fire, GAME OVER")
        c=0
    elif way=='y':
        print("YOU WIN!")
    else:
        print("GAME OVER")
        
