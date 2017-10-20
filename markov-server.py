"""It's a tweet generator thing."""
import time
from flask import Flask, render_template, request, redirect
import re
import random
from grabfile import grab_file
# from cleanup import get_dictionary
from probability import probability_gen
from listogram import Listogram
from dictogram import Dictogram
from linkedlist import LinkedList
from hashtable import HashTable
import twitter
import pickle
from pathlib import Path




app = Flask(__name__)


def stop_checker(stopstring):
    """This just checks for the stop tokens."""
    if stopstring == '[stop-p]':
        return '.'
    elif stopstring == '[stop-q]':
        return '?'
    elif stopstring == '[stop-e]':
        return '!'
    elif stopstring is None:
        return '.'
    return


def markov_starter(markov_table, window_queue):
        """Start off the markov sentence."""
        start_keys = []
        for first, second in (markov_table.keys()):
            if (first == '[start]') and (second not in {'[stop-p]', '[stop-q]', '[stop-e]', None}):
                start_keys.append((first, second))
        first_set = Dictogram(start_keys)
        first_words = probability_gen(first_set)

        window_queue.append(first_words[0])
        window_queue.append(first_words[1])

        new_word = probability_gen(markov_table.get(window_queue.items()))

        window_queue.append(new_word)
        window_queue.move()

        return
        # Just in case.


# TO-DO: Rename variables
def markov_loop(markov_table, window_queue):
    """Markov maker!"""
    final_list = window_queue.stringify()
    new_word = probability_gen(markov_table.get(window_queue.items()))

    while new_word not in {'[stop-p]', '[stop-q]', '[stop-e]', None}:
        window_queue.append(new_word)
        final_list += " " + new_word
        window_queue.move()
        new_word = probability_gen(markov_table.get(window_queue.items()))

    final_list += stop_checker(new_word)
    print(final_list)

def room_capitalize(text):
    """Capitalize text as needed based on input."""
    capitalize_input = "capitalize-room.txt"
    capitalize_these = open(capitalize_input).read().split("\n")
    for value, word in enumerate(text):
        if word in capitalize_these:
            text[value] = word.capitalize()
    return text

def markov_generator(corpus_text, start_time):
    corpus_ll = LinkedList(corpus_text)
<<<<<<< HEAD

    window_queue = LinkedList()
    current_table = {}

    window_queue.append(corpus_text[0])
    window_queue.append(corpus_text[1])
    current_table[(window_queue.items())] = corpus_text[2]


    print("--- %s seconds --- pre dict \n\n\n" % (time.time() - start_time))

    for i in range(corpus_ll.length()-3):
        window_queue.move()
        window_queue.append(corpus_text[i+2])
        next_word = corpus_text[i+3]

        if window_queue.items() in current_table:
            current_table[(window_queue.items())][(next_word)] += 1
        else:
            current_table[(window_queue.items())] = (next_word, 1)
        print(current_table)
    print("--- %s seconds --- post dict \n\n\n" % (time.time() - start_time))

    for key, value in current_table:
        current_table(key, Dictogram(value))

    print("--- %s seconds --- Dictogram set \n\n\n" % (time.time() - start_time))
=======

    window_queue = LinkedList()
    current_table = HashTable()

    window_queue.append(corpus_text[0])
    window_queue.append(corpus_text[1])
    current_table.set((window_queue.items()), [corpus_text[2]])

    print("--- %s seconds --- pre dict \n\n\n" % (time.time() - start_time))

    for i in range(corpus_ll.length()-3):
        window_queue.move()
        window_queue.append(corpus_text[i+2])
        next_word = corpus_text[i+3]

        if current_table.contains((window_queue.items())):
            currentvalues = current_table.get(window_queue.items())
            currentvalues.append(next_word)
            new_value = currentvalues

            current_table.set((window_queue.items()), new_value)
        else:
            current_table.set((window_queue.items()), [next_word])

    print("--- %s seconds --- post dict \n\n\n" % (time.time() - start_time))

    for key, value in current_table.items():
        current_table.set(key, Dictogram(value))

    print("--- %s seconds --- Dictogram set \n\n\n" % (time.time() - start_time))

>>>>>>> parent of 9577f4b... blabla pickles

    return current_table





# @app.route('/')
def main():
    """Start main process."""
    start_time = time.time()
    corpus_text = grab_file()

    window_queue = LinkedList()
    final_list = LinkedList()
    tweet = ""

    print("--- %s seconds --- pre-walk \n\n\n" % (time.time() - start_time))

<<<<<<< HEAD
    # if markov_pickle.is_file():
    #     with open('markov.pickle', 'rb') as f:
    #         markov_walked = pickle.load(f)
    # else:
    markov_walked = markov_generator(corpus_text, start_time)
    #     sys.setrecursionlimit(2000)
    #     with open('markov.pickle', 'wb') as f:
    #         pickle.dump(markov_walked, f)

=======
>>>>>>> parent of 9577f4b... blabla pickles

    # with open('markov.pickle', 'w') as f:
    markov_walked = markov_generator(corpus_text, start_time)
    print("--- %s seconds --- markov walk \n\n\n" % (time.time() - start_time))

    markov_starter(markov_walked, window_queue)
    print("--- %s seconds --- markov starter \n\n\n" % (time.time() - start_time))

    markov_loop(markov_walked, window_queue)
    print("--- %s seconds --- markov done \n\n\n" % (time.time() - start_time))



    # loops = 20
    #
    # randomnumber = 4
    # while len(tweet) <= 100:
    #     markov_starter(start_token_list, joined_input, final_list, word_linkedlist)
    #     if word_linkedlist.items():
    #         markov_loop(joined_input, final_list, loops, word_linkedlist)
    #
    #     if len(tweet) + final_list.string_length() < 180:
    #         tweet += final_list.room_tweet()
    #     if len(tweet) < 100:
    #         tweet += " "
    #     word_linkedlist.empty_list()
    #     final_list.empty_list()
    #     if random.randint(1, randomnumber) is 1:
    #         break
    # print(tweet)


    """Below are the three alternate functions not needed for the tweetgen."""
    # Word you want to search up for frequency; change as needed
    # word = "the"

    # input_histo = Dictogram(file_input[0])
    # histogram(input_histo)
    # unique words... was replaced by dictogram
    # unique_words(input_histo.tokens)
    # input_histo.tokens
    # word frequency... also replaced
    # input_histo.count(word)

    print("--- %s seconds --- end total \n\n\n" % (time.time() - start_time))
    # print(input_histo.tokens)
    # return render_template('main.html', output=tweet, time=time.time())


# @app.route('/about')
def about():
    """Redirects for other pages."""
    return render_template('about.html')

# @app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')

if __name__ == "__main__":
    main()
