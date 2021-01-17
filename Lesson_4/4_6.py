"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from sys import argv
from itertools import count, cycle

script_name, start_number, exit_number = argv
new_list = []
for i in count(int(start_number)):
    if i > int(exit_number):
        break
    else:
        new_list.append(i)
print(*new_list)
count_i = 0
for i in cycle(new_list):
    if count_i >= len(new_list):
        break
    else:
        print(i, end=' ')
        count_i += 1
print()



