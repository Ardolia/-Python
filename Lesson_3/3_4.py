# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

my_func1 = lambda x, y: x ** y
print(my_func1(2, -4))


def my_func(x, y):
    return x ** y


def my_func2(x, y):
    y = abs(y)
    for i in range(y - 2):
        x *= x
    return 1 / x


a = float(input('Введите действительное число: '))
b = int(input('Введите отрицательное целое число: '))
print(my_func(a, b))
print(my_func2(a, b))