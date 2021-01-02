# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.

def my_func(a, b, c):
    if a == min(a, b, c):
        return b + c
    elif b == min(a, b, c):
        return a + c
    else:
        return a + b


print(my_func(5, 6, 7))
print(my_func(5, 5, 5))
print(my_func(5, 0, 1))
print(my_func(5, 0, -1))
print(my_func(1, 2, 7))
