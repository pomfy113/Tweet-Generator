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
    actions_removed = re.sub(r"(\(.*\))", '', filename)
    dialogue = re.findall(r"(?:\: (.*))", actions_removed)
    # asing = re.sub(r"(?:[)\.?!\s] (\w*)|\n(\w*)|^(\w*))", lambda s: s.group(0).lower(), ' '.join(dialogue))
    cleaned_text = re.findall(r"['\-\w]+", ' '.join(dialogue).lower())
    return(capitalize_check(cleaned_text))

def capitalize_check(text):
    capitalize_input = "capitalize-room.txt"
    capitalize_these = open(capitalize_input).read().split("\n")
    for value, word in enumerate(text):
        if word in capitalize_these:
            text[value] = word.capitalize()
    print(text)
    return text

grab_file()
