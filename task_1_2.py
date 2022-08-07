n = 1000
list_cub = [1]
next_cub = 2

# создание списка из кубов нечетных чисел
while next_cub < n:
    if next_cub % 2 != 0:
        list_cub.append(next_cub ** 3)
    next_cub = next_cub + 1


# вычисление суммы тех чисел из этого списка, сумма цифр которых делится нацело на 7
sum_dig_div_7 = 0
for next_cub in list_cub:
    sum_div_7 = 0
    while next_cub != 0:
        sum_div_7 = sum_div_7 + next_cub % 10
        next_cub = next_cub // 10
    if sum_div_7 % 7 == 0:
        sum_dig_div_7 = sum_dig_div_7 + sum_div_7
print(sum_dig_div_7)

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого cписка, сумма цифр которых делится нацело на 7
sum_dig_div_7 = 0
for next_cub in list_cub:
    next_cub = next_cub + 17
    sum_div_7 = 0
while next_cub != 0:
    sum_div_7 = sum_div_7 + next_cub % 10
    next_cub = next_cub // 10
    if sum_div_7 % 7 == 0:
        sum_dig_div_7 = sum_dig_div_7 + sum_div_7
print(sum_dig_div_7)
