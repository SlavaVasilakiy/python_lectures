# типы данных и переменные
# int , float , boolean , str , list , None
a = 123 # целочисленые
b = 1.23 # дробные
c = True # False

# варианты вывода
print(a, b, c)
print('{} {} {}'.format(a, b, c))
print(f'{a} {b} {c}')

# массивы \ списки
list = [1, 2, 3, 'example of text', 1.23, True] # в список можно вносить различные типы данных одновременно. Но так делать не рекомендуется :)

# ввод данных
input() # по умолчанию input принимает строковый формат, для обозначения вводимых данных нужно указать к примеру int(input())

# арифметические операции + (сложение) , - (вычетание) , * (умножение) , / (деление) деление по умолчанию работает как для дробных чисел, для деления целых чисел нужно использовать двойной знак // , % ( остаток от деления) , ** (возведение в степень)
# округление чисел
a = 1.321
b = 3
c = round(a * b, 5) # round (команда для округления) , цифра 5 вконце (число выводимых знаков после запятой и соответственно округления)

# логические операции : > , < , >= , <= , == , !=
# not , and , or
# is , is not , in , not in

# ветвления
# if \ else
a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
if a > b:
    print(a) # табуляция обязательна
else:
    print(b)

# if \ elif
username = input('Введите имя ')
if username == 'Маша':
    print('Ура, это же МАША')
elif username == 'Марина':
    print('Я так ждал Вас, МАРИНА')
elif username == 'Ильнар':
    print('ИЛЬНАР - ТОП')
else:
    print('Привет, ', username)

# циклы
# while
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# while , else
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)

# for
list = range(1, 10, 2) # range(1, 10, 2) диапозон чисел от 1 до 10 с шагом 2
for i in list:
    print(i)

# работа со строками :
text = 'съешь еще этих мягких французских булок'
print(len(text)) # покажет количество символов в строке
print('еще' in text) # есть ли фраза 'еще' в строке
print(text.isdigit()) # являются ли все символы цифрами
print(text.islower()) # являются ли все симолы символами нижнего регистра
print(text.replace('еще', 'ЕЩЕ')) # заменить еще на ЕЩЕ

# для вызова справки help(имя)

# функции
def function_name(x):
    if x == 1:
        return 'целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 1
print(function_name(arg))
