import random

def rock_paper_scissors():
    
    print('\nДобро пожаловать в игру "Камень-ножницы-бумага"\n')
    
    while True:
        rules = input('Вы знаете правила(да, нет): ')
        
        if rules.lower() == 'да':
            break
        elif rules.lower() == 'нет':
            print('Правила очень просты: камень бьет ножницы, ножницы бьют бумагу, бумага бьет камень, но если оба игрока выбрали одно и то же, то в этом случае будет ничья и никому балл не засчитывается.')
        else:
            print('Ошибка!')
            
    print('\nДавайте начнем игру')
    print('Вы играете против компьютера')
    
    user_attempt = 0
    computer_attempt = 0
    
    while user_attempt < 3 and computer_attempt < 3:
        win = random.choice(['Поздравляю вы выиграли!', 'Вы выиграли!', 'Ого! Вы одержали победу'])
        lose = random.choice(['Увы! Вы проиграли', 'К сожалению, вы проиграли', 'Вы проиграли'])
        tie = random.choice(['Ничья!', 'Упс! Кажется, ничья'])
        computer_choice = random.choice(['Камень', 'Ножницы', 'Бумага'])
        
        user_choice = input('\nВаш ход: ')
        
        if (user_choice.lower() == 'камень' and computer_choice.lower() == 'ножницы') or (user_choice.lower() == 'ножницы' and computer_choice.lower() == 'бумага') or (user_choice.lower() == 'бумага' and computer_choice.lower() == 'камень'):
            print(f'Ход компьютера: {computer_choice}')
            print(win)
            
            user_attempt += 1
            
            print(f'Счет: Пользователь - {user_attempt} | Компьютер - {computer_attempt}')
        elif (user_choice.lower() == 'ножницы' and computer_choice.lower() == 'камень') or (user_choice.lower() == 'камень' and computer_choice.lower() == 'бумага') or (user_choice.lower() == 'бумага' and computer_choice.lower() == 'ножницы'):
            print(f'Ход компьютера: {computer_choice}')
            print(lose)
            
            computer_attempt += 1
            
            print(f'Счет: Пользователь - {user_attempt} | Компьютер - {computer_attempt}')
        elif user_choice.lower() == computer_choice.lower():
            print(f'Ход компьютера: {computer_choice}')
            print(tie)
            print(f'Счет: Пользователь - {user_attempt} | Компьютер - {computer_attempt}')
        else:
            print('Ошибка!')
            
    if user_attempt == 3:
        print('\nВы выиграли!')
        print(f'Счет: Пользователь - {user_attempt} | Компьютер - {computer_attempt}')
    elif computer_attempt == 3:
        print('\nВы проиграли!')
        print(f'Счет: Пользователь - {user_attempt} | Компьютер - {computer_attempt}')
        
if __name__ == '__main__':
    rock_paper_scissors()