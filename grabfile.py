"""For anything concerning grabbing and cleaning up a file."""
import re


def grab_file():
    """Grab file and splits it all into a list of words."""
    # Please use a relative path if uploading online!
    filename = "sherlock.txt"
    # Placing individual words into file_input list
    file_input = re.sub("[^\w\-\s]", '', open(filename).read().lower()).split()

    # Test string and the print for it; use if you want to have a raw string
    # testfilename = "egg fish fish Jimmy EGG FISH. jImMy egg-jimmy eg'g"
    # testfilename = "one fish two fish red fish blue cake fish blue"
    # file_input = testfilename.split()

    return file_input
