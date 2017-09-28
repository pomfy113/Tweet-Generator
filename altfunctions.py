"""All the extra functions."""


def histogram(occurence_dict):
    """Print out a sorted histogram into a file."""
    histofile = open("histogram.txt", "w+")
    for value, key in sorted(occurence_dict.items(), key=lambda s: s[1], reverse=True):
        histofile.write("%s, %s \n" % (value, key))
    histofile.close()


# What's passed in is the size of the list with unique words
def unique_words(occurence_dict):
    """Print amount of unique words."""
    unique_words = 0
    for word in occurence_dict:
        if occurence_dict[word] == 1:
            unique_words += 1
    print("There are", unique_words, "unique words.")


# Prints whatever the word's frequency is
def frequency(word, occurence_dict):
    """Print out a certain word's occurence rate."""
    print_string = "The word '{}' shows up {} times."
    if word in occurence_dict:
        print(print_string.format(word, occurence_dict[word]))
    else:
        print("The word",  "'"+word+"'", "does not show up!")
