"""All the extra functions."""


def histogram(input_histo):
    """Print out a sorted histogram into a file."""
    histofile = open("histogram.txt", "w+")
    for value, key in sorted(input_histo.items(), key=lambda s: s[1], reverse=True):
        histofile.write("%s, %s \n" % (value, key))
    histofile.close()


# What's passed in is the size of the list with unique words
def unique_words(input_histo):
    """Print amount of unique words."""
    unique_words = 0
    for word in input_histo:
        if input_histo[word] == 1:
            unique_words += 1
    return input_histo


# Prints whatever the word's frequency is
def frequency(input_histo, word):
    """Print out a certain word's occurence rate."""
    print_string = "The word '{}' shows up {} times."
    if word in input_histo:
        print(print_string.format(word, input_histo[word]))
    else:
        print("The word",  "'"+word+"'", "does not show up!")
    return input_histo.count(word)
