import random
import string
import numpy
import re
import time

start_time = time.time()

# What's being passed in
# "filename" for passing in a file; change if you have a different filename
# Otherwise, use testfilename to pass in your own string
filename = "/Users/fcruz/Documents/GitHub/Tweet-Maker/grimm.txt"
# filename = "egg fish egg fish James James James James egg egg egg EGG FISH. egg jAmEs"
# testfilename = "egg egg egg egg egg egg egg egg egg egg fish"

# Comment below is from switching to a file to the string above
# Change as needed
dictionary = open(filename).read().split()
# dictionary = filename.split()

# Lists and variables for later
# dictlist is a list of lists; each list has the unique word + occurences
# alreadyplaced has words that have showed up at least once
# currentWord is the index of the current word on either list
dictlist = []
probability = []

totalwords = len(dictionary)
currentWord = 0

# loops through length of passed in strings
# also makes sure to filter out non-alphanumerics and changes it to lowercase
for i in range(len(dictionary)):
    dictionary[i] = re.sub('[^0-9a-zA-Z]+', '', dictionary[i]).lower()

    if dictionary[i] in [item[0] for item in dictlist]:
        currentWord = [item[0] for item in dictlist].index(dictionary[i])
        dictlist[currentWord] = [dictlist[currentWord][0], dictlist[currentWord][1]+1]
    # if it's the first time, then it showed up once!
    # add that to both lists; dictlist will say it showed up once
    # alreadyplaced says that it has shown up before
    else:
        dictlist.append([dictionary[i], 1])
# prints out each word and its occurences, without all the fuss

# probability equation for each word
for k in range(len(dictlist)):
    #print dictlist[k][0]
    probability.append(float(dictlist[k][1])/totalwords)

# printing out the words based on probability
# re.sub removes all non-space and alphanumeric
# numpy.random.choice prints out the words based on a probability
# for probability chances, please see/print out the probability list!
probabilityList = re.sub('[^0-9a-zA-Z ]+', '', str(numpy.random.choice([item[0] for item in dictlist], 10, p=probability)))
print (probabilityList.capitalize() + ".")
print("--- %s seconds ---" % (time.time() - start_time))
