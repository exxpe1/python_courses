users = {'admin':'admin', 'user':'user'}


def check_login(f):
    def wrapper():
        check = users.get(input('Введите логин '))
        if check not in users:
            print('Доступ запрещен')
        elif check == input('Введите пароль '):
            return f()
        else:
            print('Доступ запрещен')
    return wrapper


@check_login
def function_1():
    print('''\t!!!
    \tВывод секретной информации для функции 1
    \t!!!''')

@check_login
def function_2():
    print('''\t!!!
    \tВывод секретной информации для функции 2
    \t!!!''')

def function_3():
    print('Разрешен доступ к функции 3 без декоратора')

while True:
    print('''Выберите функцию для просмотра 
    1 - Функция 1, необходима проверка логина и пароля 
    2 - Функция 2, необходима проверка логина и пароля 
    3 - Функция 3, нет проверки логина и пароля
    4 - Выход''')
    choose = input()
    if choose == '1':
        function_1()
    elif choose == '2':
        function_2()
    elif choose == '3':
        function_3()
    else:
        break


