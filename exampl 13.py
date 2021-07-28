from random import randrange

def a (y, x):
    return [randrange(0, x) for _ in range(y)]

def compareLists ():
    lis3 = a(15, 15)
    lis4 = a(15, 15)
    listWithDifferentItems = set(lis3).intersection(lis4)
    print(listWithDifferentItems)

compareLists ()