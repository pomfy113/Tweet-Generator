import random

quotes = open("/usr/share/dict/words").read().splitlines()

#def random_python_quote():
rand_index = random.randint(0, len(quotes) - 1)
print quotes[rand_index]
