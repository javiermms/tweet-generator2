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