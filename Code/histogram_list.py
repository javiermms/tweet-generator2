with open('sample.txt') as f:
    text = f.read()
    words_array = text.split()
    
def create_2dArray_historgram(array):
    two_dimensional_array = []

    for word in array:
        found = False                       
        for element in two_dimensional_array:
            if word in element[0]:
                found = True
                element[1] += 1
                break

        if not found:
            two_dimensional_array.append([word, 1])

    return two_dimensional_array

# if __name__ == '__main__':
array = create_2dArray_historgram(words_array)
   