#!python3
from typing import List

class Node:
    """
    Models a Node object, containing two attributes:
    data consisting of an integer value held by each node
    next being the reference to the next node in the list
    """
    def __init__(self, data:int):
        self.data:int = data
        self.next = None
    
    def __repr__ (self):
        return "<Data: %s>" % self.data

class LinkedList:
    """
    Linked List object
    """
    def __init__(self):
        self.head:Node = None
        self.size:int = 0
    
    def add(self, data:int):
        """
        Adds new node to the beginning of the list
        """
        new_node:Node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1 # Updates size of list after adding new node

    def append(self, data:int):
        """
        Adds new node to the beginning of the list
        """

        new_node:Node = Node(data)
        if self.head is None: 
            self.head = new_node
        else:
            curr:Node = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1 # Updates size of list after adding new node

    def insert(self, data:int, index:int):
        """
        Requires: index needs to be a positive integer
        Adds new node to a specific position of the list
        """
        if index < 0: return
        elif index == 0:
            self.add(data)
        elif index > self.get_size():
            self.append(data)
        else:
            pos:int = index - 1
            curr:Node = self.head
            for i in range(pos):
                curr = curr.next

            new_node:Node = Node(data)
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1 # Updates size of list after adding new node

    def remove(self, value:int):
        """
        Removes value from list & returns Node containing said value
        If two ocurrences exist, removes the first to appear
        """
        if self.head is None: return

        found:bool = False
        res:Node = None
        # Base case
        if self.head.data == value:
            res = self.head
            self.head = self.head.next
            found = True
            
        else:
            curr:Node = self.head.next
            prev:Node = self.head
            while curr:
                if curr.data == value:
                    prev.next = curr.next
                    found = True
                    res = curr
                    break
                prev = curr
                curr = curr.next
        if found: 
            self.size -= 1 # Updates size after removing node
            return res
    
    def node_at_index(self, index):
        if index == 0: return self.head
        else:
            curr:Node = self.head
            pos:int = 0
            while pos < index:
                curr = curr.next
                pos += 1
            return curr

    def get_size(self):
        """
        Returns size of list
        """
        if self.head is None: return 0
        else:
            curr:Node = self.head
            count:int = 0
            while curr:
                curr = curr.next
                count += 1
            return count

    def __repr__(self):
        print_str:List[str] = []
        curr:Node = self.head
        i:int = 0
        if curr is None: return ""
        
        while curr:
            print_str.append("%s: %s" % (str(i),  curr))
            curr = curr.next
            i += 1
        return " --> ".join(print_str)

        
