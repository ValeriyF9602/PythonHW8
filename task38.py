'''
Задача 38

Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
'''


def read_int(text: str) -> int:

    return int(input(text))


def copy_all_contacts(path_f: str) -> list: # Запись контактов в список

    contacts_list = list()

    with open(path_f, 'r', encoding='utf-8') as contacts:

        i = 0
        for line in contacts:
            contacts_list.append((line.strip().split(':')))
            contacts_list[i][0] = contacts_list[i][0].split(',')
            contacts_list[i][1] = contacts_list[i][1].split(',')
            i += 1
    
    return contacts_list


def find_contacts(contacts_list: list, contact_name: list) -> list: # Поиско контактов по ФИО. Можно вводить неполные данные
                                                                        # (Фамилия: Ива —> Иванов, Иванова, Иванченко и т.д.)
    if contact_name == ['', '', '']: return []
    equal_contacts = list()
    
    for line in range(len(contacts_list)):
        isnt_equal = False
        
        for i in range(3):
            if contact[i] == '':
                continue
            if len(contact_name[i]) > len(contacts_list[line][0][i]):
                isnt_equal = True
                break
            
            for j in range(len(contact_name[i])):
                if contact[i][j] != contacts_list[line][0][i][j]:
                    isnt_equal = True
                    break
            
            if isnt_equal:
                break
        
        if isnt_equal:
            continue
        else:
            equal_contacts.append(line)
    return equal_contacts


def print_contact(contacts_list: list, line: int, text_1: str = '', numer: bool = False): # Вывод выбранного контакта

    print(f'\t{text_1}{contacts_list[line][0][0]} {contacts_list[line][0][1]} {contacts_list[line][0][2]}')
    if numer:
        for i in range(len(contacts_list[line][1])):
            print(f'\t\t{i + 1}. {contacts_list[line][1][i]}')
    else:
        for i in range(len(contacts_list[line][1])):
            print(f'\t\t{contacts_list[line][1][i]}')



def print_all(path_f: str): # Вывод всех контактов с их номерами телефонов

    with open(path_f, 'r', encoding='utf-8') as contacts_file:
        
        for line in contacts_file:
            line = line.strip().split(':')
            print()
            print(*line[0].split(","))
            
            for number_phone in line[1].split(','):
                print('\t> ' + number_phone)


def add_contact(path_f: str, contact_name: list): # Добавление нового контакта в конец файла

    with open(path_f, 'a', encoding='utf-8') as contacts_file:
        contacts_file.write(f'{contact_name[0]},{contact_name[1]},{contact_name[2]}:{contact_name[3]}')
        add_phone = True
        
        while add_phone:
            add_phone = int(acos(int(input('Выберите следующее действие:\n'
                                           '\t1. Добавить дополнительный номер\n'
                                           '\t2. Вернуться в главное меню\n'
                                           '\t\tНомер действия: ')) - 1))
            if add_phone:
                contacts_file.write(',' + input('Введите дополнительный номер телефона: '))
        
        contacts_file.write('\n')


def change_contact(contacts_list: list, index: int, action: int) -> list: # МЕСИВО: Изменение выбранного контакта, после чего трубуется 
                                                                                    # перезаписать файл через функцию rewrite_file().
    if action == 1:                                                                 # Лучше было разделить функцию на функции поменьше
        print('Вы действительно хотите удалить контакт:')                           # и ветвление выполнить в основном коде???
        print_contact(contacts_list, index)
        del_num = int(acos(int(input(f'\t1. Да\n\t2. Нет\n\t\tОтвет: ')) - 1))
        if del_num:
            contacts_list.pop(index)
    
    
    elif action == 2:
        print('Изменение фамилии контакта:')
        print_contact(contacts_list, index)
        contacts_list[index][0][0] = input('\tНовая фамилия: ')
    
    
    elif action == 3:
        print('Изменение имени контакта:')
        print_contact(contacts_list, index)
        contacts_list[index][0][1] = input('\tНовое имя: ')
    
    
    elif action == 4:
        print('Изменение отчества контакта:')
        print_contact(contacts_list, index)
        contacts_list[index][0][2] = input('\tНовое отчество: ')
    
    
    elif action == 5:
        
        if len(contacts_list[index][1]) > 1:
            print('Какой из номеров телефона изменить?\n')
            print_contact(contacts_list, index, numer=True)
            
            number = int(input('Порядковый номер контакта: '))
            contacts_list[index][1][number - 1] = input('Новый номер телефона: ')
        
        else:
            print('Старый номер телефона:')
            print_contact(contacts_list, index)
            contacts_list[index][1][0] = input('Новый номер телефона: ')
    
    
    elif action == 6:
        
        print(f'Добавить новый номер телефона контакту:')
        print_contact(contacts_list, index)
        
        contacts_list[index][1].append(input('\t  Ввод: '))
    
    
    elif action == 7:

        if len(contacts_list[index][1]) > 1:
            print('Какой из номеров телефона удалить?\n')
            print_contact(contacts_list, index, numer=True)
            
            number = int(input('Укажите порядковый номер:'))
            
            del_num = int(acos(int(input(f'Вы действительно хотите удалить номер: {contacts_list[index][1][number - 1]}\n'
                                         f'\t1. Да\n\t2. Нет\n\t\tОтвет: ')) - 1))
            if del_num:
                contacts_list[index][1].pop(number - 1)
        
        else:
            print('\nВы действительно хотите удалить контакт:')
            print_contact(contacts_list, index)
            del_num = int(acos(int(input('\t1. Да\n\t2. Нет\n\t\tОтвет: ')) - 1))
            if del_num:
                contacts_list.pop(index)

    return contacts_list


