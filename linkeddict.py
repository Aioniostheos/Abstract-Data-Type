class Entry:
    """
    A linked dict entry.

    :author: Aioniostheos
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedDict:
    """
    A linked version of dict.

    :author: Aioniostheos
    """

    def __init__(self):
        """
        Initialize the linked dict.
        """
        self.__head = None

    def __len__(self):
        """
        :return: the length of the linked dict.
        """
        count = 0
        entry = self.__head
        while entry is not None:
            count += 1
            entry = entry.next
        return count

    def __getitem__(self, key):
        """
        Subscript operator [] overload.

        :param key: the key of the value to get.
        :return: the value with the given key.
        """
        entry = self.__head
        while entry is not None:
            if entry.key == key:
                return entry.value
            entry = entry.next
        raise KeyError()

    def __setitem__(self, key, value):
        """
        Subscript operator [] overload.

        :param key: the key of the value to set.
        :param value: the value to set.
        """
        entry = self.__head
        while entry is not None:
            if entry.key == key:
                entry.value = value
                return
            entry = entry.next
        entry.next = Entry(key, value)

    def __delitem__(self, key):
        """
        Subscript operator [] overload.

        :param key: the key of the value to delete.
        """
        previous_entry = self.__head
        while previous_entry.next is not None:
            if previous_entry.next.key == key:
                previous_entry.next = previous_entry.next.next
                return
            previous_entry = previous_entry.next

    def __contains__(self, key):
        """
        Check if the linked dict contains the given key.

        :param key: the key to check.
        :return: True if the key is in the linked dict, False otherwise.
        """
        entry = self.__head
        while entry is not None:
            if entry.key == key:
                return True
            entry = entry.next
        return False

    def keys(self):
        """
        :return: a list of all the keys in the linked dict.
        """
        keys = []
        entry = self.__head
        while entry is not None:
            keys.append(entry.key)
            entry = entry.next
        return keys

    def values(self):
        """
        :return: a list of all the values in the linked dict.
        """
        values = []
        entry = self.__head
        while entry is not None:
            values.append(entry.value)
            entry = entry.next
        return values

    def items(self):
        """
        :return: a list of all the items in the linked dict.
        """
        items = []
        entry = self.__head
        while entry is not None:
            items.append((entry.key, entry.value))
            entry = entry.next
        return items
