# 1. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

our_list = list(map(int, input("Введите список чисел: ").split()))
print(f"Исходный список: {our_list}")

new_list = []
[new_lst.append(i) for i in our_lst if i not in new_list]

print(f"Список из неповторяющихся элементов: {new_list}")


# 2. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

our_list = list(map(float, input('Введите список вещественных чисел: ').split()))

new_list = [round(i%1,2) for i in our_list if i%1 != 0]
print(max(new_list) - min(new_list))

# 3. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

our_list = list(map(int, input('Введите список чисел: ').split()))

new_list = [our_list[i] for i in range(len(our_list)) if i % 2 != 0]

print(sum(new_list))