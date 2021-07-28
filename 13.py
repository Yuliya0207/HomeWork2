from random import randrange
lis1=15
lis2=15
lis3=[randrange (0,15) for x in range (lis1)]
lis4=[randrange(0,15) for x in range(lis2)]
print(lis3)
print(lis4)
y=set(lis3).intersection(lis4)
print(y)
