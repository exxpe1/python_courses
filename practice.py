value1 = int(input('Введите первое число '))
value2 = int(input('Введите второе число '))
value3 = int(input('Введите третье число '))
# 1 задание
if value1 == 0 or value2 == 0 or value3 == 0:
   print('В ведённых числах есть 0')
else:
    print('Нет нулевых значений!!!')
# 2 задание
if value1 != 0:
    print(value1)
elif value2 !=0:
    print(value2)
elif value3 !=0:
    print(value3)
else:
    print('Введены все нули!')
# 3 задание
if value1 > value2 + value3:
    print(value1 - value2 - value3)
else:
    print('Первое значение меньше чем сумма 2 и 3')

# 4 задание
if value1 < value2 + value3:
    print(value2 + value3 - value1)
else:
    print('Первое значение больше чем сумма 2 и 3')

# 5 задание 
if value1 > 50 and (value2 > value1 or value3 > value1):
    print('Вася')
else:
    print('Не Вася')

# 6 задание 
if value1 > 5 or value2 == 7 and value3 == 7:
    print('Петя')
else:
    print('Не Петя')
