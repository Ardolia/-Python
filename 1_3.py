# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Введите цифру: '))
print(f'Получился результат: {n} + {n * 11} + {n * 111} = {n * 123}')