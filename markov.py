from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    full_file = open(input_path)
    input_text = full_file.read()

    return input_text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    # Phase one:  create bi-grams as tuples

    # bi_gram = ()
    working_dictionary = {}

    # Take big single string and chop into a list of word strings
    split_text = input_text.split()

    # Limiting our index range up to end minus two. Prevents out of index errors.
    for i in range(len(split_text) - 2):  # currently list of strings aka words

        # Create tuple starting with index 0 and 0 + 1. Save to key variable.
        key = (split_text[i], split_text[i + 1])

        # Check to see if key is already in dictionary. If not, add it with value = empty list.
        if key not in working_dictionary:
            working_dictionary[key] = []

        # Regardless of existence, append word at index + 3 to the value list.
        working_dictionary[key].append(split_text[i + 2])

    return working_dictionary


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    chains_dict = chains

    running_sentance = ""

    # print type(chains_dict)
    # print chains_dict

    word_key = choice(chains_dict.keys())
    print "Starting point: {}".format(word_key)

    while word_key in chains_dict:
            # find corresponding value (randomized)
            # append those items to the running sentance
            # use 2 and 3 as your new pair
            # run loop again
        next_word = choice(chains_dict[word_key])
        print "Next Word: {}".format(next_word)

        running_sentance += next_word
        print "Running sentance: {}".format(running_sentance)
        # return text

        # first word in new tuple is index 1 of the old tuple and next_word


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print input_text
# Get a Markov chain
chains = make_chains(input_text)
# print working_dictionary
# Produce random text
random_text = make_text(chains)

print random_text
