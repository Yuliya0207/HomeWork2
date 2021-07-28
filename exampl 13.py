from random import randrange


def createList (iterationCount, maxRandomValue):
    return [randrange(0, maxRandomValue) for x in range(iterationCount)]




def createListsAndPrintDifferences():
    lis3 = createList(15, 15)
    lis4 = createList(15, 15)
    listWithDifferentItems = set(lis3).intersection(lis4)
    print(listWithDifferentItems)

createListsAndPrintDifferences()