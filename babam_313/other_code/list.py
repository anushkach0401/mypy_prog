list=[]
total=0
count=0
while True:
    n=input("Enter number")
    if n=="done":
        break
    num=(float)(n)
    list.append(num)
avg=sum(list)/len(list)
print(avg)

