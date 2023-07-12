import datetime
from datetime import datetime
from datetime import timedelta

def read_file(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as data:
            notes_array = []
            for line in data:
                item = line.replace('\n','').split(sep = ';')
                notes_array.append(item)
        return notes_array
    except:
        print(f'Не удалось открыть файл {filename}!')

def write_file(filename, notes_array):
    try:
        with open(filename, mode='w', encoding='utf-8') as data:
            for i in notes_array:
                write_element = ';'.join(i)
                data.write(f'{write_element}\n')
    except:
        print(f'Не удалось открыть файл {filename}!')

def add_note(filename, head = '', body = '', date = ''):
    notes_array = read_file(filename) 
    max_id = 0
    for i in range(1,len(notes_array)):
        if max_id < int(notes_array[i][0]): 
            max_id = int(notes_array[i][0])
    next_id = max_id + 1
    head = input('Введите заголовок: ')
    body = input('Введите текст заметки: ')
    current_date = datetime.now()
    date = current_date.strftime('%d/%m/%y %H:%M:%S')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(head)
    new_item.append(body)
    new_item.append(date)
    notes_array.append(new_item)
    write_file(filename, notes_array)
    print('Новая заметка добавлена успешно.\n')

def show_all_notes(filename):
    notes_array = read_file(filename)
    print(f"\n{'ID':<7}{'Заголовок':<30}{'Текст заметки':<80}{'Дата создания (изменения)'}")
    for i in range(1,len(notes_array)):
        print(f"{notes_array[i][0]:<7}{notes_array[i][1]:<30}{notes_array[i][2]:<80}{notes_array[i][3]}")
    print()

def show_notes_by_date(filename, date):
    flag = True
    notes_array = read_file(filename)
    check_date = datetime.strptime(date, '%d/%m/%y')
    for i in range(1,len(notes_array)):
        note_date = datetime.strptime(notes_array[i][3], '%d/%m/%y %H:%M:%S')
        if (check_date <= note_date) and (check_date + timedelta(hours=24) > note_date):
            if flag == True:
                print(f"\n{'ID':<7}{'Заголовок':<30}{'Текст заметки':<80}{'Дата создания (изменения)'}")
                flag = False
            print(f"{notes_array[i][0]:<7}{notes_array[i][1]:<30}{notes_array[i][2]:<80}{notes_array[i][3]}")
    print()
    if flag == True:
        print('Нет заметок на указанную дату!\n')

def show_note(filename, index):
    notes_array = read_file(filename)
    print(f"\n{'ID':<7}{'Заголовок':<30}{'Текст заметки':<80}{'Дата создания (изменения)'}")
    print(f"{notes_array[index][0]:<7}{notes_array[index][1]:<30}{notes_array[index][2]:<80}{notes_array[index][3]}")
    print()

def find_note_ID(filename, ID):
    notes_array = read_file(filename)
    for i in range(1,len(notes_array)):
        if notes_array[i][0] == str(ID):
            return i
    return None      

def change_note(filename, item_ID):
    notes_array = read_file(filename)
    head = input('Введите заголовок: ')
    body = input('Введите текст заметки: ')
    current_date = datetime.now()
    date = current_date.strftime('%d/%m/%y %H:%M:%S')
    notes_array[item_ID][1] = head
    notes_array[item_ID][2] = body
    notes_array[item_ID][3] = date
    write_file(filename, notes_array)
    print('Изменения внесены успешно.')
    show_note(filename, item_ID)

def delete_note(filename, ID):
    notes_array = read_file(filename)
    notes_array.pop(int(ID))
    write_file(filename, notes_array)

def menu():
    user_input = None
    while user_input != 0:
        print('1 - Показать все заметки')
        print('2 - Найти заметки по дате')
        print('3 - Добавить заметку')
        print('4 - Изменить заметку')
        print('5 - Удалить заметку')
        print('0 - Выход')
        try:
            user_input = int(input('Выберите пункт меню: '))
        except:
            print('Введено нечисловое значение!')
        match user_input:
            case 1:
                try:
                    show_all_notes(filename)
                except:
                    print(f'Ошибка при обработке данных!\n')
            case 2:
                date_input = input('Укажите дату в формате ДД/ММ/ГГ: ')
                try:
                    show_notes_by_date(filename, date_input)
                except:
                    print(f'Ошибка при обработке данных!\n')
            case 3:
                try:
                    add_note(filename)
                except:
                    print(f'Ошибка при обработке данных!\n')
            case 4:
                date_input = int(input('Укажите ID заметки для внесения изменений: '))
                try:
                    ID = find_note_ID(filename, date_input)
                    if ID != None and ID != 0:
                        print('Редактирование заметки: ')
                        show_note(filename, ID)
                        change_note(filename, ID)
                    else:
                        print('Заметка с таким ID не найдена!\n')
                except:
                    print(f'Ошибка при обработке данных!\n')
            case 5:
                try:
                    date_input = int(input('Укажите ID зметки для удаления: '))
                    ID = find_note_ID(filename, date_input)
                    if ID != None and ID != 0:
                        print('Удалена заметка: ')
                        show_note(filename, ID)
                        delete_note(filename, ID)
                    else:
                        print('Заметка с таким ID не найдена!\n')
                except:
                    print(f'Ошибка при обработке данных!\n')
            case 0:
                print('Работа завершена.\n')
            case _:
                print('Введите значение 0...5\n')

filename = 'notes.csv'
menu()