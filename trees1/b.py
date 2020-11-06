"""
Реализуйте сбалансированное двоичное дерево поиска.

Входные данные
Входной файл содержит описание операций с деревом, их количество не превышает 100. В каждой строке находится одна из
следующих операций:

    insert 𝑥 — добавить в дерево ключ 𝑥. Если ключ 𝑥 есть в дереве, то ничего делать не надо;
    delete 𝑥 — удалить из дерева ключ 𝑥. Если ключа 𝑥 в дереве нет, то ничего делать не надо;
    exists 𝑥 — если ключ 𝑥 есть в дереве выведите «true», если нет «false»;
    next 𝑥 — выведите минимальный элемент в дереве, строго больший 𝑥, или «none» если такого нет;
    prev 𝑥 — выведите максимальный элемент в дереве, строго меньший 𝑥, или «none» если такого нет.

В дерево помещаются и извлекаются только целые числа, не превышающие по модулю 10^9.

Выходные данные
Выведите последовательно результат выполнения всех операций exists, next, prev. Следуйте формату выходного файла из
примера.
"""
import sys

SEPARATOR = "\n"
UNICODE = "utf-8"


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return f'(key: {self.key}, height: {self.height}) <left: {self.left} right: {self.right}>'


class AVSBinaryTree:
    def __init__(self):
        self.root = None

    def exists(self, key):
        return self._exists(key, self.root)

    def _exists(self, key, node):
        if node is None:
            return False
        elif key == node.key:
            return True
        elif key < node.key:
            return self._exists(key, node.left)
        elif key > node.key:
            return self._exists(key, node.right)

    @staticmethod
    def get_height(node):
        if node:
            return node.height
        return 0

    def insert(self, key):
        self.root = self._insert(key, self.root)

    def _insert(self, key, node: Node):
        if node is None:
            return Node(key)
        elif key < node.key:
            node.left = self._insert(key, node.left)
        elif key > node.key:
            node.right = self._insert(key, node.right)
        node.height = max(self.get_height(node.left),
                          self.get_height(node.right)) + 1
        return self.balance(node)
        # return node

    def next(self, key):
        return self._next(key, self.root)

    def _next(self, key, node: Node, last_next=None):
        if node is None:
            return last_next
        elif key < node.key:
            last_next = node.key if (last_next is None) or (node.key < last_next) else last_next
            return self._next(key, node.left, last_next)
        else:
            return self._next(key, node.right, last_next)

    def prev(self, key):
        return self._prev(key, self.root)

    def _prev(self, key, node: Node, last_prev=None):
        if node is None:
            return last_prev
        elif key <= node.key:
            return self._prev(key, node.left, last_prev)
        else:
            last_prev = node.key if (last_prev is None) or (node.key > last_prev) else last_prev
            return self._prev(key, node.right, last_prev)

    def find_max(self, node=None):
        if node is None:
            return node
        while node.right:
            node = node.right
        return node

    def find_min(self, node=None):
        if node is None:
            return node
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        # print(self.root)
        self.root = self._delete(key, self.root)

    def _delete(self, key, node: Node):
        if node is None:
            return None
        elif key == node.key:
            if node.left is not None and node.right is not None:
                node.key = self.find_max(node.left).key
                node.left = self._delete(node.key, node.left)
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                del Node
                node = None
        elif key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        return self.balance(node)

    # Balancing funcs
    def count_balance(self, node):
        if node:
            return self.get_height(node.left) - self.get_height(node.right)
        return 0

    def fix_height(self, node):
        if node:
            node.height = max(self.get_height(node.left),
                              self.get_height(node.right)) + 1

    def balance(self, node):
        self.fix_height(node)
        balance = self.count_balance(node)
        # print(f'Balance of node {node} is {balance}')
        if balance < -1:
            if self.count_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        if balance > 1:
            if self.count_balance(node.left) < 0:
                node.right = self.left_rotate(node.left)
            return self.right_rotate(node)
        return node

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.fix_height(node)
        self.fix_height(new_root)
        return new_root

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.fix_height(node)
        self.fix_height(new_root)
        return new_root


if __name__ == '__main__':
    raw_input = sys.stdin.buffer.read().splitlines()
    result_exists = list()
    my_tree = AVSBinaryTree()
    for operation in raw_input:
        operation = operation.decode(UNICODE)
        op, val = operation.split()
        val = int(val)
        if op == 'insert':
            my_tree.insert(val)
            print(my_tree.root)
        elif op == 'exists':
            print(str(my_tree.exists(val)).lower())
        elif op == 'next':
            print(str(my_tree.next(val)).lower())
        elif op == 'prev':
            print(str(my_tree.prev(val)).lower())
        elif op == 'delete':
            my_tree.delete(val)
            print(my_tree.root)

    print(my_tree.root)
