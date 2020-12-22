# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

number_int = 5
number_float = 5.5
s = 'Просто строка'
n_bool = True
number_int_user = int(input('Введите целое число: '))
number_float_user = float(input('Введите дробное число: '))
string_user = input('Введите строку: ')
print(f'Вот что ввел пользователь:\nЦелое число: {number_int_user}\nДробное число: '
      f'{number_float_user}\nСтрока: {string_user}')
