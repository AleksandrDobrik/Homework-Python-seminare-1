# Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
#  и выдаёт номер четверти плоскости, в которой 
#  находится эта точка (или на какой оси она находится).
print('Enter non-null values')
x = int(input('Enter coordinate X '))
y = int(input('Enter coordinate Y '))

if x > 0:
    if y > 0:
        answer = '1'
    else:
        answer = '4'
else:
    if y > 0:
        answer = '2'
    else:
        answer = '3'
# не совсем понял, как точка может находиться на оси, если Х и У не равны 0.
if (x == 0 or y == 0):
    print('Your enter null values')
else:
    print(f'x = {x}, y = {y}, => {answer}')