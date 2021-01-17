"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
try:
    file_lesson_5_1 = open("lesson_5_1.txt", "a")
    text_user = input()
    while text_user != '':
        file_lesson_5_1.write(text_user + '\n')
        text_user = input()
except IOError:
    print('Ошибка ввода')
finally:
    file_lesson_5_1.close()
