
from datetime import datetime
from data_job import print_job, create_job, delete_job, unlog_sys

def login(names):
    ok = False
    print("Добрый день! Необходимо залогиниться")
    print(f"{names}")
    print("Представьтесь, кто Вы?")
    while not ok:
        x = input("Введите число от 1 до 4: ")
        if x.isdigit() and 1 <= int(x) <= 4:
            ok = True
        else:
            print("Вы ошиблись!")
    return x


def inp_date(date):
    d = input("Введите дату: ")


def inp_period(period):
    ok = False
    print("Выберите период времени")
    print(f"{period}")
    while not ok:
        x = input("Введите число от 1 до 3: ")
        if x.isdigit() and 1 <= int(x) <= 3:
            ok = True
        else:
            print("Вы ошиблись!")
    return x


def inp_menu(menu):
    ok = False
    print("Что Вы хотите сделать?")
    print(f"{menu}")
    while not ok:
        x = input("Введите число от 1 до 4: ")
        if x.isdigit() and 1 <= int(x) <= 4:
            ok = True
        else:
            print("Вы ошиблись!")
    return x


def inp_txt():
    return input("Опишите суть дела: ")

