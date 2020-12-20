weight = int(input('Введите вес ')) #запрашиваем вес
height = int(input('Введите рост ')) #запрашиваем рост
bmi = int(weight // ((height / 100) ** 2)) #получаем сам ИМТ
sep = '='

min_bmi = 16 #нижняя граница ИМТ
max_bmi = 50 #верхняя граница ИМТ
step = 1 #цена деления шкалы
symbol = '|'

first = int((bmi - min_bmi) // step) * sep #рисуем первую часть шкалы
second = int((max_bmi - bmi) // step) * sep #рисуем вторую часть шкалы
scale = str(min_bmi) + first + symbol + second + str(max_bmi)

print('Ваш индекс массы тела:', bmi)
print(scale)
