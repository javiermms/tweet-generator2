import random
import sys

arr = sys.argv
arr.pop(0)

def reverse_word(word):
    list_of_chars = []
    count = len(word)
    while count != 0:
        count -= 1
        list_of_chars.append(word[count])
        backwords = ''.join(list_of_chars)
    return backwords

def reverse(arr):
    sentence_length = len(arr)
    reverse_arr = []

    while sentence_length != 0:
        sentence_length -= 1
        reverse_arr.append(reverse_word(arr[sentence_length]))

    return reverse_arr


          
if __name__ == '__main__':
    result = reverse(arr)
    print(' '.join(result))

# cheese = "cheese"
# print(cheese[1])

#in sequencial order get words in array (get one index)
# after grabing word change words backwords
# put the new changed word at the front
# delete old word
'''
The cheese is blue
step one change the word
append it to the front 
delete normal word
eulb si eseehc ehT 
'''
# def reverse_sentence(arr):
#     print(arr)
#     for words in arr:
        
        

