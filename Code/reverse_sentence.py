import random
import sys

arr = sys.argv
arr.pop(0)

def reverse(arr):
    sentence_length = len(arr)
    reverse_arr = []

    while sentence_length != 0:
        sentence_length -= 1
        reverse_arr.append(arr[sentence_length])

    return reverse_arr
          
if __name__ == '__main__':
    result = reverse(arr)
    print(' '.join(result))
