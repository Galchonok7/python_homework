
from datetime import datetime
from data_base import get_data, change_data

a = None


def print_job(x, date):
    global a
    if date not in DIC_LOGIN:
        a = get_data(x)
    if a is None:
        a = get_data(x)
    return a[date]


def create_job(x, date, time, txt):
    global a
    if date not in DIC_LOGIN:
        a = get_data(x)
    if a is None:
        a = get_data(x)
    a.setdefault(date, ['','',''])
    a[date][time - 1] = txt

    return True
from datetime import datetime

DIC_LOGIN = \
    {
        1: ('Konstantin', 'konstatin.txt'),
        2: ('Lada', 'lada.txt'),
        3: ('Vadim', 'vadim.txt'),
        4: ('Sergey', 'sergey.txt')
    }

def delete_job(x, date, time):
    global a
    if date not in DIC_LOGIN:
        a = get_data(x)
    if a is None:
        a = get_data(x)
    a[date][time - 1] = ''
    return True


def unlog_sys(x):
    global a
    if date not in DIC_LOGIN:
        a = get_data(x)
    if a is None:
        a = get_data(x)
    change_data(a)
    a = None
    return True
