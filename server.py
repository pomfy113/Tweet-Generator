import random
import re
import time
import string
from flask import Flask
from flask import render_template
from flask import request, url_for


app = Flask(__name__)



def grabFile():
    """Grabs file and splits it all into a list of words"""
    # Test string below filename
    filename = "grimm.txt"
    # testfilename = "egg fish egg fish Jimmy Jimmy Jimmy egg egg egg EGG FISH. egg jImMy egg-jimmy eg'g"

    # Placing individual words into fileInput list
    # Use the commented one for testing/raw strings
    fileInput = open(filename).read().split()
    # testfileInput = testfilename.split()
    return fileInput


# Makes dictionary that has the word and how many occurences it has
def makeList(fileInput):
    # List of things I want to capitalize
    capitalizethese = ('i')
    dictList = {}

    # Loops through every element in fileInput
    # Removes any non alphanumeric + turns word into lowercase
    # Dictionary is {'word; amount of occurences'}
    for word in fileInput:
        word = re.sub('[^a-zA-Z\-]+', '', word).lower()
        if word in capitalizethese:
            word = word.capitalize()
        if word in dictList:
            dictList[word] += 1
        else:
            dictList[word] = 1
    return dictList


# Generates list based on probability and weights
def probGen(dictList, inputLen, wordAmt):
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
                finishedList.append(key)
                break
    finishedList[0] = finishedList[0].capitalize()
    return finishedList

# Print function
def printGen(finishedList):
    print(' '.join(finishedList) + ".")
    return(' '.join(finishedList) + ".")

# Everything is already histogram'd
# Sorted by the keys, from highest to lowest
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
    start_time = time.time()
    # Grabs input + input length
    fileInput = grabFile()
    inputLen = len(fileInput)
    # Use input file; get dictionary of words+occurences
    dictList = makeList(fileInput)

    # Grabs how long you want string to be; defaults to 10
    wordAmtInput = request.args.get('num', '')
    if wordAmtInput == '':
        wordAmt = 10
    else:
        wordAmt = int(wordAmtInput)

    # List based on probability
    # Grabs list, length of dictionary, and desired string length
    finishedList = probGen(dictList, inputLen, wordAmt)

    printGen(finishedList)

    # Word you want to search up for frequency; change as needed
    word = "the"

    # The three programs needed
    histogram(dictList)
    uniqueWords(inputLen)
    frequency(word.lower(), dictList)

    print("--- %s seconds ---" % (time.time() - start_time))
    return render_template('main.html', output=printGen(finishedList))


# Redirects for other pages!
@app.route('/<url>')
def redirect(url):
    return render_template(url+'.html')


if __name__ == "__main__":
    main()
