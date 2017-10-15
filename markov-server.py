"""It's a tweet generator thing."""
import time
from flask import Flask, render_template, request
import re
from grabfile import grab_file, capitalize_check
# from cleanup import get_dictionary
from probability import probability_gen
from printer import sentence_print, word_print
from altfunctions import histogram
from dictogram import Dictogram
from listogram import Listogram
from linkedlist import LinkedList

app = Flask(__name__)


def markov_loop(file_input, final_list, word, loops, word_linkedlist):
    """Markov maker; recursive, based on variable 'loop'."""
    """This is going to be a doozy, so keep a close eye on those comments."""

    # For testing purposes
    print("Linkedlist:", word_linkedlist)
    # Return once we're out of loops
    if loops == 0:
        return word_linkedlist
    # Combine
    word = ' '.join(word_linkedlist.items())
    print("Word being passed in:", word)
    new_list = Dictogram(re.findall(r' %s ([\[\]\w\'-\,]*)' % str(word), file_input))
    print(new_list)
    if not new_list:
        return word_linkedlist
    new_word = probability_gen(new_list)

    if new_word == "[stop]":
        print("STOPPING")
        final_list.append('.')
        loops = 0
        return word_linkedlist

    word_linkedlist.append(new_word)
    final_list.append(new_word)

    word_linkedlist.move()
    markov_loop(file_input, final_list, new_word, loops-1, word_linkedlist)

    return word_linkedlist


# @app.route('/')
def main():
    """Start main process."""
    start_time = time.time()
    file_input = grab_file()
    word_linkedlist = LinkedList()
    joined_input = ' '.join(file_input[0])
    final_list = LinkedList()



    # Grabs how long you want string to be for later; defaults to 10
    # output_len = request.args.get('num', '')
    # if output_len == '':
    loops = 10
    # else:
    #     loops = int(output_len)

    # START tokens.
    start_token_histo = Dictogram(file_input[1])
    first_word = probability_gen(start_token_histo).lower()
    word_linkedlist.append(first_word)
    final_list.append(first_word)
    # Checking for the second word.

    new_list = Dictogram(re.findall(r' %s ([\[\]\w\'-\,]*)' % str(first_word), joined_input))
    print("Second word's dictogram:", first_word, new_list)
    while not bool(new_list):
        new_list = Dictogram(file_input[0])
    second_word = probability_gen(new_list)
    word_linkedlist.append(second_word)
    final_list.append(second_word)


    print("Current linked list:", word_linkedlist)
    first_words = ' '.join(word_linkedlist.items())

    # Markov begins; prints based probability of adjacent words
    # loops - 1 because already did a word

    # input histogram for junk

    markov_loop(joined_input, final_list, first_words, loops-1, word_linkedlist)
    final_list2 = capitalize_check(final_list.items())
    print((' '.join(final_list2)).replace(" .", "."))


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
    # return render_template('main.html', output=sentence_print(finished_list))


@app.route('/<url>')
def redirect(url):
    """Redirects for other pages."""
    return render_template(url+'.html')


if __name__ == "__main__":
    main()
