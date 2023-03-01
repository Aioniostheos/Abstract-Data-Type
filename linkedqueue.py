class Node:
    """
    A node in a linked queue.

    :author: Aioniostheos
    """

    def __init__(self, value):
        """
        Initialize a node.
        """
        self.value = value
        self.next = None


class LinkedQueue:
    """
    A linked version of a queue.

    :author: Aioniostheos
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.__first = None

    def dequeue(self):
        """
        Remove and return the front item of the queue.

        :return: the front item.
        """
        node = self.__first
        self.__first = self.__first.next
        return node.value

    def enqueue(self, item):
        """
        Add an item to the back of the queue.

        :param item: the item to enqueue.
        """
        node = self.__first
        while node.next is not None:
            node = node.next
        node.next = Node(item)

    def is_empty(self):
        """
        :return: True if the queue is empty, False otherwise.
        """
        return self.__first is None

    def peek(self):
        """
        Return the front item of the queue without removing it.

        :return: the front item.
        """
        return self.__first.value

    def size(self):
        """
        :return: the size of the queue.
        """
        count = 0
        node = self.__first
        while node is not None:
            count += 1
            node = node.next
        return count
