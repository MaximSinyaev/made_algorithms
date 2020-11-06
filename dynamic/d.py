"""
Дана текстовая строка. С ней можно выполнять следующие операции:

1. Заменить один символ строки на другой символ.

2. Удалить один произвольный символ.

3. Вставить произвольный символ в произвольное место строки.

Например, при помощи первой операции из строки «СОК» можно получить строку «СУК», при помощи второй операции — строку
«ОК», при помощи третьей операции — строку «СТОК».

Минимальное количество таких операций, при помощи которых можно из одной строки получить другую, называется стоимостью
редактирования или расстоянием Левенштейна.
Определите расстояние Левенштейна для двух данных строк.

Входные данные
Программа получает на вход две строки, длина каждой из которых не превосходит 1000 символов, строки состоят только из
заглавных латинских букв.

Выходные данные
Требуется вывести одно число — расстояние Левенштейна для данных строк.
"""
import sys


def levenstein(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    dist = max(l1, l2)
    lev_matrix = [[0 for _ in range(l1 + 1)] for __ in range(l2 + 1)]
    for i in range(l1 + 1):
        lev_matrix[0][i] = i
    for j in range(l2 + 1):
        lev_matrix[j][0] = j
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            lev_matrix[j][i] = min(lev_matrix[j - 1][i] + 1, lev_matrix[j][i - 1] + 1)
            val = 0 if s1[i - 1] == s2[j - 1] else 1
            lev_matrix[j][i] = min(lev_matrix[j - 1][i - 1] + val, lev_matrix[j][i])
            if j == l2 and l2 > l1:
                dist = min(dist, lev_matrix[j][i])
            if i == l1 and l1 > l2:
                dist = min(dist, lev_matrix[j][i])
    if l1 == l2:
        dist = lev_matrix[-1][-1]
    return dist


if __name__ == '__main__':
    raw_input = sys.stdin.buffer.read().splitlines()
    result_exists = list()
    s1 = raw_input[0]
    s2 = raw_input[1]
    res = levenstein(s1, s2)
    print(res)
