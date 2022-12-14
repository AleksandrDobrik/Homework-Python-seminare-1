# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, 
# является ли этот день выходным.

print('Enter a number from one to seven')
number = int(input())
if (0 < number < 6):
    n = 'no'
elif (5 < number < 8):
    n = 'yes'
else:
    n = 'you entered an invalid value'
print(number, ' -> ', n)
