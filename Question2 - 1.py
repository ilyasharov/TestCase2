class FifoBufferList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def put(self, item):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
        self.buffer.append(item)

    def get(self):
        if not self.buffer:
            return None
        return self.buffer.pop(0)

    def is_empty(self):
        return not self.buffer

    def is_full(self):
        return len(self.buffer) == self.capacity
