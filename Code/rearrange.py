import random
import sys

def shuffle(arr):
    '''Given an input of type list this function reshuffles it by choosing a random word from that list
    and appending it to a new list until all wo'''
    shuffled_arr = []
    while len(arr) != 0:
        word = random.choice(arr)
        # ensures there is no duplicates by removing the word from the array
        arr.remove(word)
        shuffled_arr.append(word)
    return shuffled_arr

if __name__ == '__main__':
    arr = sys.argv
    arr.pop(0)
    result = shuffle(arr)
    print(' '.join(result))


