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

    bi_gram = ()
    working_dictionary = {}
    # index_first = 0
    # index_second = 1

    split_text = input_text.split()
    # print split_text

    for i in range(len(split_text) - 2):  # currently list of strings aka words

        key = (split_text[i], split_text[i + 1])

        working_dictionary[key] = None

        # bi_gram = bi_gram + (split_text[index_first], split_text[index_second])
        # index_first += 1
        # index_second += 1

        # print "Incremented? {}".format(split_text[index_first])
    print working_dictionary
        # print index_first
        # print index_second
    return working_dictionary

    # print bi_gram
    # chains = {}

    # your code goes here

    # return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
print input_text
# Get a Markov chain
chains = make_chains(input_text)
# print working_dictionary
# Produce random text
random_text = make_text(chains)

print random_text
