class Queue:
    def __init__(self):
        self.__queue = []

    def is_empty(self):
        return self.__queue == []

    def get_queue(self):
        return self.__queue

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        item = self.__queue[0]
        del self.__queue[0]
        return item

    def peek(self):
        return self.__queue[0]

