# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input('Введите время в секундах: '))
time_hh = time_in_seconds // 3600
time_mm = time_in_seconds // 60 % 60
time_ss = time_in_seconds % 60
print(f'Вы ввели время: {time_hh // 10}{time_hh % 10}:{time_mm // 10}{time_mm % 10}:{time_ss // 10}{time_ss % 10}')

