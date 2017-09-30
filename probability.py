"""Deals with making probabilities."""
import random
import time

def probability_gen(input_histo, input_len):
    """Generate a word/sentence based on probability and weights."""
    # Go through dictionary; keep adding its weight to accumulator
    # When accumulator hits over the random number, append to list
    if isinstance(input_histo, list):
        return(list_prob(input_histo, input_len))
    if isinstance(input_histo, dict):
        return(dict_prob(input_histo, input_len))


def dict_prob(input_histo, input_len):
    """Do this is it's a histogram."""
    random_num = random.random()
    accumulator = 0.0
    finished_list = []
    for key, value in input_histo.items():
        accumulator += float(value/input_len)
        if accumulator >= random_num:
            finished_list.append(key)
            break
    return finished_list


def list_prob(input_histo, input_len):
        random_num = random.random()
        accumulator = 0.0
        finished_list = []
        for key, value in input_histo:
            accumulator += float(value/input_len)
            if accumulator >= random_num:
                finished_list.append(key)
                break
        return finished_list
