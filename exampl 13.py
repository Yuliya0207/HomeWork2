from random import randrange

def a (y, x):
    return [randrange(0, x) for _ in range(y)]

def compareLists ():
    lis1 = a(10, 15)
    lis2 = a(20, 15)
    listWithDifferentItems = set(lis1).intersection(lis2)
    print(listWithDifferentItems)

compareLists ()
