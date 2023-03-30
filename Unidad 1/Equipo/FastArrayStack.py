class FastArrayStack:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.items = [None] * self.capacity

    def resize(self, new_capacity):
        new_items = [None] * new_capacity
        for i in range(self.n):
            new_items[i] = self.items[i]
        self.items = new_items
        self.capacity = new_capacity

    def push(self, item):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.items[self.n] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            raise Exception("Stack is empty")
        self.n -= 1
        item = self.items[self.n]
        self.items[self.n] = None
        if self.n > 0 and self.n == self.capacity // 4:
            self.resize(self.capacity // 2)
        return item

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n
