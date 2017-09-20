import random
import string
import numpy
import re
import time

# Timer for checking how fast it runs
start_time = time.time()


# Grabs a file and returns the fileInput file
def grabFile():
    # What strings are being passed in
    # Uncomment things as needed
    filename = "/Users/fcruz/Documents/GitHub/Tweet-Maker/grimm.txt"
    # filename = "egg fish egg fish Jimmy Jimmy Jimmy egg egg egg EGG FISH. egg jImMy egg-jimmy"

    # Placing individual words into fileInput list
    # Use the commented one for strings
    fileInput = open(filename).read().split()
    # fileInput = filename.split()
    return fileInput


# Makes list of lists that has the word and how many occurences it has
def makeList(fileInput):
    # Init
    dictList = {}
    parsedWords = []
    totalwords = len(fileInput)
    currentWord = 0
    # Loops through every element in fileInput
    # Removes any non alphanumeric; turns everything into lowercase
    for word in fileInput:
        word = re.sub('[^a-zA-Z\-]+', '', word).lower()

        # Check if already seen; if so, add 1 to occurences
        # Second element is how many times the word has occurred already
        if word in dictList:
            dictList[word] += 1

        # If not seen yet, create a new list within dictList
        # First occurence means second element is "1" (see above)
        else:
            dictList[word] = 1
            parsedWords.append(word)
    return (dictList, parsedWords)


# Generates probability list of word based on occurences
def probGen(dictList, parsedWords, inputLen):
    # Making a list of probability; can access probability using indexes
    probability = []
    # Divide the occurence amount by total amount of words
    for k in range(len(dictList)):
        probability.append(float(dictList[parsedWords[k]])/inputLen)
    return probability


# Print function
def printGen(parsedWords, probability):
    # Generates words based on probability, makes into string, puts into list
    # Removes all non-alphanumeric (mostly brackets and commas)
    finishedList = str(numpy.random.choice(parsedWords, 10, p=probability))
    print(finishedList)
    print(re.sub('[^a-zA-Z\-\ ]+', '', finishedList).capitalize() + ".")


# Everything is already histogram'd!
def histogram(dictList):
    for keys,values in dictList.items():
        print(keys, values)

# What's passed in is the size of the list with unique words
def uniqueWords(uniqueWordAmt):
    print("There are", uniqueWordAmt, "unique words.")


# Returns whatever the word's frequency is
def frequency(word, dictList):
    if word in dictList:
        print("The word", "'"+word+"'", "shows up", dictList[word], "times.")


# Main function
if __name__ == "__main__":
    # If you want a different file, see the grabFile function
    fileInput = grabFile()
    # Use input file; get dictionary of words+occurences and all unique words
    dictList, parsedWords = makeList(fileInput)
    # Probability list!
    probList = probGen(dictList, parsedWords, len(fileInput))
    # Print!
    printGen(parsedWords, probList)

    # Word you want to search up for frequency; change as needed
    word = "the"
    # The three programs needed
    histogram(dictList)
    uniqueWords(len(parsedWords))
    frequency(word, dictList)
    # Timer!
    print("--- %s seconds ---" % (time.time() - start_time))
