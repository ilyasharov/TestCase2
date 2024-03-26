from queue import Queue

class FifoBufferQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = Queue(maxsize=capacity)

    def put(self, item):
        self.buffer.put(item)

    def get(self):
        return self.buffer.get()

    def is_empty(self):
        return self.buffer.empty()

    def is_full(self):
        return self.buffer.full()