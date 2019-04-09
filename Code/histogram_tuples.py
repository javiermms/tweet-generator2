with open('sample.txt') as f:
    tupel = ()
    text = f.read()
    word_list = text.split()
    array = []

    #tuple is immutable list so the frequency and word cannot be changed once added 
    for word in word_list:
        found = False
        for inner_tuple in array:
            if word == inner_tuple[0]:
                count = inner_tuple[1] + 1
                array.remove(inner_tuple)
                array.append((word, count))
                found = True
                break
        if not found:
            array.append((word, 1))

print(array) 