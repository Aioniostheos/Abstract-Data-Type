class Node:
    """
    A node in a linked list.

    :author: Aioniostheos
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    A linked version of list.

    :author: Aioniostheos
    """

    def __init__(self):
        """
        Initialize the linked list.
        """
        self.__head = None

    def __len__(self):
        """
        :return: the length of the linked list.
        """
        count = 0
        node = self.__head
        while node is not None:
            count += 1
            node = node.next
        return count

    def __getitem__(self, index):
        """
        Subscript operator [] overload.

        :param index: the index of the value to get.
        :return: the value at the given index.
        """
        for i, value in enumerate(self):
            if i == index:
                return value

    def __setitem__(self, index, value):
        """
        Subscript operator [] overload.

        :param index: the index of the value to set.
        :param value: the value to set.
        """
        node = self.__head
        for i in range(index):
            node = node.next
        node.value = value

    def __iter__(self):
        """
        :return: the iterator for the linked list.
        """
        node = self.__head
        while node is not None:
            yield node.value
            node = node.next

    def __repr__(self):
        """
        :return: a string representation of the linked list.
        """
        return '[' + ', '.join([str(value) for value in self]) + ']'

    def append(self, value):
        """
        Add the given value to the end of the linked list.

        :param value: the value to add to the end of the linked list.
        """
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            last_node = self.__head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = node

    def insert(self, index, value):
        """
        Insert the given value at the given index in the linked list.

        :param index: the index to insert the value at.
        :param value: the value to insert.
        """
        if index >= len(self):
            raise IndexError('Index out of range.')
        node = Node(value)
        if index == 0:
            node.next = self.__head
            self.__head = node
        else:
            previous_node = self.__head
            for i in range(index - 1):
                previous_node = previous_node.next
            node.next = previous_node.next
            previous_node.next = node

    def remove(self, value):
        """
        Remove the first occurrence of the given value from the linked list.

        :param value: the value to remove from the linked list.
        """
        self.pop(self.index(value))

    def pop(self, index=-1):
        """
        Remove and return the value at the given index in the linked list.

        :param index: the index of the value to remove and return.
        :return: the value at the given index.
        """
        if index == -1:
            previous_node = self.__head
            for i in range(len(self) - 2):
                previous_node = previous_node.next
            node = previous_node.next
            previous_node.next = None
            return node.value
        elif index >= len(self):
            raise IndexError('Index out of range.')
        elif index == 0:
            node = self.__head
            self.__head = node.next
            return node.value
        else:
            previous_node = self.__head
            for i in range(index - 1):
                previous_node = previous_node.next
            node = previous_node.next
            previous_node.next = node.next
            return node.value

    def index(self, value):
        """
        :param value: the value to find the index of.
        :return: the index of the first occurrence of the given value in the linked list.
        """
        for i, item in enumerate(self):
            if item == value:
                return i
        raise ValueError('Value not found.')

    def reverse(self):
        """
        :return: a new linked list that is the reverse of the current linked list.
        """
        new_list = LinkedList()
        for value in self:
            new_list.insert(0, value)
        return new_list

