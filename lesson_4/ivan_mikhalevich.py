import os

d = {a: a + 1 for a in range(9)}
b = ('x', '0')
choice = input('Выберите x или 0 для игры ')

while choice not in b:
    try:
        print('Вы ввели не x или 0')
        choice = input('Выберите x или 0 для игры ')
    except ValueError:
        print('Вы ввели не x или 0')
        choice = input('Выберите x или 0 для игры ')

player1 = choice

if player1 == 'x':
    player2 = '0' 
else:
    player2 ='x'

game_mode = 0
while game_mode < 9:
    game_mode += 1
    for a in range(3):
        print(d[0 + a * 3], '|', d[1 + a * 3], '|', d[2 + a * 3])
        print('---------')
    print('Ход игрока ', choice)
    position = int(input('Введите номер ячейки для ввода '))
    while d[position - 1] in b:
        print('Вы выбрали занятую ячейку')
        position = int(input('Введите номер ячейки для ввода '))
    d[position - 1] = choice    
    if d[0] == d[1] == d[2] or d[0] == d[3] == d[6] or d[0] == d[4] == d[8] \
    or d[2] == d[4] == d[6] or d[1] == d[4] == d[7] or d[5] == d[4] == d[3] \
    or d[5] == d[2] == d[8] or d[6] == d[7] == d[8]:
        print('Игрок', choice, 'выиграл.')
        restart =''
        restart = int(input('Вы хотите продолжить играть? \n 1 - Да \n 2 - Выход \n'))
        if restart == 1:
            game_mode = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            d = {a: a + 1 for a in range(9)}
        else:
            break
        
    else:
        if game_mode == 9:
            print('Ничья')
            restart = int(input('Вы хотите продолжить играть? \n 1 - Да \n 2 - Выход \n'))
            if restart == 1:
                game_mode = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                d = {a: a + 1 for a in range(9)}
            else:
                break
        else:
            pass

    if choice == 'x':
        choice = '0'
    else:
        choice = 'x'