"""
Psuedo-Code c('.'c)

Mission/Task at Hand: Take a corpus and create a markov chain using a dictionary or list of tuples.

The Dictionary Way:

Create a variable called previous_word
Create a dictionary and loop through the corpus. 
If the word is not in the dictionary add it. 
Use the previous_word word as the key.
Make a dictionary as the value with a key that is the current word and a value of one. 

If the word is in the dictionary loop through the value (inner dictionary).  
If the current word is not in this dictionary add it setting the key to current word and the value as one.
If the current word is in this dictionary increment the number by one.

The Way of The Tuple:

(~~~~Coming Soon~~~~)

Things your keeping track of:

- current word
- previous_word
- if the word has already been seen 

"""
import random
from dictogram import Dictogram

with open('sample.txt') as f:
    text = f.read()
    words_array = text.split()

def create_markov(array):
    markov_chain = {}
    arr_length = len(array) - 1
    counter = 0
    
    while counter < arr_length:

        previous_word =  array[counter]

        if counter + 1 <= arr_length:
            current_word = array[counter + 1]

        if previous_word not in markov_chain:
            markov_chain[previous_word] = Dictogram([current_word])  
        else:
            markov_chain[previous_word].add_count(current_word)
        
        counter += 1

    return markov_chain

def random_start(array):
    random_word = random.choice(array)
    return random_word

# def generate_sentence(word):

    

# print(random_start(words_array))
markov = create_markov(words_array)
random_start(markov)

