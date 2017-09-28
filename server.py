"""It's a tweet generator thing."""
import time
from flask import Flask, render_template, request

from grabfile import grab_file
from cleanup import get_dictionary
from probability import probability_gen
from printer import sentence_print, word_print
from altfunctions import histogram, unique_words, frequency

app = Flask(__name__)


@app.route('/')
def main():
    """Main process."""
    start_time = time.time()
    file_input = grab_file()
    inputLen = len(file_input)

    # Grabs how long you want string to be for later; defaults to 10
    wordAmtInput = request.args.get('num', '')
    if wordAmtInput == '':
        wordAmt = 10
    else:
        wordAmt = int(wordAmtInput)

    # Grab the input, make into dictionary of words + occurences
    occurence_dict = get_dictionary(file_input)

    # List based on probability
    # Grabs input, length of input, and desired string length
    finished_list = probability_gen(occurence_dict, inputLen, wordAmt)

    if wordAmt == 1:
        word_print(finished_list)
    else:
        sentence_print(finished_list)

    """Below are the three alternate functions not needed for the tweetgen."""
    # # Word you want to search up for frequency; change as needed
    # word = "the"

    # # The three programs needed
    # histogram(occurence_dict)
    # unique_words(occurence_dict)
    # frequency(word.lower(), occurence_dict)

    print("--- %s seconds --- end after frequency \n" % (time.time() - start_time))
    return render_template('main.html', output=sentence_print(finished_list))


# Redirects for other pages!
@app.route('/<url>')
def redirect(url):
    return render_template(url+'.html')


if __name__ == "__main__":
    main()
