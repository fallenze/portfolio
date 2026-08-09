import random
import string

print('\n~~Генератор паролей~~\n')

while True:
    try:
        length = int(input('Введите длину пароля: '))
    except ValueError:
        print('Ошибка!\n')
        continue
        
    if length > 25:
        print('Пароль слишком длинный\n')
    elif length < 8:
        print('Пароль слишком короткий\n')
    else:
        break

set_password = []
for i in range(length):
    digits_letters_punctuation = [random.choice(string.digits), random.choice(string.ascii_letters)]
    set_password.append(random.choice(digits_letters_punctuation))
        
print(f'\nПароль: {''.join(set_password)}')