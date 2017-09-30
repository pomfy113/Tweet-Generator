### Answers
**What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?**
- The application returns a set of randomly generated word(s) based on how often they show up from the source file. Though not its main functionality, it can also see how often a specific word shows up in a body of text, how many unique words there are, and print out a list of words and their occurrences.
- Each file is a module! It's separated into:
    - `server.py` - the main file, it runs!
    - `grabfile.py` - grabs a list of words from a body of text
    - `dictogram.py` - handles turning something into a dictionary.
        - While `cleanup.py` is much faster, dictogram is cleaner (harhar) and allows for extra functionality.
    - `probability.py` - handles all the percentage handling. WIP, but I hope to change this to a class and separate things away, but it works fine as is right now.
    - `printer.py` - It prints!
    - `altfunctions.py` - The alternate functionalities:
        - Creating a list of words+occurrences and makes a text file for it.
        - Checks how many unique words there are.
            - No longer needed due to dictogram
        - Prints out how many times a specific word shows up.
            - No longer needed due to dictogram


**Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?**
- Mostly. I think. I'm mostly sure.

**What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?**
- No globals, and each variable stays only where they're needed.

**Are the functions small and clearly specified, with as few side effects as possible?**
- Each thing mostly does one thing, so I'm mostly sure, yes. I can likely separate `probability.py` to something that changes things into probability, and one to use that probability to put things in, but they're there's no functionality reason I know of *right now*.

**Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?**
- Likely the extra methods, maybe? It's just additional methods that have already been solved by the dictogram class.

**Can files be used as both modules and as scripts?
Do modules all depend on each other or can they be used independently?**
- Pretty sure. All modules should be usable without anything else.
