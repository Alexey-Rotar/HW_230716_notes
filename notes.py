import datetime

def read_file(filename):
    with open(filename, 'r') as data:
        notes_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ';')
            notes_array.append(item)
    return notes_array

def write_file(filename, notes_array):
    with open(filename, 'w') as data:
        for i in notes_array:
            write_element = ';'.join(i)
            data.write(f'{write_element}\n')

def add_note(filename, head = '', body = '', date = ''):
    notes_array = read_file(filename) 
    max_id = 0
    for i in range(1,len(notes_array)):
        if max_id < int(notes_array[i][0]): 
            max_id = int(notes_array[i][0])
    next_id = max_id + 1
    head = input('Заголовок: ')
    body = input('Текст заметки: ') 
    current_date = datetime.datetime.now()
    date = current_date.strftime('%m/%d/%y %H:%M:%S')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(head)
    new_item.append(body)
    new_item.append(date)
    notes_array.append(new_item)
    write_file(filename, notes_array)

def show_all_notes(filename):
    notes_array = read_file(filename)    
    for i in range(1,len(notes_array)):
        print("ID: ", notes_array[i][0], "Заголовок: ", notes_array[i][1],"Текст заметки: ", notes_array[i][2], "Дата: ", notes_array[i][3])

def show_item(filename, ID):
    notes_array = read_file(filename)
    print(notes_array[ID])

def find_note_ID(filename, ID):
    notes_array = read_file(filename)
    for i in range(1,len(notes_array)):
        if notes_array[i][0] == str(ID):
            return i
        else:
            return None      

def change_note(filename, item_ID):
    notes_array = read_file(filename)
    head = input('Заголовок: ')
    body = input('Текст заметки: ')
    current_date = datetime.datetime.now()
    date = current_date.strftime('%m/%d/%y %H:%M:%S')
    notes_array[item_ID][1] = head
    notes_array[item_ID][2] = body
    notes_array[item_ID][3] = date

    write_file(filename, notes_array)
    print('Измененная запись: ')
    print(notes_array[item_ID])

def delete_note(filename, ID):
    notes_array = read_file(filename)
    notes_array.pop(int(ID))
    write_file(filename, notes_array)

def menu():
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input())

    if user_operation == 1:
        show_all_notes(filename)
    elif user_operation == 2: 
        add_note(filename)
    elif user_operation == 3:
        user_operation = int(input('Укажите ID записи для внесения изменений: '))
        ID = find_note_ID(filename, user_operation)
        if ID != None and ID != 0:
            print('Будут вноситься изменения в запись: ')
            show_item(filename, ID)
            change_note(filename, ID)
        else:
            print('Запись с таким ID не найдена!')
    elif user_operation == 4:
        user_operation = int(input('Укажите ID записи для удаления: '))
        ID = find_note_ID(filename, user_operation)
        if ID != None and ID != 0:
            print('Удалена запись: ')
            show_item(filename, ID)
            delete_note(filename, ID)
        else:
            print('Запись с таким ID не найдена!')

filename = 'notes.csv'
menu()