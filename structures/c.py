"""
Для каждой операции изъятия элемента выведите ее результат.

На вход программе подаются строки, содержащие команды. Каждая строка содержит одну команду. Команда — это либо "+ N",
либо "-". Команда "+ N" означает добавление в очередь числа 𝑁, по модулю не превышающего 109. Команда "-" означает
изъятие элемента из очереди.

Входные данные
В первой строке содержится количество команд — 𝑚 (1⩽𝑚⩽105). В последующих строках содержатся команды, по одной в каждой
строке.

Выходные данные
Выведите числа, которые удаляются из очереди, по одному в каждой строке. Гарантируется, что изъятий из пустой очереди не
производится.
"""

import sys


class Queue:
    def __init__(self):
        self.size = 0
        self.begin = 0
        self.max_size = 2
        self.data = [0] * self.max_size

    def append(self, value):
        if self.size == self.max_size:
            self.enlarge_capacity()
        self.data[(self.size + self.begin) % self.max_size] = value
        self.size += 1

    def left_pop(self):
        value = self.data[self.begin]
        self.data[self.begin] = 0
        self.begin = (self.begin + 1) % self.max_size
        self.size -= 1
        return value

    def enlarge_capacity(self):
        new_data = [0] * self.max_size * 2
        for i in range(self.max_size):
            new_data[i] = self.data[i]
        del self.data
        self.data = new_data
        self.max_size *= 2

    def __repr__(self):
        return str(self.data)

if __name__ == '__main__':
    raw_input = sys.stdin.read().splitlines()
    n = int(raw_input[0])
    queue = Queue()
    for i in range(n):
        # print(queue)
        op = raw_input[1 + i].split()
        if op[0] == '+':
            queue.append(int(op[1]))
        else:
            print(queue.left_pop())
