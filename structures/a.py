"""
Вам требуется реализовать структуру данных, выполняющую следующие операции:

    Добавить элемент 𝑥 в конец структуры.
    Удалить последний элемент из структуры.
    Выдать минимальный элемент в структуре.

Входные данные
В первой строке входного файла задано одно целое число 𝑛 — количество операций (1≤𝑛≤106). В следующих 𝑛 строках заданы
сами операции. В 𝑖–ой строке число 𝑡𝑖 — тип операции (1, если операция добавления. 2, если операция удаления. 3,
если операция минимума). Если задана операция добавления, то через пробел записано целое число 𝑥 — элемент, который
следует добавить в структуру (−109≤𝑥≤109). Гарантируется, что перед каждой операцией удаления или нахождения минимума
структура не пуста.

Выходные данные
Для каждой операции нахождения минимума выведите одно число — минимальный элемент в структуре. Ответы разделяйте переводом строки.
"""
import sys


class Node:
    def __init__(self, data, prev=None):
        self.data = data
        self.min_el = min(data, prev.min_el) if prev else data
        self.next = None
        self.prev = prev

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data, self.tail)
            self.tail = self.tail.next
        self.size += 1

    def pop(self):
        if self.size == 1:
            del self.head
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def find_min(self):
        return self.tail.min_el


if __name__ == '__main__':
    raw_input = sys.stdin.read().splitlines()
    n = int(raw_input[0])
    linked_list = LinkedList()
    for i in range(n):
        op = [_ for _ in raw_input[1 + i].split()]
        if op[0] == "1":
            linked_list.append(int(op[1]))
        elif op[0] == "2":
            linked_list.pop()
        elif op[0] == "3":
            sys.stdout.write(str(linked_list.find_min()) + "\n")
