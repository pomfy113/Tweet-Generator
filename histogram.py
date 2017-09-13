import random
import string
import numpy
import re
import time

start_time = time.time()

# Grabs a file and returns the dictionary file
def grabFile():
    # What strings are being passed in
    # Uncomment things as needed
    filename = "/Users/fcruz/Documents/GitHub/Tweet-Maker/grimm.txt"
    # filename = "egg fish egg fish James James James James egg egg egg EGG FISH. egg jAmEs"

    # Placing individual words into dictionary list
    # Use the commented one for strings
    dictionary = open(filename).read().split()
    # dictionary = filename.split()
    return dictionary

# Makes list of lists that has the word and how many occurences it has
def makeList(dictionary):
    # Init
    dictlist = []
    alreadyplaced = []
    totalwords = len(dictionary)
    currentWord = 0

    # Loops through every element in dictionary
    # Removes any non alphanumeric; turns everything into lowercase
    for i in range(len(dictionary)):
        dictionary[i] = re.sub('[^0-9a-zA-Z]+', '', dictionary[i]).lower()

        # Check if already seen; if so, add 1 to occurences
        # Second element is how many times the word has occurred already
        if dictionary[i] in alreadyplaced:
            dictlist[alreadyplaced.index(dictionary[i])][1] += 1

        # If not seen yet, create a new list within dictlist
        # First occurence means second element is "1" (see above)
        else:
            dictlist.append([dictionary[i], 1])
            alreadyplaced.append(dictionary[i])

    return (dictlist, alreadyplaced)

# Generates probability list of word based on occurences
def probGen(dictlist, dictionary):
    probability = []
    # Divide the occurence amount by total amount of words
    for k in range(len(dictlist)):
        probability.append(float(dictlist[k][1])/len(dictionary))
    return probability

# Print function
def printGen(alreadyplaced,probability):
    # Generates words based on probability, makes it into string, puts into list
    # Removes all non-alphanumeric (mostly brackets and commas)
    finishedList = str(numpy.random.choice(alreadyplaced,10,p=probability))
    print (re.sub('[^0-9a-zA-Z ]+', '', finishedList).capitalize() + ".")

if __name__ == "__main__":
    dictionary = grabFile()
    dictlist,alreadyplaced = makeList(dictionary)
    printGen(alreadyplaced,probGen(dictlist,dictionary))
    print("--- %s seconds ---" % (time.time() - start_time))
