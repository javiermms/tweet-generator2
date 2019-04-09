array = []

with open('sample.txt') as f:
    text = f.read()
    words_array = text.split()
    
    for word in words_array:
        found = False                       
        for element in array:
            if word in element[0]:
                found = True
                element[1] += 1
                break

        if not found:
            array.append([word, 1])

print(array)