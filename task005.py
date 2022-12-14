# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве.

print('Enter coordinates of two points')
x1 = int(input('Enter coordinate X1 '))
y1 = int(input('Enter coordinate Y1 '))
x2 = int(input('Enter coordinate X2 '))
y2 = int(input('Enter coordinate Y2 '))

d = round(((x2 - x1) ** 2 + (y2 - y1 ) ** 2) ** 0.5, 2)
print(d)