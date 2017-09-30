"""It's a tweet generator thing."""
import time
from flask import Flask, render_template, request
import re
from grabfile import grab_file
# from cleanup import get_dictionary
from probability import probability_gen
from printer import sentence_print, word_print
from altfunctions import histogram
from dictogram import Dictogram
from listogram import Listogram

app = Flask(__name__)

def next_word_loop(file_input, word, loops, final_list):
    """Markov maker; recursive, based on variable 'loop'."""
    if loops == 0:
        return final_list
    word_search = re.sub('[^\w]', '', str(word))
    new_list = Dictogram(re.findall(r'%s (\w*)' % word_search, file_input))
    new_word = probability_gen(new_list)
    final_list.append(new_word)
    next_word_loop(file_input, new_word, loops-1, final_list)

    return final_list

@app.route('/')
def main():
    """Start main process."""
    start_time = time.time()
    file_input = grab_file()
    final_list = []

    # Grabs how long you want string to be for later; defaults to 10
    output_len = request.args.get('num', '')
    if output_len == '':
        loops = 10
    else:
        loops = int(output_len)

    # Grab the input, make into dictionary/list of words + occurences
    # Using probability, grabs first word.
    input_histo = Dictogram(file_input)
    first_word = probability_gen(input_histo)
    final_list.append(first_word)
    loops -= 1

    # Markov begins; prints based probability of adjacent words
    joined_input = ' '.join(file_input)
    finished_list = next_word_loop(joined_input, first_word, loops, final_list)


    print(finished_list)
    print(sentence_print(finished_list))

    """Below are the three alternate functions not needed for the tweetgen."""
    # Word you want to search up for frequency; change as needed
    # word = "the"

    # histogram(input_histo)
    # unique words... was replaced by dictogram
    # unique_words(input_histo.tokens)
    # input_histo.tokens
    # word frequency... also replaced
    # input_histo.count(word)

    print("--- %s seconds --- end after frequency \n" % (time.time() - start_time))
    return render_template('main.html', output=sentence_print(finished_list))


@app.route('/<url>')
def redirect(url):
    """Redirects for other pages!"""
    return render_template(url+'.html')


if __name__ == "__main__":
    main()