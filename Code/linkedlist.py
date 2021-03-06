#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty lis
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) because of the while loop"""
        # TODO: Loop through all nodes and count one for each

        count = 0 # O(1)
        node = self.head # O(1)

        while node: # from 1 to n iterations
            count += 1  # O(1)
            node = node.next # O(1)
        return count # O(1)

        # 2n + 3 = O(n)

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) because in the function there are only constant time operations"""

        new_node = Node(item) # O(1)

        if self.head == None:                             
            self.head = new_node # O(1)
            self.tail = new_node # O(1)
        else:                               
            self.tail.next = new_node # O(1)
            self.tail = new_node # O(1)

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) because in the function there are only constant time operations"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists

        new_node = Node(item) # O(1)

        if self.head != None:                                
            new_node.next = self.head # O(1)
            self.head = new_node # O(1)
        else:
            self.head = new_node # O(1)
            self.tail = new_node # O(1)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) If the data is in the first node. Then the best case would be constant time.
        TODO: Worst case running time: O(n) If you have to go through the whole linked list. Then the worst case would be linear. """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        current_node = self.head # O(1)

        while current_node is not None: # from 1 to n iterations
            if quality(current_node.data) is True:
                return current_node.data # O(1)
            else:
                current_node = current_node.next # O(1)
        #Did not find item in ll 
        return None # O(1)

        # 2n + 2 = O(n)

    def delete(self, item):
            """Delete the given item from this linked list, or raise ValueError.
            TODO: Best case running time: O(1) If the firt item happens to be the one we are looking for
            TODO: Worst case running time: O(n) if we have to go through the whole 
            linked list to find item that we want to delete or item does not exist"""
            # TODO: Loop through all nodes to find one whose data matches given item
            # TODO: Update previous node to skip around node with matching data
            # TODO: Otherwise raise error to tell user that delete has failed
            # Hint: raise ValueError('Item not found: {}'.format(item))

            current_node = self.head  # O(1)
            previous_node = None # O(1)

            while current_node: # from 1 to n iterations
                # if/else block checks for match and deletes node depending on its location in the ll
                if self.head.data == item:
                    # checks to see if more than one item is on ll
                    if self.head.next != None:
                        self.head = self.head.next # O(1)
                        break
                    # if there isn't it deletes the item from the linked list
                    else:
                        self.head = None # O(1)
                        self.tail = None # O(1)
                        break
                elif current_node.data == item:
                    # deletes tail
                    if current_node == self.tail:
                        previous_node.next = None # O(1)
                        self.tail = previous_node # O(1)
                        break
                    # if found in the middle
                    else:
                        previous_node.next = current_node.next # O(1)
                        break
                        
                # keeps traversing through ll   
                previous_node = current_node # O(1)
                current_node = current_node.next # O(1)

            if current_node == None:
                raise ValueError('Item not found: {}'.format(item)) # O(1)

            # 12n + 4 = O(n)


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['A', 'B', 'C']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
