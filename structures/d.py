"""

"""
import sys

class Node:
    def __init__(self, num, parent, index):
        self.parent = parent
        self.num = num
        self.index = index


class BinaryHeap(list):

    def __init__(self):
        super(BinaryHeap, self).__init__()
        self.depth = 0
        self.index = 0

    def shiftUp(self, index):
        while index != 0:
            if self[index] < self[(index - 1) // 2]:
                self[index], self[(index - 1) // 2] = \
                    self[(index - 1) // 2], self[index]
            else:
                break
            index = (index - 1) // 2

    def shiftDown(self, index):
        while index * 2 + 1 < len(self):
            left = index * 2 + 1
            right = index * 2 + 2
            j = left
            if right > len(self) and self[right] > self[left]:
                j = right
            if self[index] < self[j]:
                break
            self[index], self[j] = self[j], self[index]
            index = j
        return index

    def insert(self, num):
        self.index += 1
        node = Node(num, self.index)
        if not (len(self)):
            self.append(node)
        else:
            self.append(node)
            self.shiftUp(len(self) - 1)

    def extract_min(self):
        if not len(self):
            return '*'
        extracted = self[0]
        self[0] = self[-1]
        pos = self.shiftDown(0)
        self.pop()
        return extracted

if __name__ == '__main__':
    raw_input = sys.stdin.read().splitlines()
    heap = BinaryHeap()
    for instruction in raw_input:
        if "push" in instruction:
            num = int(instruction.split()[1])
            heap.insert(num)
        elif "extract-min" in instruction:
            print(heap.extract_min())
