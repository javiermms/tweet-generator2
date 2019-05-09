#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)
        #O(1)          O(1)  lists always know there size O(1)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n) Why and under what conditions?"""
        # Collect all keys in each bucket

        all_keys = [] # O(1)

        for bucket in self.buckets: # O(n)
            for key, value in bucket.items(): #O(n)
                all_keys.append(key) # O(1)
        return all_keys # O(1)

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket

        cumulative_values = []

        for bucket in self.buckets:
            for key, value in bucket.items():
              cumulative_values.append(value)
        return cumulative_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = [] # O(1)

        for bucket in self.buckets: #b iterations => O(b*i)
            all_items.extend(bucket.items()) #O(i=n/b) for items method (load factor)
        return all_items # O(1)

        # all_items = []# O(1)
        # for bucket in self.buckets: # b iteratuons => O(b * l) => O(n) overall
        #     items = bucket.items() #O(l) because l is list's length

        #     all_items.extend(items) #O(l) see analysis below
        #     #equivalent to extend:
        #     # for item in items: # l iterations => O(l) overall
        #     #     all_items.append(item) # O(1) on average
        # return items # O(1)


    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

        count = 0 # O(1)

        for bucket in self.buckets: #b iterations => O(b*l)
            count += bucket.length() #O(l=n(entries)/b(buckets)) (L is average length)for length method (load factor) <--- how full is the hashtable
            # count = count + bucket.length()
            # O(1)    O(1)    O(l)
        return count # O(1)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(l) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

        index = self._bucket_index(key) #O(1) calculate index
        bucket = self.buckets[index] #O(1) because an array can calculate where it is because we are passing in index (what it does: getting ll)
        entry = bucket.find(lambda key_value: key_value[0] == key) #Look for key : O(l), l = length
        #item = (key, value)

        # if (entry is not None): 
        #     return True #O(1)
        # else: 
        #     return False #O(1)
        return entry is not None #check if entry was found O(1)

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(l) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        bucket = self.buckets[self._bucket_index(key)] #O(1)
        entry = bucket.find(lambda key_value: key_value[0] == key) #O(n)

        if entry is not None: 
            return entry[1] #O(1)
        else:
            raise KeyError('Key not found: {}'.format(key)) #O(1)

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        bucket = self.buckets[self._bucket_index(key)] #O(1)
        entry = bucket.find(lambda pair: pair[0] == key) #O(n)

        # new_entry = (key,value) #O(1)

        if entry is not None: #update old key value pair 
            bucket.delete(entry) #O(n) or O(1)
        #add new key value pair
        bucket.append((key,value)) #O(1)


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        bucket = self.buckets[self._bucket_index(key)] #O(1)

        key_value = bucket.find(lambda item : item[0] == key) #O(n)

        if key_value is not None:
            bucket.delete(key_value) #O(n) or O(1)
        else:
            raise KeyError('Key not found: {}'.format(key)) #O(1)



def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()