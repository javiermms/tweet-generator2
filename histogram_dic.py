with open('sample.txt') as f:
    text = f.read()
    words_array = text.split()

def create_dic_histogram(array):
    dic = {}
    for word in array:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    return dic 

array = create_dic_histogram(words_array)

