class Node:
    """
    A node in a linked stack.

    :author: Aioniostheos
    """

    def __init__(self, value):
        """
        Initialize an empty node.
        """
        self.value = None
        self.previous = None


class LinkedStack:
    """
    A linked version of a stack.

    :author: Aioniostheos
    """

    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self.__last = None

    def is_empty(self):
        """
        :return: True if the stack is empty, False otherwise.
        """
        return self.__last is None

    def peek(self):
        """
        Return the top item of the stack without removing it.

        :return: the top item.
        """
        return self.__last.value

    def pop(self):
        """
        Remove and return the top item of the stack.

        :return: the popped item.
        """
        node = self.__last
        if node is not None:
            self.__last = node.previous
            return node.value
        else:
            return None

    def push(self, item):
        """
        Add an item to the top of the stack.

        :param item: the item to push.
        """
        node = Node(item)
        node.previous = self.__last
        self.__last = node

    def size(self):
        """
        :return: the size of the stack.
        """
        count = 0
        node = self.__last
        while node is not None:
            count += 1
            node = node.previous
        return count
