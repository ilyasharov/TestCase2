from collections import deque

class FifoBufferDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def put(self, item):
        self.buffer.append(item)

    def get(self):
        return self.buffer.popleft()

    def is_empty(self):
        return not self.buffer

    def is_full(self):
        return len(self.buffer) == self.capacity