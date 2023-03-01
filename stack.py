class Stack:
    """
    A stack is a last-in-first-out (LIFO) value structure.
    This implementation uses a Python list as underlying storage.

    :author: Aioniostheos
    """

    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self.__stack = []

    def is_empty(self):
        """
        :return: True if the stack is empty, False otherwise.
        """
        return self.size() == 0

    def peek(self):
        """
        Return the top item of the stack without removing it.

        :return: the top item, None if the stack is empty.
        """
        if self.is_empty():
            return None
        else:
            return self.__stack[-1]

    def pop(self):
        """
        Remove and return the top item of the stack.

        :return: the popped item, None if the stack is empty.
        """
        if self.is_empty():
            return None
        else:
            return self.__stack.pop()

    def push(self, item):
        """
        Add an item to the top of the stack.

        :param item: the item to push.
        """
        self.__stack.append(item)

    def size(self):
        """
        :return: the size of the stack.
        """
        return len(self.__stack)
