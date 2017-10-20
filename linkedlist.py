#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any."""
        # O(n) per iterable; creation of head/tail are constants
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list"""
        # O(n); dependent on append making array is 1,
        # assigning current is 1, looping through it + appending is 2n.

        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return tuple(result)

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # O(n); 1 for accum, 1 per counter, 2n for the while loop
        accum = 0
        counter = self.head
        while counter:
            counter = counter.next
            accum += 1
        return accum
        pass

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        # O(1); depends on how many inputs are in the linked list
        # Best case: 6 operations
        # Create node, assign .data as item (2). Check if empty (1).
        # Apply self's head and tail into new_node.
        # Worst case: still the same because we know where the tail is

        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        pass

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # See append; almost the same with things switched up
        # O(6) total; constants are the same
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        pass

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # Hoo boy. It depends.
        # See each bit for their individual; constant on here is 3
        current = self.head
        previous = None
        found = False
        while current:
            if current.data == item:
                # If it's the last remaining node
                # It's constant.
                if (previous is None) and (current.next is None):
                    current.next = self.head = self.tail = None
                    found = True
                    break
                # If it's at the head.
                # Also constant. Best case due to slightly less operations
                elif previous is None:
                    self.head = self.head.next
                    found = True
                    break
                # If it's at the tail;
                # (man, if only I had double-linked list.) It's O(n)
                # Also the worst case scenario.
                elif current.next is None:
                    self.tail = previous
                    previous.next = None
                    found = True
                    break
                # All other cases
                # Dependent on size of list and where we meet it
                # Can be anywhere from one to a million
                else:
                    previous.next = current.next
                    found = True
                    break
            # Hey it's like extra 2
            previous = current
            current = current.next
        # If it's not found, then it's 0(n); had to go through all of the list
        if not found:
            raise ValueError
        pass

    def find(self, quality):
        """Return item from this linked list satisfying the given quality."""
        # O(n). Depends on how big the list is.
        # Worst case is the entire list. Best case is meeting off the bat.
        counter = self.head
        while counter:
            if quality(counter.data):
                return counter.data
            counter = counter.next
        pass

    def move(self):
        """Take out whatever the head is."""
        self.head = self.head.next
        if self.is_empty():
            self.tail = None

    def empty_fix(self):
        """If the list ends up being empty."""
        self.tail = self.head
        self.head.next = None

    def stringify(self):
        return ' '.join(self.items()).replace(" .", ".")

    def string_length(self):
        return len(self.stringify())

    def room_tweet(self):
        capitalize_input = "capitalize-room.txt"
        capitalize_these = open(capitalize_input).read().split("\n")
        text_list = self.items()

        for value, word in enumerate(text_list):
            if value is 0:
                text_list[value] = word.capitalize()
            if word in capitalize_these:
                text_list[value] = word.capitalize()
        return ' '.join(text_list).replace(" .", ".").replace(" !", "!").replace(" ?", "?")


    def empty_list(self):
        self.head = None
        self.tail = None
        return

def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print(ll)
    ll.append('D')
    print(ll)
    ll.append('E')
    print(ll)
    ll.append('F')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())
    ll.move()
    print(ll, "head:", ll.head, "tail:", ll.tail)
    ll.move()
    print(ll, "head:", ll.head, "tail:", ll.tail)
    ll.move()
    print(ll, "head:", ll.head, "tail:", ll.tail)

if __name__ == '__main__':
    test_linked_list()
