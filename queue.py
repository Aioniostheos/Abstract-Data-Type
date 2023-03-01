class Queue:
    """
    A queue is a first-in-first-out (FIFO) value structure.
    This implementation uses a Python list as underlying storage.

    :author: Aioniostheos
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.__queue = []

    def dequeue(self):
        """
        Remove and return the front item of the queue.

        :return: the front item, None if the queue is empty.
        """
        if self.is_empty():
            return None
        else:
            return self.__queue.pop(0)

    def enqueue(self, item):
        """
        Add an item to the back of the queue.

        :param item: the item to enqueue.
        """
        self.__queue.append(item)

    def is_empty(self):
        """
        :return: True if the queue is empty, False otherwise.
        """
        return self.size() == 0

    def peek(self):
        """
        Return the front item of the queue without removing it.

        :return: the front item, None if the queue is empty.
        """
        if self.is_empty():
            return None
        else:
            return self.__queue[0]

    def size(self):
        """
        :return: the size of the queue.
        """
        return len(self.__queue)
