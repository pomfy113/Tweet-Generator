import random
import string

# What's being passed in
# "filename" for passing in a file; change if you have a different filename
# Otherwise, use testfilename to pass in your own string
# filename = "/Users/fcruz/Documents/GitHub/Tweet-Maker/grimm.txt"
testfilename = "egg fish egg fish James James James James egg egg egg EGG FISH. egg jAmEs"

# Comment below is from switching to a file to the string above
# Change as needed
# dictionary = open(filename).read().split()
dictionary = testfilename.split()

# Lists and variables for later
# tempList is a list of lists; each list has the unique word + occurences
# alreadyplaced has words that have showed up at least once
# currentWord is the index of the current word on either list
templist = []
alreadyplaced = []
currentWord = 0

# loops through length of passed in strings
# also makes sure to filter out non-alphanumerics and changes it to lowercase
for i in range(len(dictionary)):
    dictionary[i] = filter(str.isalnum, dictionary[i].lower())
    # if the current word has already been seen,
    # find its index; add 1 to how many times the word shows up
    if dictionary[i] in alreadyplaced:
        currentWord = alreadyplaced.index(dictionary[i])
        templist[currentWord] = [templist[currentWord][0], templist[currentWord][1]+1]
    # if it's the first time, then it showed up once!
    # add that to both lists; templist will say it showed up once
    # alreadyplaced says that it has shown up before
    else:
        templist.append((dictionary[i], 1))
        alreadyplaced.append(dictionary[i])
# prints out each word and its occurences, without all the fuss
for j in range(len(templist)):
    print templist[j][0] + " " + str(templist[j][1])
