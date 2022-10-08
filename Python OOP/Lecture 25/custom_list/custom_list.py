from core.helper import Helper


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
        pass

    def clear(self):
        pass

    def index(self, value):
        pass

    def count(self, value):
        pass

    def reverse(self):
        pass

    def copy(self):
        pass

    def size(self):
        pass

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



