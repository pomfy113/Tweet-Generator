"""Deals with making probabilities."""
import random

def probability_gen(input_histo):
    """Generate a word/sentence based on probability and weights."""
    # Go through dictionary; keep adding its weight to accumulator
    # When accumulator hits over the random number, append to list
    if isinstance(input_histo, list):
        return(list_prob(input_histo))
    if isinstance(input_histo, dict):
        return(dict_prob(input_histo))


def dict_prob(input_histo):
    """Do this if it's a histogram."""
    random_num = random.random()
    accumulator = 0.0
    for key, value in input_histo.items():
        accumulator += float(value/input_histo.tokens)
        if accumulator >= random_num:
            return key
            break

def list_prob(input_histo):
        random_num = random.random()
        accumulator = 0.0
        finished_list = []
        for key, value in input_histo:
            print("Printing k/v:", key, value)
            accumulator += float(value/input_histo.tokens)
            if accumulator >= random_num:
                return key
                break
