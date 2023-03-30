
from ArrayDeque import ArrayDeque


class DualArrayDeque:
    def __init__(self):
        self.front = ArrayDeque()
        self.back = ArrayDeque()

    def add_first(self, item):
        self.front.add_first(item)
        self.balance()

    def add_last(self, item):
        self.back.add_last(item)
        self.balance()

    def remove_first(self):
        if self.front.is_empty():
            if self.back.is_empty():
                raise Exception("Deque is empty")
            self.move_items()
        return self.front.remove_first()

    def remove_last(self):
        if self.back.is_empty():
            if self.front.is_empty():
                raise Exception("Deque is empty")
            self.move_items()
        return self.back.remove_last()

    def move_items(self):
        mid = len(self.front.items)
        for i in range(mid):
            self.back.add_first(self.front.remove_last())
            if mid - len(self.front.items) > 1:
                self.front.add_last(self.back.remove_first())
        self.balance()

    def balance(self):
        n = self.size()
        if 3 * len(self.front.items) < len(self.back.items):
            new_front = ArrayDeque()
            new_back = ArrayDeque()
            new_size = n // 2
            for i in range(new_size):
                new_front.add_last(self.remove_first())
            while not self.is_empty():
                new_back.add_last(self.remove_first())
            self.front = new_front
            self.back = new_back
        elif 3 * len(self.back.items) < len(self.front.items):
            new_front = ArrayDeque()
            new_back = ArrayDeque()
            new_size = n // 2
            for i in range(new_size):
                new_back.add_first(self.remove_last())
            while not self.is_empty():
                new_front.add_first(self.remove_last())
            self.front = new_front
            self.back = new_back

    def is_empty(self):
        return self.front.is_empty() and self.back.is_empty()

    def size(self):
        return self.front.size() + self.back.size()
