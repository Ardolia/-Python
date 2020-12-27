# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

while True:
    check_lesson = input('Что будем проверять? Напиши 1 для "list" или 2 для "dict": ')
    if check_lesson == '2':
        time_of_year = {}
        for i in range(1, 13):
            if i == 12 or i == 1 or i == 2:
                time_of_year[i] = 'Зима'
            elif 3 <= i <= 5:
                time_of_year[i] = 'Весна'
            elif 6 <= i <= 8:
                time_of_year[i] = 'Лето'
            else:
                time_of_year[i] = 'Осень'
        while True:
            while True:
                month = input('Введите номер месяца: ')
                if month.isdigit():
                    month = int(month)
                    break
                else:
                    print('Число должно быть целое! Или вообще хотя бы число\n')
            if month <= 0 or month > 12:
                print('Вы не знаете сколько месяцев в году? Откройте календарь и попробуйте снова!')
            else:
                print(f'Вы выбрали месяц, который относится к времени года "{time_of_year.get(month)}"')
                break
        break
    elif check_lesson == '1':
        time_of_year_list = []
        for i in range(1, 13):
            if i == 12 or i == 1 or i == 2:
                time_of_year_list.append('Зима')
            elif 3 <= i <= 5:
                time_of_year_list.append('Весна')
            elif 6 <= i <= 8:
                time_of_year_list.append('Лето')
            else:
                time_of_year_list.append('Осень')
        while True:
            while True:
                month = input('Введите номер месяца: ')
                if month.isdigit():
                    month = int(month)
                    break
                else:
                    print('Число должно быть целое!\n')
            if month <= 0 or month > 12:
                print('Вы не знаете сколько месяцев в году? Откройте календарь и попробуйте снова!')
            else:
                print(f'Вы выбрали месяц, который относится к времени года "{time_of_year_list[month - 1]}"')
                break
        break
    else:
        print('Читай внимательнее и попробуй еще раз\n')
