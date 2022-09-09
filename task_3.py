# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def SumList(list):
    our_sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            our_sum = our_sum + int(list[i])
    return our_sum

our_list = input('Введите список чисел: ').split()
print(SumList(our_list))

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д..

def RezList(list):
    rez_list = []
    for i in range(0, len(list)):
        a = int(list[i])
        list.reverse()
        b = int(list[i])
        rez_list.append(a * b)
    return rez_list

our_list = input('Введите список чисел: ').split()
print(RezList(our_list))


# 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

our_list = list(map(float, input('Введите список вещественных чисел: ').split()))

new_list = [round(i%1,2) for i in our_list if i%1 != 0]
print(max(new_list) - min(new_list))


# 4. Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.

n = int(input('Введите целое число: '))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(f'Двоичное число: {b}')


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('Введите целое число: '))
k1 = 0
k2 = 1
if k <= 0:
    k = input('Введите число > 0: ')
elif k == 1:
    print(k1)
elif k == 2:
    print(k2)
else:
    print(0, 1, end=' ')
    for i in range(2, k):
        k1, k2 = k2, k1 + k2
        print(k2, end=' ')