def rewrite_file(path_f: str, contacts_list: list):

    with open(path_f, 'w', encoding='utf-8') as contacts_file:
        
        for i in range(len(contacts_list)):
            contacts_file.write(f'{contacts_list[i][0][0]},{contacts_list[i][0][1]},{contacts_list[i][0][2]}:')
            
            for j in range(len(contacts_list[i][1])):
                
                if j < len(contacts_list[i][1]) - 1:
                    contacts_file.write(f'{contacts_list[i][1][j]},')
                
                else:
                    contacts_file.write(f'{contacts_list[i][1][j]}\n')




from math import acos

path_file = 'ContactList.txt'
params = ['фамилию', 'имя', 'отчество', 'номер телефона']

print('\n\tТЕЛЕФОННЫЙ СПРАВОЧНИК')

while True:

    action = int(input('\nГЛАВНОЕ МЕНЮ\n\n'
                       '\t1. Показать все контакты\n'
                       '\t2. Найти контакт по ФИО\n'
                       '\t3. Добавить контакт\n'
                       '\t0. ВЫХОД\n'
                       'Номер действия: '))

    if action == 1:
        print_all(path_file)

    elif action == 2:
        contact = [input(f'Введите {params[i]} (оставьте строку пустой, если вы не знаете {params[i]}):\n\t') for i in range(3)]
        
        phonebook = copy_all_contacts(path_file)
        found = find_contacts(phonebook, contact)
        
        if len(found) == 0:
            print('\tКонтакты не найдены')
        
        else:
            if len(found) == 1:
                print_contact(phonebook, found[0], 'Найден следующий контакт:\n')
                index = int(input('Выберите следующее действие:\n'
                                  '\t1. Изменить контакт\n'
                                  '\t0. Вернуться в главное меню\n'
                                  '\t\tНомер действия: ')) - 1
            
            else:
                print('\nНайдены следующие контакты:')
                for i in range(len(found)):
                    print_contact(phonebook, found[i], f'{i + 1}. ')
                
                index = int(input('Выберите следующее действие:\n'
                                   '\tУкажите порядковый номер контакта для его изменения '
                                   'или ведите 0, чтобы вернуться в главное меню\n\t\tНомер действия: ')) - 1
            
            if index >= 0:
                    
                while True:
                    new_action = int(input('Следующие действия:\n'
                        '\t1. Удалить контакт\n'
                        '\t2. Изменить фамилию\n'
                        '\t3. Изменить имя\n'
                        '\t4. Изменить отчество\n'
                        '\t5. Изменить номер телефона\n'
                        '\t6. Добавить номер телефона\n'
                        '\t7. Удалить номер телефона\n'
                        '\t0. Вернуться в главное меню\n'
                        '\t\tНомер действия: '))
                    
                    if new_action == 0:
                        break
                    
                    phonebook = change_contact(phonebook, found[index], new_action)
                    rewrite_file(path_file, phonebook)
                    
                    if new_action in [1, 7]:
                        break

    elif action == 3:
        contact = [input(f'Введите {params[i]}:\n\t') for i in range(4)]
        add_contact(path_file, contact)

    elif action == 0:
        break