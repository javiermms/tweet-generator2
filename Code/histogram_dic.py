with open('sample.txt') as f:
    dic = {}
    text = f.read()
    words_array = text.split()

    for word in words_array:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1

print(dic)