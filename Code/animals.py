from pprint import pprint

def get_words(filename):
    '''Open the file and 
    return a list of all words in it.'''
    all_words_list = []
    with open(filename) as file:
        for line in file:
            word_list = line.split() #possible argument that may be used in the future ','
            for animal in word_list:
                all_words_list.append(animal)
    return all_words_list

def count_animals(animals_list):
    '''Count occurances in the given list of animals 
    and return that data structure'''

    animal_counts = {}

    for animal_name in animals_list:
        # Check if we saw this animal before
        if animal_name in animal_counts:
            animal_counts[animal_name] += 1
        else:
            animal_counts[animal_name] = 1
       
    return animal_counts

# always do this _ that way you think about a good var nam

def print_table(animal_counts):
    ''''Prints out a table of animals and their counts'''
    print('ANIMAL | COUNT')
    print('--------------')
    for animal_name in animal_counts:
        count = animal_counts[animal_name]
        # print('{} | {}'.format(animal_name, count))
        print(f'{animal_name} | {count}')
    # total_count = 0
    # for count in animal_counts.values():
    #     total_count += count
    total_count = sum(animal_counts.values())
    print('--------------')
    print(f'Total : {total_count}')

     # total_count = 0
    # for animal_name, count in animal_counts.items():
    #     total_count += count
    #     print(f'{animal_name} | {count}')

animals_list = get_words('animals.txt')
counts = count_animals(animals_list)
pprint(counts)
print_table(counts)

