"""
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух
чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * +
означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о
приоритете операторов для своего чтения.

Дано выражение в обратной польской записи. Определите его значение.

Входные данные
В единственной строке записано выражение в постфиксной записи, содержащее однозначные числа и операции +, -, *. Строка
содержит не более 100 чисел и операций.

Выходные данные
Необходимо вывести значение записанного выражения. Гарантируется, что результат выражения, а также результаты всех
промежуточных вычислений по модулю меньше 231.
"""
import sys

class Stack:
    def __init__(self):
        self.size = 0
        self.max_size = 2
        self.data = [0] * self.max_size

    def append(self, value):
        if self.size == self.max_size:
            self.enlarge_capacity()
        self.data[self.size] = value
        self.size += 1

    def pop(self):
        self.size -= 1
        value = self.data[self.size]
        self.data[self.size] = 0
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
    stack = Stack()
    for symb in raw_input[0].split():
        if symb.isnumeric():
            stack.append(int(symb))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if symb == '-':
                stack.append(val2 - val1)
            elif symb == '+':
                stack.append(val2 + val1)
            if symb == '*':
                stack.append(val2 * val1)
    print(stack.pop())
