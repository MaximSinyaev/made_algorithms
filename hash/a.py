"""
Реализуйте множество с использованием хеш таблицы.

Входные данные

Входной файл содержит описание операций, их количество не превышает 1000000. В каждой строке находится одна из следующих
операций:
    insert 𝑥 — добавить элемент 𝑥 в множество. Если элемент уже есть в множестве, то ничего делать не надо.
    delete 𝑥 — удалить элемент 𝑥. Если элемента 𝑥 нет, то ничего делать не надо.
    exists 𝑥 — если ключ 𝑥 есть в множестве выведите «true», если нет «false».

В множество помещаются и извлекаются только целые числа, не превышающие по модулю 10^9.

Выходные данные
Выведите последовательно результат выполнения всех операций exists. Следуйте формату выходного файла из примера.
"""
import random
import sys


SEPARATOR = "\n"
UNICODE = "utf-8"


class MySet():
    # A = random.randint(1, 100)
    A = 17
    P = 1073676287
    EMPTY = None

    def __init__(self):
        self.size = 10 ** 6
        self.count = 0
        self.data = [self.EMPTY] * self.size

    def hash(self, val: int):
        return (self.A * val % self.P) % self.size

    def rehash(self):
        self.size *= 2
        old_data = self.data
        self.data = [self.EMPTY] * self.size
        for old_val in old_data:
            if old_val != self.EMPTY:
                self.insert(old_val)
        # print("Old data", old_data)
        # print("Rehashed", self.data)
        del old_data

    def insert(self, val: int):
        h = self.hash(val)
        i = h
        while self.data[i] != self.EMPTY:
            if self.data[i] == val:
                return
            i = (i + 1) % self.size
        self.data[i] = val
        self.count += 1
        if self.count >= self.size // 2:
            self.rehash()

    def get(self, val: int):
        h = self.hash(val)
        i = h
        while self.data[i] != self.EMPTY:
            if self.data[i] == val:
                return 1
            i += 1
        return 0

    def delete(self, val):
        if self.get(val) == 0:
            return
        self.count -= 1
        h = self.hash(val)
        while self.data[h] != self.EMPTY:
            if self.data[h] == val:
                self.data[h] = self.EMPTY
                j = (h + 1) % self.size
                while self.data[j] != self.EMPTY:
                    if self.hash(self.data[j]) <= h:
                        self.data[h], self.data[j] = self.data[j], self.data[h]
                        h = j
                    j = (j + 1) % self.size
            h = (h + 1) % self.size


if __name__ == '__main__':
    raw_input = sys.stdin.buffer.read().splitlines()
    result_exists = list()
    my_set = MySet()
    for operation in raw_input:
        operation = operation.decode(UNICODE)
        op, val = operation.split()
        val = int(val)
        if op == 'insert':
            my_set.insert(val)
        elif op == 'exists':
            result_exists.append('true' if my_set.get(val) else 'false')
        elif op == 'delete':
            my_set.delete(val)

    encoded_array = (SEPARATOR.join(result_exists)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array + '\n'.encode(UNICODE))
    # print(my_set.data)
