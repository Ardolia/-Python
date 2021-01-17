"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый
файл.
"""
f_read = open('lesson_5_4_1.txt', 'r', encoding='utf-8')
f_write = open('lesson_5_4_2.txt', 'a', encoding='utf-8')
for line in f_read:
    line = line.replace('One', 'Один')
    line = line.replace('Two', 'Два')
    line = line.replace('Three', 'Три')
    line = line.replace('Four', 'Четыре')
    f_write.write(line)
f_read.close()
f_write.close()
