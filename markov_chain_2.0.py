import random
from dictogram import Dictogram
from stochastic_sampling import probability
import string
from clean_up_text import words_array
        
def create_markov(array):
    markov_chain = {}

    for num in range(len(array)-2):
        word_1 = array[num]
        word_2 = array[num + 1]
        word_3 = array[num + 2]
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

def second_order_sentence(markov_chain, length=20):
    first_words = random_start(markov_chain)
    sentence = first_words[0].capitalize() + ' ' + first_words[1] + ' '
    
    for _ in range(random.randint(0, length)):
        next_word = probability(markov_chain[first_words])
        prev_words = (first_words[1], next_word)
        first_words = prev_words
        sentence += next_word + ' '
        if prev_words not in markov_chain:
            return sentence
    return sentence

result = second_order_sentence(create_markov(words_array)))


