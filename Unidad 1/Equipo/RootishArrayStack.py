import math


class RootishArrayStack:
    def __init__(self):
        self.blocks = []

    def index_to_block(self, i):
        return int((-3 + math.sqrt(9 + 8 * i)) / 2)

    def get(self, i):
        b = self.index_to_block(i)
        j = i - (b * (b + 1)) // 2
        return self.blocks[b][j]

    def set(self, i, x):
        b = self.index_to_block(i)
        j = i - (b * (b + 1)) // 2
        self.blocks[b][j] = x

    def add(self, i, x):
        r = len(self.blocks)
        if r * (r + 1) // 2 < len(self.blocks):
            self.blocks.append([None] * r)
        self.blocks.append([None] * (r + 1))
        for j in range(len(self.blocks) - 1, i, -1):
            b = self.index_to_block(j - 1)
            j_prev = j - (b * (b + 1)) // 2
            j_curr = j_prev + 1
            if j_curr == len(self.blocks[b]):
                self.blocks[j].insert(0, None)
            else:
                self.blocks[j][j_curr] = self.blocks[j][j_prev]
        self.set(i, x)

    def remove(self, i):
        x = self.get(i)
        for j in range(i, self.size() - 1):
            self.set(j, self.get(j + 1))
        r = len(self.blocks)
        if (r - 2) * (r - 1) // 2 >= len(self.blocks):
            self.blocks.pop()
        else:
            self.blocks[r - 1].pop()
        return x

    def size(self):
        return sum(len(block) for block in self.blocks)

    def __str__(self):
        return str([self.get(i) for i in range(self.size())])
