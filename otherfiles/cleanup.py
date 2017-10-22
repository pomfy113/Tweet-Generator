"""Making a list or dictionary."""
import re
import time


def get_dictionary(file_input):
    """Make dictionary based on word and occurences."""
    # List of things I want to capitalize
    capitalize_these = ('i')
    occurence_dict = {}
    # Removes any non alphanumeric + turns word into lowercase
    # Dictionary is {'word; amount of occurences'}
    for word in file_input:
        if word in capitalize_these:
            word = word.capitalize()
        if word in occurence_dict:
            occurence_dict[word] += 1
        else:
            occurence_dict[word] = 1

    return occurence_dict
