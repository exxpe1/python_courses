import os


d={a: a + 1 for a in range(9)}
def board_print():
    for a in range(3):
        print(d[0 + a * 3], '|', d[1 + a * 3], '|', d[2 + a * 3])
        print('---------')


choice = input('Выберите X или 0 для игры ')
player1 = choice
if player1 == 'x':
    player2 = '0' 
else:
    player2 ='x'

game_mode = '0'


while game_mode == '0':
    board_print()
    print('Ход игрока ', choice.upper())
    position = int(input('Введите номер ячейки для ввода '))
    d[position - 1] = choice
    if d[0] == d[1] == d[2] or d[0] == d[3] == d[6] or d[0] == d[4] == d[8] \
        or d[2] == d[4] == d[6] or d[1] == d[4] == d[7] or d[5] == d[4] == d[3] \
        or d[5] == d[2] == d[8] or d[6] == d[7] == d[8]:
            print('Игрок ', choice.upper(), 'выиграл.')
            #print('\n 1 - начать заново \n 2 - выход')
            #next_choice = int(input('Выберите действие для продолжения'))
            #if next_choice == 1:
                   # d={a: a + 1 for a in range(9)}
                   # game_mode == '0'
                   # clear = lambda: os.system('cls')
                   # clear()
            #elif next_choice == 2 :
                   # game_mode == '0'
           # else:
                   # print('Вы выбрали неправильную опцию')
                   # next_choice = int(input('Выберите действие для продолжения'))
    else:
        pass
  
    if choice == 'x':
        choice = '0'
    else:
        choice = 'x'

