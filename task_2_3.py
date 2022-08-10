
list2 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for element_list2 in range(len(list2)):
    name = list2[element_list2].rsplit(' ')[-1]

    print('Привет,',name.title(),'!')
