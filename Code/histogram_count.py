# Output:counts_list = [(1, ['one', 'two', 'red', 'blue']), (4, ['fish'])]
#loop through the if the word is unique append it to an array and set the frequncy to one
# if the word is not unique count the frequency and create a tuple
# note that the words go in array that makes up a tuple 
# array[tuple(1,array[])]

with open('sample.txt') as f:
    array = list()
    duplicate_array = list()
    output = list()
    text = f.read()
    words_array = text.split()
    new_array = list()
    
    count = 1
    for word in words_array:
        found = False
        for element in array:
            if word == element:
                count += 1
                found = True
                break
        
        if not found:
            array.append(word)
    if found:
        duplicate_array.append(word)
            
    output.append((1, array))
    output.append((count, duplicate_array))
    
    
    

# print(array)
print(output)