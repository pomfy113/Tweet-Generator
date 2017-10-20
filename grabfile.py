"""For anything concerning grabbing and cleaning up a file."""
import re
from pathlib import Path


def grab_file():
    """Grab file and splits it all into a list of words."""
    # Please use a relative path if uploading online!
    pregen_histofile = Path("theroomcleanedup.txt")
    if pregen_histofile.is_file():
        print("It's already here!")
        file_open = open(pregen_histofile, encoding='utf8').read()
        file_input = file_open.split(" ")
    else:
        filename = "theroom.txt"
        # Placing individual words into file_input list

        file_open = open(filename, encoding='utf8').read()

        file_input = room_service(file_open)

        histofile = open("theroomcleanedup.txt", "w+")
        histofile.write(' '.join(file_input))
        histofile.close()

    return file_input

def room_service(filename):

    """Cleans 'The Room' script."""
    # removes all actions
    actions_removed = re.sub(r"( \(.*\))", '', filename)
    # remove weird [bla] stuff
    audibility = re.sub(r"(?:\[inaudible\]|\[incomprehensible\])", '', actions_removed)
    # create stop tokens
    stop_tokens_double = re.sub(r"(\?\!)", ' [stop-qe] [start]', audibility)
    stop_tokens_period = re.sub(r"(\.)", ' [stop-p] [start]', stop_tokens_double)
    stop_tokens_excla = re.sub(r"(\!)", ' [stop-e] [start]', stop_tokens_period)
    stop_tokens_quest = re.sub(r"(\?)", ' [stop-q] [start]', stop_tokens_excla)
    # only puts in dialogue
    dialogue = re.findall(r"(?:\: (.*))", stop_tokens_quest)
    regular_text = re.findall(r"[\[\]'\-\w\,]+", ' '.join(dialogue).lower())
    regular_text.insert(0, '[start]')

    return(regular_text)


def capitalize_check(text):
    capitalize_input = "capitalize-room.txt"
    capitalize_these = open(capitalize_input).read().split("\n")
    for value, word in enumerate(text):
        if word in capitalize_these:
            text[value] = word.capitalize()
    return text
