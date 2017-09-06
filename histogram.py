import random

# filename = "/Users/fcruz/Documents/GitHub/Tweet-Maker/grimm.txt"
testfilename = "egg fish egg fish James James James "

# def histogram(filename):
# dictionary = open(filename).read().split
dictionary = testfilename.split()
testlist = []
templist = []
j = 0
for i in range(len(dictionary)):
    if dictionary[i] in testlist:
        templist.append((dictionary[i], j+1))
        print templist
    testlist.append(dictionary[i])
    print dictionary[i]
