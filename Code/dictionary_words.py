import random
import sys

number = sys.argv[1]
# make functions simple dont do everything in one function
# each line does a diffrent thing
# seperate it that way the file is not called everytime you call it

def sentence_generator(num):
    random_words = list()

    with open('/usr/share/dict/words') as f:
        text = f.read().splitlines()

        while int(num) > len(random_words):
            random_number = random.randint(0,len(text)-1)
            randword = text[random_number]
            random_words.append(randword)
        # check for duplicates? smaller the file you get duplicates
    
    return " ".join(random_words) + '.'

print(sentence_generator(number))
