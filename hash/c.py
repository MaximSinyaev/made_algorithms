"""
Реализуйте прошитый ассоциативный массив с использованием хеш таблицы.

Входные данные
Входной файл содержит описание операций, их количество не превышает 100000. В каждой строке находится одна из следующих
операций:

    put 𝑥 𝑦 — поставить в соответствие ключу 𝑥 значение 𝑦. Если элемент уже есть, то значение необходимо изменить.
    delete 𝑥 — удалить ключ 𝑥. Если элемента 𝑥 нет, то ничего делать не надо.
    get 𝑥 — если ключ 𝑥 есть в множестве выведите соответствующее ему значение, если нет выведите «none».
    prev 𝑥 — вывести значение соответствующее ключу находящемуся в ассоциативном массиве, который был вставлен позже
        всех, но до 𝑥 или «none», если такого нет или в массиве нет 𝑥.
    next 𝑥 — вывести значение соответствующее ключу находящемуся в ассоциативном массиве, который был вставлен раньше
        всех, но после 𝑥 или «none», если такого нет или в массиве нет 𝑥.

Ключи и значения — строки из латинских букв длинной не более 20 символов.

Выходные данные
Выведите последовательно результат выполнения всех операций get, prev, next.
Следуйте формату выходного файла из примера.
"""
import sys


SEPARATOR = "\n"
UNICODE = "utf-8"

class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"{self.key}: {self.val}"


class LinkedMap:
    A = 31
    P = 1073676287
    EMPTY = list

    def __init__(self):
        self.size = 10 ** 5
        self.count = 0
        self.last = None
        self.data = [None] * self.size

    def hash(self, val: str):
        a_pow = 1
        res = 0
        for i in val:
            res = (res + ord(i) * a_pow) % self.P
            a_pow = ((a_pow * self.A) % self.P)
        res = res % self.size
        return res

    def put(self, key, val):
        h = self.hash(key)
        if self.data[h]:
            for i, node in enumerate(self.data[h]):
                if key == node.key:
                    self.data[h][i].val = val
                    return
        # Такого ключа не было, добавляем новый элемент
        self.count += 1
        new_el = Node(key, val, prev=self.last)
        if self.last:
            self.last.next = new_el
        self.last = new_el
        if not self.data[h]:
            self.data[h] = self.EMPTY()
        self.data[h].append(new_el)

    def get(self, key):
        h = self.hash(key)
        if self.data[h]:
            for node in self.data[h]:
                if key == node.key:
                    return node.val
        return 'none'

    def get_next(self, key):
        h = self.hash(key)
        if self.data[h]:
            for node in self.data[h]:
                if key == node.key:
                    return node.next.val if node.next else 'none'
        return 'none'

    def get_prev(self, key):
        h = self.hash(key)
        if self.data[h]:
            for node in self.data[h]:
                if key == node.key:
                    return node.prev.val if node.prev else 'none'
        return 'none'

    def delete(self, key):
        self.count -= 1
        h = self.hash(key)
        if self.data[h]:
            for i, node in enumerate(self.data[h]):
                if key == node.key:
                    if id(self.last) == id(self.data[h][i]):
                        self.last = self.data[h][i].prev
                    if self.data[h][i].prev:
                        self.data[h][i].prev.next = self.data[h][i].next
                    if self.data[h][i].next:
                        self.data[h][i].next.prev = self.data[h][i].prev
                    self.data[h].pop(i)
                    break


if __name__ == '__main__':
    raw_input = sys.stdin.buffer.read().splitlines()
    result_exists = list()
    linked_map = LinkedMap()

    for operation in raw_input:
        args = operation.decode(UNICODE).split()
        if args[0] == "put":
            linked_map.put(args[1], args[2])
        elif args[0] == "delete":
            linked_map.delete(args[1])
        elif args[0] == "get":
            res = linked_map.get(args[1])
            result_exists.append(res)
        elif args[0] == "next":
            res = linked_map.get_next(args[1])
            result_exists.append(res)
        elif args[0] == "prev":
            res = linked_map.get_prev(args[1])
            result_exists.append(res)

    encoded_array = (SEPARATOR.join(result_exists)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array + '\n'.encode(UNICODE))