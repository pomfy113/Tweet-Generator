"""For anything concerning grabbing and cleaning up a file."""
import re


def grab_file():
    """Grab file and splits it all into a list of words."""
    # Please use a relative path if uploading online!
    filename = "theroom.txt"
    # Placing individual words into file_input list
    # file_input = re.findall(r"(?:['\-\w]{2,}|[Ia])", open(filename).read())
    # Test string and the print for it; use if you want to have a raw string
    # testfilename = "egg fish fish Jimmy EGG FISH. jImMy egg-jimmy eg'g Mr. egg"
    # testfilename = "one fish two fish red fish blue cake fish blue"
    # file_input = testfilename.split()
    file_open = open(filename, encoding='utf8').read()

    file_input = room_service(file_open)

    histofile = open("theroomcleanedup.txt", "w+")
    histofile.write(' '.join(file_input[0]))
    histofile.close()
    # file_input = clean_up(file_input)
    return file_input

# def clean_up(filename):
#     """Cleans up the file. Very regex heavy."""
#
#     # Casing: for now, checks after punctuations, beginning of newlines, quotes,
#     # Makes those non-capitalized
#     casing = re.sub(r"(?:[\.?!\s] (\w*)|\"(\w*)|\n(\w*)|^(\w*))", lambda s: s.group(0).lower(), filename)
#
#     # find function; puts it all into a list
#     return re.findall(r"(?:['\-\w]{2,}|[Ia])", casing)

def room_service(filename):
    """Cleans 'The Room' script."""
    start_text = []
    # removes all actions
    actions_removed = re.sub(r"( \(.*\))", '', filename)
    # remove weird [bla] stuff
    audibility = re.sub(r"(?:\[inaudible\]|\[incomprehensible\])", '', actions_removed)
    # create stop tokens
    stop_tokens = re.sub(r"(\.|\!|\?)", ' [STOP]', audibility)
    # only puts in dialogue
    dialogue = re.findall(r"(?:\: (.*))", stop_tokens)
    for strings in dialogue:
        start_text.extend(re.findall(r"^[\w\-']+", strings))
        start_text.extend(re.findall(r"[\.!?\"] ([\w\-']+)", strings))
    # asing = re.sub(r"(?:[)\.?!\s] (\w*)|\n(\w*)|^(\w*))", lambda s: s.group(0).lower(), ' '.join(dialogue))
    regular_text = re.findall(r"[\[\]'\-\w\,]+", ' '.join(dialogue).lower())
    print(regular_text)

    # print(start_text)
    # print(start_text)
    return(regular_text, start_text)

def capitalize_check(text):
    capitalize_input = "capitalize-room.txt"
    capitalize_these = open(capitalize_input).read().split("\n")
    for value, word in enumerate(text):
        if word in capitalize_these:
            text[value] = word.capitalize()
    return text

grab_file()
