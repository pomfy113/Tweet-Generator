"""Deals with making probabilities."""
import random
import time

def probability_gen(occurence_dict, input_len, word_amt):
    """Generate a word/sentence based on probability and weights."""
    finished_list = []
    random_num = random.random()
    accumulator = 0.0
    # Go through dictionary; keep adding its weight to accumulator
    # When accumulator hits over the random number, append to list
    for i in range(word_amt):
        for key, value in occurence_dict.items():
            accumulator += float(value/input_len)
            if accumulator >= random_num:
                random_num = random.random()
                accumulator = 0.0
                if i != 0:
                    finished_list.append(key)
                    break
                else:
                    finished_list.append(key.capitalize())
                    break
    return finished_list
