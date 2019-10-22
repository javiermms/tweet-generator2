#!python
from __future__ import division, print_function  # Python 2 and 3 compatibility


class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
    
        if word in self:
            self[word] += count
            self.tokens += count
        else:
            self[word] = count
            self.tokens += count
            self.types += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count

        if word in self:
            return self[word]
        else: 
            return 0


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        # word = 'abracadabra'
        # print_histogram(list(word))
        # # Test histogram on words in a classic book title
        # fish_text = 'one fish two fish red fish blue fish'
        # print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        firstrow_text = ('14, 9, 5, 12, 18, 10, 35, 8, 3, 14, 1, 22, 5, 19, 13, 7, 4, 40, 13, 1, 3, 4, 8, 5, 9, 17, 6, 3, 1, 7, 2, 7, 6, 1, 6, 5, 2, 6, 3, 1, 4, 12, 15, 16, 21 ')
        print_histogram(firstrow_text.split())


if __name__ == '__main__':
    main()
