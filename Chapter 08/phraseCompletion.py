import nltk, requests
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import ngrams
from collections import Counter
import numpy as np

file = requests.get('http://www.bradfordtuckfield.com/marktwain.txt')
file = file.text
text = file.replace('\n', '')

def search_suggestion(search_term, text):
    token = nltk.word_tokenize(text)
    # bigrams = ngrams(token, 2)
    # trigrams = ngrams(token, 3)
    # fourgrams = ngrams(token, 4)
    # fivegrams = ngrams(token, 5)
    grams = [ngrams(token, 2), ngrams(token, 3), ngrams(token, 4), 
             ngrams(token, 5)]

    split_term = tuple(search_term.split(' '))
    search_term_length = len(search_term.split(' '))

    counted_grams = Counter(grams[search_term_length - 1])
    combined_term = 'No suggested searches'
    matching_terms = [element for element in list(counted_grams.items()) 
                    if element[0][:-1] == tuple(split_term)]

    if len(matching_terms) > 0:
        frequencies = [item[1] for item in matching_terms]
        maximum_frequency = np.max(frequencies)
        highest_frequency_term = [item[0] for item in matching_terms
                                if item[1] == maximum_frequency][0]
        combined_term = ' '.join(highest_frequency_term)
    return combined_term

print(search_suggestion('life is a', text))