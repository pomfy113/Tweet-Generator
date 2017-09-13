import random
import string
import numpy
import re
import time

start_time = time.time()

# Grabs a file and returns the fileInput file
def grabFile():
    # What strings are being passed in
    # Uncomment things as needed
    filename = "/Users/fcruz/Documents/GitHub/Tweet-Maker/grimm.txt"
    # filename = "egg fish egg fish James James James James egg egg egg EGG FISH. egg jAmEs"

    # Placing individual words into fileInput list
    # Use the commented one for strings
    fileInput = open(filename).read().split()
    # fileInput = filename.split()
    return fileInput

# Makes list of lists that has the word and how many occurences it has
def makeList(fileInput):
    # Init
    dictList = {}
    placedWords = []
    totalwords = len(fileInput)
    currentWord = 0

    # Loops through every element in fileInput
    # Removes any non alphanumeric; turns everything into lowercase
    for i in range(len(fileInput)):
        fileInput[i] = re.sub('[^0-9a-zA-Z]+', '', fileInput[i]).lower()

        # Check if already seen; if so, add 1 to occurences
        # Second element is how many times the word has occurred already
        if fileInput[i] in dictList:
            dictList[fileInput[i]] +=1

        # If not seen yet, create a new list within dictList
        # First occurence means second element is "1" (see above)
        else:
            dictList[fileInput[i]] = 1
            placedWords.append(fileInput[i])
    return (dictList, placedWords)

# Generates probability list of word based on occurences
def probGen(dictList, placedWords,inputLen):
    # Making a list of probability; can access probability using indexes
    probability = []
    # Divide the occurence amount by total amount of words
    for k in range(len(dictList)):
        probability.append(float(dictList[placedWords[k]])/inputLen)
    return probability

# Print function
def printGen(placedWords,probability):
    # Generates words based on probability, makes it into string, puts into list
    # Removes all non-alphanumeric (mostly brackets and commas)
    finishedList = str(numpy.random.choice(placedWords,10,p=probability))
    print (re.sub('[^0-9a-zA-Z ]+', '', finishedList).capitalize() + ".")

# Main function
if __name__ == "__main__":
    fileInput = grabFile()
    dictList,placedWords = makeList(fileInput)
    printGen(placedWords,probGen(dictList,placedWords, len(fileInput)))
    print("--- %s seconds ---" % (time.time() - start_time))
