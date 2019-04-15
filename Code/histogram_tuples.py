with open('sample.txt') as f:
    tupel = ()
    text = f.read()
    word_list = text.split()

#tuple is immutable list so the frequency and word cannot be changed once added 
array = []

def histogram_tuple(words_array):
    '''Creates a histogram of an array of tuples containing a word and its frequency'''

    for word in words_array:
        # found = False
        for current_tuple in array:
            if word == current_tuple[0]:
                count = current_tuple[1] + 1
                array.append((word, count))
                array.remove(current_tuple)
                found = True
                break
        else:
            array.append((word, 1))
    
    return array

if __name__ == '__main__':  
    print(histogram_tuple(word_list))