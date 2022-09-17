'''
Задача: Создать информационную систему позволяющую работать
с сотрудниками некой компании \ студентами вуза \ учениками
школы
'''

from datetime import datetime
from data_base import get_data, change_data
from data_job import print_job, create_job, delete_job, unlog_sys
from data_ui import login, inp_date, inp_period, inp_menu, inp_txt
a = None

names = ("1. Константин 2. Лада 3. Вадим 4. Сергей")
menu = ("1. Создать дело 2. Удалить дело 3. Вывести все дела 4. Разлогиниться")
period = ("1. Утро 2. День 3. Вечер")

name_kode = int(login(names))
while True:
    menu_kode = int(inp_menu(menu))

    if menu_kode == 1:
        date = input("Введите дату в формате 01.01.2000: ")
        time_kode = int(inp_period(period))
        text_delo = inp_txt()
        Flag = create_job(name_kode, date, time_kode, text_delo)
        if Flag:
            print("Дело успешно создано")

    if menu_kode == 2:
        date = input("Введите дату в формате 01.01.2000: ")
        time_kode = int(inp_period(period))
        Flag1 = delete_job(name_kode, date, time_kode)
        if Flag1:
            print("Дело успешно удалено")

    if menu_kode == 3:
        date = input("Введите дату в формате 01.01.2000: ")
        print(print_job(name_kode, date))

    if menu_kode == 4:
        unlog_sys(name_kode)
        break