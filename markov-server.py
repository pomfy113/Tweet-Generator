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

# app = Flask(__name__)


# @app.route('/')
def main():
    """Start main process."""
    start_time = time.time()
    file_input = grab_file()
    # Grabs how long you want string to be for later; defaults to 10
    # output_len = request.args.get('num', '')
    # if output_len == '':
    #     word_amt = 10
    # else:
    #     word_amt = int(output_len)

    # Grab the input, make into dictionary/list of words + occurences
    # Changed into a class for more functionality; trades speed though

    # templist = []
    input_histo = Listogram(file_input)
    print(file_input)
    for word in file_input:

        print(word, ' '.join(file_input))
        cake = Dictogram(re.findall(r'%s (\w+)' % word, ' '.join(file_input)))
        print(word, cake)



    input_len = input_histo.tokens

    # List based on probability
    # Grabs input, length of input, and desired string length
    finished_list = probability_gen(input_histo, input_len)
    # print(sentence_print(finished_list))
    # if word_amt == 1:
    #     word_print(finished_list)
    # else:
    #     sentence_print(finished_list)

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
    # return render_template('main.html', output=sentence_print(finished_list))


# Redirects for other pages!
# @app.route('/<url>')
# def redirect(url):
#     return render_template(url+'.html')


if __name__ == "__main__":
    main()
