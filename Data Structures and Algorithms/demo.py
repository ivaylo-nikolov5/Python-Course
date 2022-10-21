from queue.queue import Queue

queue = Queue()
queue.enqueue(10)
queue.enqueue(34)
queue.enqueue(15)
queue.enqueue(38)

print(queue.get_queue())
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.get_queue())
