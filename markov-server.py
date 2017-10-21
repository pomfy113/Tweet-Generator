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

# Markov Hash Table + start tokens, preloaded before server call
MARKOV_FULL_TABLE = None
# Start tokens and stop tokens
START_TOKENS = []
STOPTOKEN = ['[stop-p]', '[stop-q]', '[stop-e]', '[stop-qe]', None]
STOPPUNCT = ['.', '?', '!', '?!']

def stop_checker(word):
    """Check for the stop tokens."""
    for value, word in enumerate(STOPTOKEN):
        return STOPPUNCT[value]
    return

def markov_loop(markov_table, window_queue, temp_tweet):
    """Let's get that loop started."""
    # Create dictogram of start tokens, then randomly generates one
    first_set = Dictogram(START_TOKENS)
    first_words = probability_gen(first_set)

    # Window created! And let's put in the first word.
    window_queue.append(first_words[0])
    window_queue.append(first_words[1])
    temp_tweet.append(first_words[1])

    # Pass in function; should return a word (see above function)
    dict_lookup = markov_table.get(window_queue.items())
    new_word = probability_gen(dict_lookup)

    # While it's not a stop token, let's keep generating words!
    while new_word not in STOPTOKEN:
        # Moving window up
        window_queue.append(new_word)
        window_queue.move()
        # To add to the sentence we'll test
        temp_tweet.append(new_word)
        # New word using probability generator
        dict_lookup = markov_table.get(window_queue.items())
        new_word = probability_gen(dict_lookup)

    # End of the line! No need to return things due to linked list!
    temp_tweet.append(stop_checker(new_word))
    return


def table_generator(corpus_text):
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

def start_token_gen():
    start_tokens = []
    for first, second in (MARKOV_FULL_TABLE.keys()):
        if (first == '[start]'):
            start_tokens.append((first, second))
    return start_tokens

@app.before_first_request
def main():
    """Start main process."""
    # This is for the initial load
    global MARKOV_FULL_TABLE
    global START_TOKENS
    corpus_text = grab_file()

    MARKOV_FULL_TABLE = table_generator(corpus_text)
    START_TOKENS = start_token_gen()

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
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')

if __name__ == "__main__":
    main()
