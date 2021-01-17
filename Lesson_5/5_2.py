"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
count_lines = 0
count_words = 0
dict_words = {}
with open("lesson_5_2.txt", "r") as f:
    for line in f:
        count_lines += 1
        count_words = len(line.split())
        dict_words[f'{count_lines} строка'] = f'{count_words} слов'
        count_words = 0
for i in dict_words:
    print(f'{i} : {dict_words[i]}')
