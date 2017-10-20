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
import twitter


app = Flask(__name__)


def stop_checker(stopstring, final_list):
    """This just checks for the stop tokens."""
    if stopstring == '[stop-p]':
        final_list.append('.')
    elif stopstring == '[stop-q]':
        final_list.append('?')
    elif stopstring == '[stop-e]':
        final_list.append('!')
    elif stopstring == None:
        final_list.append('.')
    return


def markov_starter(start_token_list, joined_input, final_list, word_linkedlist):
        """Start off the markov sentence."""
        # Just in case.
        infinite_stopper = 4
        # START tokens. Start off with a single word.
        start_token_histo = Dictogram(start_token_list)
        first_word = probability_gen(start_token_histo).lower()
        word_linkedlist.append(first_word)
        final_list.append(first_word)

        # Checking for the second word.
        new_list = Dictogram(re.findall(r'\[stop-\w\] %s ([\[\]\w\'\:\-\,]*)' % str(first_word), joined_input))
        second_word = probability_gen(new_list)

        # For checking one word sentences.
        while second_word in {'[stop-p]', '[stop-q]', '[stop-e]', None}:
            if infinite_stopper <= 0 or second_word is None:
                stop_checker(second_word, final_list)
                word_linkedlist.empty_list()
                return ' '.join(word_linkedlist.items())
            second_word = probability_gen(new_list)
            infinite_stopper -= 1

        # Append to window and the ongoing sentence.
        word_linkedlist.append(second_word)
        final_list.append(second_word)

        return ' '.join(word_linkedlist.items())

# TO-DO: Rename variables
def markov_loop(file_input, final_list, loops, word_linkedlist):
    """Markov maker; recursive, based on variable 'loop'."""
    """This is going to be a doozy, so keep a close eye on those comments."""
    if final_list.string_length() > 180:
        print("A bit too long!")
        return word_linkedlist
    # Return once we're out of loops
    if loops is False:
        return word_linkedlist

    # Combine window before passing it into regex findall
    word = ' '.join(word_linkedlist.items())
    pattern = r' %s ([\[\]\w\'\:\-\,]*)' % str(word)
    following_words = re.findall(pattern, file_input)
    new_list = Dictogram(following_words)
    new_word = probability_gen(new_list)

    # if stop token, then do the stop-check to punctuate properly
    if new_word in {'[stop-p]', '[stop-q]', '[stop-e]', None}:
        print("STOPPING")
        stop_checker(new_word, final_list)
        loops = False
        return word_linkedlist

    # Add to window and ongoing list
    word_linkedlist.append(new_word)
    final_list.append(new_word)

    # Dequeue, then next!
    word_linkedlist.move()
    markov_loop(file_input, final_list, loops, word_linkedlist)

    return word_linkedlist

def room_capitalize(text):
    """Capitalize text as needed based on input."""
    capitalize_input = "capitalize-room.txt"
    capitalize_these = open(capitalize_input).read().split("\n")
    for value, word in enumerate(text):
        if word in capitalize_these:
            text[value] = word.capitalize()
    return text

def markov_generator(corpus_text):
    corpus_text = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'fish', 'two', 'fish']
    corpus_ll = LinkedList(corpus_text)
    window_queue = LinkedList()
    current_dict = Dictogram()

    window_queue.append(corpus_text[0])
    window_queue.append(corpus_text[1])
    current_dict.update([window_queue.items()])
    current_dict[window_queue.items()] = Dictogram()
    current_dict[window_queue.items()].update([corpus_text[2]])


    for i in range(corpus_ll.length()):
        window_queue.move()
        window_queue.append(corpus_text[i+3])

        if window_queue.items() not in current_dict:
            current_dict.update([window_queue.items()])
        current_dict[window_queue.items()] = Dictogram()
        print("Current next word:", corpus_text[i+4])

        # if current_dict[window_queue.items()].count(corpus_text[i+4]) != 0:
        #     print("Already in!")
        #     current_dict[window_queue.items()][corpus_text[i+4]] += 1
        # else:
        current_dict[window_queue.items()].update('fish')
        # if current_dict[window_queue.items()].count(corpus_text[i+4])

        print("New dictionary:", current_dict[window_queue.items()])
        # print(current_dict[window_queue.items()][corpus_text[i+4]])

        print(window_queue.items(), "\n", current_dict, "\n===================")




    print(current_dict)


    # for i in range(len(current_markov)):






# @app.route('/')
def main():
    """Start main process."""
    start_time = time.time()
    corpus_text = grab_file()

    final_list = LinkedList()
    tweet = ""

    markov_generator(corpus_text)

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
