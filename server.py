import random
import re
import time
from flask import Flask
from flask import render_template
from flask import request, url_for


app = Flask(__name__)


# Timer for checking how fast it runs
# Grabs a file and returns the fileInput file
def grabFile():
    # What strings are being passed in
    # Uncomment things as needed
    filename = "grimm.txt"
    # filename = "egg fish egg fish Jimmy Jimmy Jimmy egg egg egg EGG FISH. egg jImMy egg-jimmy eg'g"

    # Placing individual words into fileInput list
    # Use the commented one for strings
    fileInput = open(filename).read().split()
    # fileInput = filename.split()
    return fileInput


# Makes list of lists that has the word and how many occurences it has
def makeList(fileInput):
    # Init
    dictList = {}
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
    return dictList


# Generates list based on probability and weights
def probGen(dictList, inputLen, wordAmt):
    # Finished list, the randomizer, and the number that goes up each time
    finishedList = []
    randomNum = random.random()
    accumulator = 0.0
    # Depending on how long you want the phrase to be,
    # Go through dictionary; keep adding its weight to accumulator
    # When accumulator hits over the random number, append to list
    for i in range(wordAmt):
        for key, value in dictList.items():
            accumulator += float(value/inputLen)
            if accumulator >= randomNum:
                randomNum = random.random()
                accumulator = 0.0
                cleanUp(key)
                finishedList.append(key)
                break
    return finishedList

def cleanUp(key):
    if key == "i":
        return "I"
    else:
        return key

# Print function
def printGen(finishedList):
    # Removes all non-alphanumeric (mostly brackets and commas)
    print(' '.join(finishedList).capitalize() + ".")
    return(' '.join(finishedList).capitalize() + ".")


# Everything is already histogram'd!
# Made sure to sort it
def histogram(dictList):
    histofile = open("histogram.txt", "w+")
    for value, key in sorted(dictList.items(), key=lambda s: s[1], reverse=True):
        histofile.write("%s, %s \n" % (value, key))
    histofile.close()


# What's passed in is the size of the list with unique words
def uniqueWords(uniqueWordAmt):
    print("There are", uniqueWordAmt, "unique words.")


# Prints whatever the word's frequency is
def frequency(word, dictList):
    if word in dictList:
        print("The word", "'"+word+"'", "shows up", dictList[word], "times.")
    else:
        print("The word",  "'"+word+"'", "does not show up!")


@app.route('/')
def main():
    # start time!
    start_time = time.time()
    # If you want a different file, see the grabFile function
    fileInput = grabFile()
    inputLen = len(fileInput)
    # Use input file; get dictionary of words+occurences
    dictList = makeList(fileInput)
    # List based on probability!
    # Also how long you want the string to be
    wordAmtInput = request.args.get('num', '')
    if wordAmtInput == '':
        wordAmt = 10
    else:
        wordAmt = int(wordAmtInput)
    # wordAmt = int(request.args.get('num', ''))
    # if wordAmt = '':
    #     wordAmt = 10
    finishedList = probGen(dictList, inputLen, wordAmt)
    # Print!
    printGen(finishedList)

    # Word you want to search up for frequency; change as needed
    word = "the"
    # The three programs needed
    histogram(dictList)
    uniqueWords(inputLen)
    frequency(word.lower(), dictList)
    # Timer!
    print("--- %s seconds ---" % (time.time() - start_time))
    return render_template('main.html', output=printGen(finishedList))


@app.route('/<url>')
def redirect(url):
    url = url+'.html'
    return render_template(url)

if __name__ == "__main__":
    main()
