"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint
with open('lesson_5_5.txt', 'a') as f:
    random_number_count = randint(1, 100)
    for i in range(random_number_count):
        f.write(str(randint(1, 1000)) + ' ')

with open('lesson_5_5.txt', 'r') as f:
    numbers_sum = sum(list(map(int, f.readline().split())))
print(numbers_sum)
