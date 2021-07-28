import random
lis1=[random.randint(1,15) for i in range(15)]
lis2=[random.randint(1,10) for i in range(10)]
c=[]
print(lis1)
print(lis2)
for i in lis1:
    if i in lis2:
        continue
    for x in lis2:
        if i == x:
            c.append(i)
            break
print(c)


