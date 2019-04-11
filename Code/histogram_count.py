from histogram_tuples import array
# Output:counts_list = [(1, ['one', 'two', 'red', 'blue']), (4, ['fish'])]
# Take in a histogram
# loop through the histogram and check to see if any indidual word has the same count
# if the count is same append the words together with there given count

# [('one', 1), ('two', 1), ('red', 1), ('blue', 1), ('fish', 4)]

new_array =[]
count = len(array)-1
for element in array:
    found = False
    if array[0][1] == element[1] and element[0] != array[0][0]:
        new_array.append((element[1],[element[0],array[0][0]]))
        found = True 
        break
    if not found:
        new_array.append((1,[element[0]]))

# print(array)
print(new_array)