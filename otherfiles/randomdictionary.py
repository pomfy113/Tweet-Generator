import random, sys

# Change filename to open a different set of words
dictionary = open("/usr/share/dict/words").read().splitlines()

# Takes number to see how many words
wordAmt = int(sys.argv[1])
wordlist = []

for index in range(wordAmt):
    # randomizer for the index;
    rand_index = random.randint(0, len(dictionary) - 1)
    wordlist.append(dictionary[rand_index])

print(" ".join(wordlist) + '.')

# Rand_index = random.randint(0, len(dictionary) - 1)
