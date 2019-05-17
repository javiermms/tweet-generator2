import random
from dictogram import Dictogram
from stochastic_sampling import probability
import string
from clean_up_text import words_array

def get_three_words(array):
    for index in range(len(array)-2):
        yield(array[index], array[index + 1], array[index + 2])

def create_markov(array):
    markov_chain = {}
    three_words = (get_three_words(words_array))
    
    for word_1, word_2, word_3 in three_words:
        tuple = (word_1, word_2)
        if tuple not in markov_chain:
            add_tuple = Dictogram([word_3])
            markov_chain[tuple] = add_tuple
        else:
            markov_chain[tuple].add_count(word_3)
    return markov_chain


def random_start(array):
    random_word = random.choice(list(array.keys()))
    return random_word

def second_order_sentence(markov_chain):
    length = 20
    first_words = random_start(markov_chain)
    sentence = first_words[0].capitalize() + ' ' + first_words[1] + ' '
    
    f

    

# print(random_start(words_array))
print(second_order_sentence(create_markov(words_array)))
# random_start(markov)

