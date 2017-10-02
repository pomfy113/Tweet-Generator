"""Print stuff."""


def sentence_print(finished_list):
    """Print a sentence."""
    # capitalize_these = ['i']
    # for value, word in enumerate(finished_list):
    #     if (word in capitalize_these) or (value == 0):
    #         finished_list[value] = word.capitalize()
    finished_list[0] = finished_list[0].capitalize()
    final_sentence = ' '.join(finished_list)
    return(final_sentence + ".")


def word_print(finished_word):
    """Print the word."""
    return (finished_word)
