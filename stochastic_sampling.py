# from histogram_list import array
import random
from histogram_dic import array

def probability(histogram):
    '''Returns a random word based on weighted probability'''
    total_freq = 0
    cumulative_probability = 0.0

    # # Adds up all word frequency from the histogram
    # for word, count in histogram:
    #     total_freq += count

    # for dictionaty
    for key in histogram:
        total_freq += histogram[key]    

    # picks a random word weighted through frequency
    # random_num = random.uniform(0, 1)
    # for word, count in histogram:
    #     cumulative_probability += count/total_freq
    #     # checks if the random number is within the cumulative_probability or equal to it 
    #     if cumulative_probability >= random_num:
    #         return word

    random_num = random.uniform(0, 1)
    for key in histogram:
        cumulative_probability += histogram[key]/total_freq
        # checks if the random number is within the cumulative_probability or equal to it 
        if cumulative_probability >= random_num:
            return key


def check_accuracy(histogram):
    '''Returns a dictionary of occurrences of words in a sample size of 10,000'''
    proof_dict = dict()

    # fills a dictionary with a word as a key and sets occurences to 0 
    for word, count in histogram:
        proof_dict[word] = 0
    # stores each individual sample of 10,000 function calls
    for _ in range(0, 10000):
        proof_dict[probability(histogram)] += 1

    return(proof_dict) 

if __name__ == '__main__':
    result = probability(array)
    print(result)
    