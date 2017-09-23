import random, sys

def randomizer():
    return random.randint(0, len(dictionary) - 1)

if __name__ == "__main__":
    dictionary = sys.argv[1:]
    scramble = dictionary[:]

    for _ in range(len(dictionary)):
        first = randomizer()
        second = randomizer()
        scramble[first],scramble[second] = scramble[second],scramble[first]

    print(" ".join(scramble) + '.')
