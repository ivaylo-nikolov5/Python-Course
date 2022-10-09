from core.helper import Helper, EmptyList, ValueNotExist
import copy


class CustomList:
    iterables = {
        list: Helper.iter_over_list_or_tuple_or_string,
        tuple: Helper.iter_over_list_or_tuple_or_string,
        dict: Helper.iter_over_dictionary,
        str: Helper.iter_over_list_or_tuple_or_string
    }

    def __init__(self):
        self.__values = []

    def get_list(self):
        return self.__values

    def append(self, value):
        self.__values.append(value)

    def remove(self, index):
        index = Helper.find_index(self.__values, index)
        result = self.__values[index]
        self.__values.pop(index)
        return result

    def get(self, index):
        index = Helper.find_index(self.__values, index)
        return self.__values[index]

    def extend(self, iterable):
        if type(iterable) not in self.iterables:
            raise ValueError("Value not iterable!")
        result = self.iterables[type(iterable)](self.__values, iterable)
        return result

    def insert(self, index, value):
        index = Helper.find_index(self.__values, index)
        values = Helper.insert_value_in_list(self.__values, value, index)
        self.__values = values
        return self.get_list()

    def pop(self):
        if not self.__values:
            raise EmptyList("You cannot pop an item from an empty list")
        value = self.__values[-1]
        self.__values = self.__values[:-1]
        return value

    def clear(self):
        self.__values = []

    def index(self, value):
        for idx in range(len(self.__values)):
            if self.__values[idx] == value:
                return idx
        raise ValueNotExist("The value is not in the list!")

    def count(self, value):
        result = len([x for x in self.__values if x == value])
        return result

    def reverse(self):
        if not self.__values:
            raise EmptyList("You cannot reverse an empty list!")
        result = self.__values[::-1]
        return result

    def copy(self):
        current_copy = copy.deepcopy(self.__values)
        return current_copy

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        pass

    def dictionize(self):
        pass

    def move(self, amount):
        pass

    def sum(self):
        pass

    def overbound(self):
        pass

    def underbound(self):
        pass

    def __str__(self):
        return str(list(self.get_list()))



