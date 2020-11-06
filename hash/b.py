"""
Реализуйте ассоциативный массив с использованием хеш таблицы.

Входные данные
Входной файл содержит описание операций, их количество не превышает 100000. В каждой строке находится одна из следующих
операций:
    put 𝑥 𝑦 — поставить в соответствие ключу 𝑥 значение 𝑦. Если ключ уже есть, то значение необходимо изменить.
    delete 𝑥 — удалить ключ 𝑥. Если элемента 𝑥 нет, то ничего делать не надо.
    get 𝑥 — если ключ 𝑥 есть в ассоциативном массиве, то выведите соответствующее ему значение, иначе выведите «none».

Ключи и значения — строки из латинских букв длинной не более 20 символов.

Выходные данные
Выведите последовательно результат выполнения всех операций get. Следуйте формату выходного файла из примера.
"""
import sys

SEPARATOR = "\n"
UNICODE = "utf-8"


class MyMap:
    # A = random.randint(1, 100)
    A = 17
    P = 1073676287
    EMPTY = list

    def __init__(self):
        self.size = 10 ** 5
        self.count = 0
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
        self.count += 1
        h = self.hash(key)
        # print(key, h)
        if not self.data[h]:
            self.data[h] = self.EMPTY()
            self.data[h].append((key, val))
            return
        for i, (key_from_list, val_from_list) in enumerate(self.data[h]):
            if key == key_from_list:
                self.data[h][i] = (key, val)
                return
        self.data[h].append((key, val))

    def get(self, key):
        h = self.hash(key)
        if self.data[h]:
            for key_from_list, val_from_list in self.data[h]:
                if key == key_from_list:
                    return val_from_list
        return 'none'

    def delete(self, key):
        h = self.hash(key)
        if self.data[h]:
            for i, (key_from_list, val_from_list) in enumerate(self.data[h]):
                if key == key_from_list:
                    self.data[h].pop(i)
                    break


if __name__ == '__main__':
    raw_input = sys.stdin.buffer.read().splitlines()
    result_exists = list()
    my_map = MyMap()
    for operation in raw_input:
        args = operation.decode(UNICODE).split()
        if args[0] == "put":
            my_map.put(args[1], args[2])
        elif args[0] == "delete":
            my_map.delete(args[1])
        elif args[0] == "get":
            res = my_map.get(args[1])
            result_exists.append(res)
    # print(my_map.data)
    encoded_array = (SEPARATOR.join(result_exists)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array + '\n'.encode(UNICODE))
