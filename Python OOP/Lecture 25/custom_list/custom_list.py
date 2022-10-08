class CustomList:
    def __init__(self):
        self.__values = []

    def get_list(self):
        return self.__values

    def append(self, value):
        self.__values.append(value)

    def remove(self, index):
        for el in range(len(self.__values)):
            if el == index:
                value = self.__values[el]
                self.__values.remove(value)
                return value

