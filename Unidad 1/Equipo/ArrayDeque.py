class ArrayDeque:
    def __init__(self):
        self.items = []

    def add_first(self, item):
        self.items.insert(0, item)

    def add_last(self, item):
        self.items.append(item)

    def remove_first(self):
        if len(self.items) == 0:
            raise Exception("Deque is empty")
        return self.items.pop(0)

    def remove_last(self):
        if len(self.items) == 0:
            raise Exception("Deque is empty")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
