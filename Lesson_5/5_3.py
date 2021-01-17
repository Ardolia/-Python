"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""
price_sum = 0
count_price = 0
with open("lesson_5_3.txt", "r") as f:
    for line in f:
        for i in line.split():
            if i.isdigit():
                price_sum += int(i)
                count_price += 1
                if int(i) < 20000:
                    print(line.split()[0])
print(f'Средняя зарплата : {price_sum / count_price}')
