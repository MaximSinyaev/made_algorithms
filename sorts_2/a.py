"""
Батальон клонов вышел на построение. Все имперцы стали в один ряд и пересчитались: первый, второй, третий, …, n-й.
Каждый из них держит в руках бумажку с результатом своего тестирования IQ. Как известно, результатом тестирования IQ
является число от 1 до 109. Периодически к батальону подходит граф Дуко, размахивает мечом и делает запрос: «Если всех
клонов с i-го по j-го упорядочить по результату теста, то какое значение будет у клона, стоящем на k-м месте?» — и
быстро требует ответ, грозя всю партию пустить в расход. Большая просьба — решите эту задачу и помогите клонам выжить.


Входные данные
В первой строке входного файла содержится целое число n — количество клонов (1≤n≤1000).

Во второй строке содержатся эти n целых чисел, разделённые пробелами. Числа находятся в промежутке от 1 до 10^9.
В третьей строке содержится число m — количество запросов (1≤m≤10^5).

Последние m строк содержат запросы в формате «i j k». Гарантируется, что запросы корректны, то есть 1≤i≤j≤n и на отрезке
 от i-го до j-го элемента включительно есть хотя бы k элементов.


Выходные данные
На каждый запрос выведите единственное число — ответ на запрос.
"""
import random


def qfind(array: list, k: int):
    if k == 0:
        return array[0]
    left = list()
    right = list()
    pivot_idx = random.randint(0, len(array) - 1)
    pivot = array[pivot_idx]
    for element in array:
        if element >= pivot:
            right.append(element)
        else:
            left.append(element)
    if len(left) == k - 1:
        return pivot
    if len(left) >= k:
        return qfind(left, k)
    else:
        return qfind(right, k - len(left))


if __name__ == '__main__':
    n = int(input())
    clones = [int(_) for _ in input().split()]
    m = int(input())
    for _ in range(m):
        i, j, k = [int(_) for _ in input().split()]
        print(qfind(clones[i - 1:j], k))