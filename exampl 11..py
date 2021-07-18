from random import sample
lis = sample(range(1,100), k=10)
print(lis)
a=lis.index(int(input("What number should be replaced?: ")))
b=int(input("Specif the number: "))
print(lis)