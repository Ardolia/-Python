# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

product_list = []  # Главный список кортежей
product_temp_dict = {  # Шаблон словаря
    'Название': '',
    'Цена': '',
    'Количество': '',
    'Единицы': ''
}
count_dict = 1  # Порядковый номер записи в списке
while True:
    print('Введите новый товар:')
    product_temp_dict['Название'] = input('Название: ')
    while True:
        product_price = input('Цена: ')
        if product_price.isdigit():
            product_temp_dict['Цена'] = int(product_price)
            break
        else:
            print('Цена - это целое число!')
    while True:
        product_number = input('Количество: ')
        if product_number.isdigit():
            product_temp_dict['Количество'] = int(product_number)
            break
        else:
            print('Количество - это целое число!')
    product_temp_dict['Единицы'] = input('В чем измеряется: ')
    product_temp_tuple = tuple([count_dict, product_temp_dict])  # Генерируем кортеж
    count_dict += 1
    product_list.append(product_temp_tuple)  # Добавляем кортеж в список
    product_temp_dict = {
        'Название': '',
        'Цена': '',
        'Количество': '',
        'Единицы': ''
    }
    s = input('Продолжить? (Д/Н) : ')   #
    if s == 'Н' or s== 'н':
        break
print('Список товаров: ')
for i in product_list:
    print(i)
list_name = []
list_price = []
list_number = []
list_ci = []
for i in range(len(product_list)):
    list_name.append(product_list[i][1]['Название'])
    list_price.append(product_list[i][1]['Цена'])
    list_number.append(product_list[i][1]['Количество'])
    list_ci.append(product_list[i][1]['Единицы'])
product_final = {'Название': list_name, 'Цена': list_price, 'Количество': list_number, 'Единицы': list_ci}
print('Итого вы добавили: ')
for key, value in product_final.items():
    print("{0}: {1}".format(key, value))
