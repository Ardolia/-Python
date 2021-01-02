# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().
import random


def change_list(list_random):
    for i in range(1, len(list_random), 2):
        list_random[i - 1], list_random[i] = list_random[i], list_random[i - 1]
    return list_random


list_random = [random.randint(0, 10) for i in range(random.randint(10, 15))]
print(f'Исходный список:   {list_random}\nИзмененный список: {change_list(list_random)}')
