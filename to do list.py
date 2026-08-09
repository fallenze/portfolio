from time import sleep
from sys import exit

def to_do_list():
    print('\n~~Список дел~~')
    print('\nНапишите ваш список дел\n')
    
    task = []
    start = True
    a = 1
    choice2 = 0
    
    while start:
        choice = input(f'{a}. ').capitalize()
        task.append(choice)
        
        if choice.lower() == 'стоп' or choice.lower() == 'stop':
            task.pop()
            if task == []:
                check = True
                while check:
                    end = input('Завершить программу?(да, нет): ')
                    if end.lower() == 'да':
                        print('Завершение программы...')
                        sleep(2)
                        print('Программа завершилась')
                        exit()
                    elif end.lower() == 'нет':
                        check = False
                        continue
            else:
                start = False
                start1 = True
                while start1:
                    b = 1
                    if task == []:
                        print('\nВаш список дел оказался пустым')
                        while True:
                            selected = input('Завершить программу?(да, нет): ')
                            if selected.lower() == 'да':
                                print('Завершение программы...')
                                sleep(2)
                                print('Программа завершилась')
                                exit()
                            elif selected.lower() == 'нет':
                                break
                            else:
                                print('Ошибка!')
                    else:
                        print('\n-------------------------------------------------------------------------------------')
                        print('\nВаш список дел: \n')
                        b = 1
                        for i in task:
                            print(f'{b}. {i}')
                            b += 1
                        print('\n-------------------------------------------------------------------------------------')
                    if choice2 == '5':
                        exit()
                    choice2 = input('''
                                    1 - Добавить новые дела;
                                    2 - Удалить одно дело;
                                    3 - Очистить полностью;
                                    4 - Отметить выполненные задачи;
                                    5 - Выход\n
                                    Ваш ответ: ''')
                    if choice2 == '1':
                        a = 1
                        print('\nНапишите новые дела: \n')
                        while True:
                            add = input(f'{a}. ').capitalize()
                            task.append(add)
                            if add.lower() == 'стоп' or add.lower() == 'stop':
                                task.pop()
                                break
                            elif add.isdigit():
                                task.pop()
                                print('Ошибка!')
                                a -= 1
                            elif add == '':
                                task.pop()
                                print('Ошибка!')
                                a -= 1
                            a += 1
                    elif choice2 == '2':
                        number = input('\nНапиши число дела, которое вы хотите удалить: ')
                        task.pop(int(number)-1)
                    elif choice2 == '3':
                        task.clear()
                        print('\nВаш список дел был очищен')
                        while True:
                            choice3 = input('Завершить программу?(да, нет): ')
                            if choice3.lower() == 'да':
                                print('Завершение программы...')
                                sleep(2)
                                print('Программа завершилась')
                                exit()
                                
                            elif choice3.lower() == 'нет':
                                print('\nНапишите новые дела: \n')
                                a = 1
                                while True:
                                    add = input(f'{a}. ').capitalize()
                                    task.append(add)
                                    if add.lower() == 'стоп' or add.lower() == 'stop':
                                        task.pop()
                                        break
                                    elif add.isdigit():
                                        task.pop()
                                        print('Ошибка!')
                                        a -= 1
                                    elif add == '':
                                        task.pop()
                                        print('Ошибка!')
                                        a -= 1
                                    a += 1
                                break
                            else:
                                print('Ошибка!')
                    elif choice2 == '4':
                        select = int(input('\nНапишите число дела, которое вы выполнили: '))
                        print()
                        task.insert(select-1, f'{task[select-1]} (выполнено)')
                        task.pop(select)
                    elif choice2 == '5':
                        print('\nЗавершение программы...')
                        sleep(2)
                        print('Программа завершилась')
                    else:
                        print('Ошибка!')
        elif choice.isdigit():
            task.pop()
            print('Ошибка!')
            a -= 1
        elif choice == '':
            task.pop()
            print('Ошибка!')
            a -= 1
        a += 1
         
if __name__ == '__main__':
    to_do_list()