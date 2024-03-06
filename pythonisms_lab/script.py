# Copied Stack implementation from Data Structures and Algorithms Repository

class InvalidOperationError(Exception):
    pass


class Node:
    """
    Node class representing elements in a stack
    """

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Stack:
    """
    Stack class to intitalize and perform operations on a stack data structure

    Added additional methods to enable node iteration of stack object
    """

    def __init__(self, collection=None):
        "Modified initalizer to allow stack nodes to be iterable"
        self.top = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def insert(self, value):
        "Helper method to allow stack nodes to be iterable"
        self.top = Node(value, self.top)

    def __iter__(self):
        "Helper method to allow stack nodes to be iterable"
        current = self.top
        while current:
            yield current.value
            current = current.next

    def to_set(self):
        "Converts to a set data structure"
        return set(self.__iter__())
    
    def __eq__(self, other):
        "Checks if two stacks are equal and returns a boolean"
        return list(self) == list(other)
    
    def __bool__(self):
        """
        If stack is empty, returns False
        If stack is not empty, returns True
        """
        return not self.is_empty()

    def push(self, value):
        """
        Method to create a new node, point the new node to the top and reassigns self.top in the stack
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Method to remove top node from stack and raises an error if stack is empty
        """
        if self.is_empty():
            raise InvalidOperationError(
                "Method not allowed on empty collection")

        pop_value = self.top.value

        # move the pointer which "removes" the node from the Stack
        self.top = self.top.next

        return pop_value

    def is_empty(self):
        """
        Checks if the stack is empty
        """
        return self.top is None

    def peek(self):
        """Peek will only review the node at the top of the stack.
        Method checks the value of the node on the top and returns that value
        """
        if self.top is None:
            raise InvalidOperationError(
                "Method not allowed on empty collection")

        return self.top.value
