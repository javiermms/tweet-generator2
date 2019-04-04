import random
import sys

arr = sys.argv
arr.pop(0)

def shuffle(arr):
    shuffled_arr = []
    while len(arr) != 0:
        word = random.choice(arr)
        arr.remove(word)
        shuffled_arr.append(word)
    return shuffled_arr

if __name__ == '__main__':
    result = shuffle(arr)
    print(' '.join(result))

            