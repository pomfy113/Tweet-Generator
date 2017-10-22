"""It's a tweet generator thing."""
from flask import Flask, render_template, request, redirect
import random
from grabfile import grab_file
# from cleanup import get_dictionary
from probability import probability_gen
from dictogram import Dictogram
from linkedlist import LinkedList
from hashtable import HashTable
import twitter

app = Flask(__name__)

# Global variables due to issue with caching
# Markov Hash Table + start tokens, preloaded before server call
MARKOV_FULL_TABLE = None
# Start tokens and stop tokens
START_GROUPS = []
STOPTOKEN = ['[stop-p]', '[stop-q]', '[stop-e]', '[stop-qe]', None]
STOPPUNCT = ['.', '?', '!', '?!']


def stop_checker(word):
    """Check for the stop tokens (see global constants)."""
    for value, word in enumerate(STOPTOKEN):
        return STOPPUNCT[value]
    return


def markov_loop(markov_table, window_queue, temp_tweet):
    """Create sentence."""
    # Grabs list of sentence starters, then randomly picks one
    first_set = Dictogram(START_GROUPS)
    first_words = probability_gen(first_set)

    # Clean chosen starter sentence; add to markov window + temporary tweet
    # If stop token, finish; only add things past [start] to tweet
    # EXAMPLE pass-in: ('[start]', 'one', 'fish')
    for i in range(len(first_words)):
        window_queue.append(first_words[i])
        if first_words[i] in STOPTOKEN:
            temp_tweet.append(stop_checker(first_words[i]))
            return
        if i != 0:
            temp_tweet.append(first_words[i])

    # New word using probability generator
    dict_lookup = markov_table.get(window_queue.items())
    new_word = probability_gen(dict_lookup)

    # While it's not a stop token, let's keep generating words!
    while new_word not in STOPTOKEN:
        window_queue.append(new_word)
        window_queue.move()
        # Add to temporary tweet
        temp_tweet.append(new_word)
        # New word using probability generator
        dict_lookup = markov_table.get(window_queue.items())
        new_word = probability_gen(dict_lookup)

    # Check to see what punctuation we ended with.
    temp_tweet.append(stop_checker(new_word))
    return


def table_generator(corpus_text, order):
    """Make the actual markov table."""
    """It's a hashtable with tuples, list => tuples, dictionary."""
    # Corpus in linkedlist form
    corpus_ll = LinkedList(corpus_text)
    # Window and the table
    window_queue = LinkedList()
    current_table = HashTable()

    # Current window for iterating through corpus; order changes size
    for i in range(order):
        window_queue.append(corpus_text[i])

    # Add above to hashtable + the word that comes after
    current_table.set((window_queue.items()), [corpus_text[order+1]])

    # For the rest
    for i in range(corpus_ll.length() - (order+1)):
        # Dequeue window, add next to window;
        window_queue.move()
        window_queue.append(corpus_text[i + order])
        # Word after window
        next_word = corpus_text[i + order + 1]
        # Check if window exists in hash table already
        # Add tuple + new word to list, or tuple and list w/ new word
        if current_table.contains((window_queue.items())):
            currentvalues = current_table.get(window_queue.items())
            currentvalues.append(next_word)
            new_value = currentvalues
            current_table.set((window_queue.items()), new_value)
        else:
            current_table.set((window_queue.items()), [next_word])

    # Turn the second element (list) into a dictionary
    for key, value in current_table.items():
        current_table.set(key, Dictogram(value))

    return current_table


def start_token_gen():
    """Generate start groups."""
    start_words = []
    for tuple in (MARKOV_FULL_TABLE.keys()):
        if (tuple[0] == '[start]'):
            start_words.append(tuple)
    return start_words


@app.before_first_request
def main():
    """Start process + Initial resource loader."""
    global MARKOV_FULL_TABLE
    global START_GROUPS
    corpus_text = grab_file()
    # What nth order? How big do I want the window to be?
    order = 2

    MARKOV_FULL_TABLE = table_generator(corpus_text, order)
    START_GROUPS = start_token_gen()


@app.route('/')
def tweetthis():
    """Generate a sentence. Preloaded."""
    # This is from the initial load
    global MARKOV_FULL_TABLE
    markov_walked = MARKOV_FULL_TABLE

    # Initializing the Markov Window and the tweet that we'll checks
    # Currently we check the size
    window_queue = LinkedList()
    temp_tweet = LinkedList()
    last_tweet = ""
    # Let's get a 25% chance of stopping a tweet immediately
    RNG = 4
    # Loop for markov
    """WARNING, the loop only works with The room_tweet."""
    """If you want to change it, change the temp_tweet.room_tweet()"""
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

    print("Final tweet:", last_tweet)

    return render_template('main.html', output=last_tweet)


@app.route('/about')
def about():
    """Redirects for other pages."""
    return render_template('about.html')


@app.route('/tweet', methods=['POST'])
def tweet():
    """Tweet sentence to twitter."""
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')


if __name__ == "__main__":
    main()
