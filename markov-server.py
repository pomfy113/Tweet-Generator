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
from werkzeug.contrib.cache import SimpleCache


markov_full_table = None
app = Flask(__name__)

def stop_checker(stopstring):
    """This just checks for the stop tokens."""
    if stopstring == '[stop-p]':
        return '.'
    elif stopstring == '[stop-q]':
        return '?'
    elif stopstring == '[stop-e]':
        return '!'
    elif stopstring == '[stop-eq]':
        return '?!'
    elif stopstring is None:
        return '.'
    return

def markov_loop(markov_table, window_queue, temp_tweet):
    """Let's get that loop started."""
    # Beginning with start keys
    start_keys = []
    for first, second in (markov_table.keys()):
        if (first == '[start]'):
            start_keys.append((first, second))

    # Create dictogram of start tokens, then randomly generates one
    first_set = Dictogram(start_keys)
    first_words = probability_gen(first_set)

    # Window created! And let's put in the first word.
    window_queue.append(first_words[0])
    window_queue.append(first_words[1])
    temp_tweet.append(first_words[1])

    # Pass in function; should return a word (see above function)
    new_word = probability_gen(markov_table.get(window_queue.items()))

    # While it's not a stop token, let's keep generating words!
    while new_word not in {'[stop-p]', '[stop-q]', '[stop-e]', '[stop-eq]', None}:
        # Moving window up
        window_queue.append(new_word)
        window_queue.move()
        # To add to the sentence we'll test
        temp_tweet.append(new_word)
        # New word using probability generator
        new_word = probability_gen(markov_table.get(window_queue.items()))

    # End of the line! No need to return things due to linked list!
    temp_tweet.append(stop_checker(new_word))
    return

def room_capitalize(text):
    """Capitalize text as needed based on input."""
    capitalize_input = "capitalize-room.txt"
    capitalize_these = open(capitalize_input).read().split("\n")
    text = text.split(" ")
    for value, word in enumerate(text):
        if word in capitalize_these:
            text[value] = word.capitalize()
    return ' '.join(text)

def markov_generator(corpus_text):
    """Make the actual markov table."""
    """It's a hashtable with tuples, followed by a list=>dictionary."""

    # Here's my corpus in LL form
    corpus_ll = LinkedList(corpus_text)
    # Here's the window and the table
    window_queue = LinkedList()
    current_table = HashTable()

    # Currently second order. WIP for making it more.
    # Current window for iterating through corpus
    window_queue.append(corpus_text[0])
    window_queue.append(corpus_text[1])
    current_table.set((window_queue.items()), [corpus_text[2]])

    # Now the loop for the rest
    for i in range(corpus_ll.length()-3):
        # For dequeue -> queue
        window_queue.move()
        window_queue.append(corpus_text[i+2])
        # Word after for placing into dictionary
        next_word = corpus_text[i+3]
        # If it's already in, add the word to the list
        if current_table.contains((window_queue.items())):
            # New word stuff to add onto the table
            currentvalues = current_table.get(window_queue.items())
            currentvalues.append(next_word)
            new_value = currentvalues

            current_table.set((window_queue.items()), new_value)
        else:
            # If it's not, we got a new set
            current_table.set((window_queue.items()), [next_word])

    # Turn the second element (list) into a dictogram
    for key, value in current_table.items():
        current_table.set(key, Dictogram(value))

    return current_table


@app.before_first_request
def main():
    """Start main process."""
    # This is for the initial load
    global markov_full_table
    corpus_text = grab_file()

    markov_full_table = markov_generator(corpus_text)


@app.route('/')
def tweetthis():
    """Generate a sentence. Preloaded."""
    # This is from the initial load
    global markov_full_table
    markov_walked = markov_full_table

    # Initializing the Markov Window and the tweet that we'll checks
    # Currently we check the size
    window_queue = LinkedList()
    temp_tweet = LinkedList()
    last_tweet = ""
    # Let's get a 25% chance of stopping a tweet immediately
    RNG = 4

    while(len(last_tweet) < 60) and (RNG != 0):
        # Here's the markov!
        markov_loop(markov_walked, window_queue, temp_tweet)
        # If good length, add to main tweet!
        if temp_tweet.string_length() + len(last_tweet) <= 120:
            last_tweet += temp_tweet.room_tweet() + " "
        # Otherwise, throw it away
        window_queue.empty_list()
        temp_tweet.empty_list()
        # Roll that dice!
        RNG = random.randint(0, 4)
        print(RNG)
    print("Final tweet:", last_tweet)

    return render_template('main.html', output=last_tweet)



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

    # print(input_histo.tokens)
    # return render_template('main.html', output=tweet, time=time.time())

@app.route('/')

@app.route('/about')
def about():
    """Redirects for other pages."""
    return render_template('about.html')

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')

if __name__ == "__main__":
    main()
