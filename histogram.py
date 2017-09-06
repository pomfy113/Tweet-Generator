import random

# filename = "/Users/fcruz/Documents/GitHub/Tweet-Maker/grimm.txt"
testfilename = "egg fish egg fish James James James "

# def histogram(filename):
# dictionary = open(filename).read().split
dictionary = testfilename.split()
templist = []
alreadyplaced = []
j = -1
for i in range(len(dictionary)):
    if dictionary[i] in alreadyplaced:
        templist[alreadyplaced.index(dictionary[i])] = [templist[alreadyplaced.index(dictionary[i])][0], templist[j][1]+1]
    else:
        templist.append((dictionary[i], 1))
        alreadyplaced.append(dictionary[i])
        j = j+1
    #print j
    print dictionary[i]
    print templist
