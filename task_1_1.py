duration = input('введите любую длительность в сек.: ')

sec_value = int(duration) % (24 * 3600)
day = int(duration) // (24 * 3600)
hour = sec_value // 3600
sec_value = sec_value % 3600
min = sec_value // 60
sec = sec_value % 60

if day >= 1:
    print(day, 'дн', hour, 'час', min, 'мин', sec, 'сек')
else:
    if day < 1 and hour >= 1:
        print(hour, 'час', min, 'мин', sec, 'сек')
    else:
        if day < 1 and hour < 1 and min >= 1:
            print(min, 'мин', sec, 'сек')
        else:
            print(sec, 'сек')
