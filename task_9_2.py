from distutils.cmd import Command
from fileinput import filename
from imaplib import Commands
from os import path

@bot.message_handler(commands=['start'])
def take_start(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'{msg.from_user.full_name}! Приложение Калькулятор приветсвует тебя!')
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Выберите, с какими числами будем работать?\n1. Целые числа\n2. Дробные числа')
    bot.register_next_step_handler(msg, take_type_number)


'''
словарь
'''

type_of_numbers = ''
type_of_operations = ''


def take_type_number(msg: telebot.types.Message):
    if msg.text in {'1', '2'}:
        global type_of_numbers
        type_of_numbers = int(msg.text)
        bot.send_message(chat_id=msg.from_user.id, text=f'Выберите, арифметическое действие <+ - * />')
        bot.register_next_step_handler(msg, take_type_of_operations)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка, введите 1 или 2')
        bot.register_next_step_handler(msg, take_type_number)


def take_type_of_operations(msg: telebot.types.Message):
    if msg.text in {'+': 1, '-': 2, '*': 3, '/': 4}:
        global type_of_operations
        type_of_operations = {'+': 1, '-': 2, '*': 3, '/': 4}[msg.text]
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите два числа через пробел <Первое> <Второе>')
        bot.register_next_step_handler(msg, take_numbers)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ошибка, введите арифметическое действие <+ - * />')
        bot.register_next_step_handler(msg, take_type_of_operations)


def take_numbers(msg: telebot.types.Message):
    tmp = msg.text.split()
    if len(tmp) == 2 and tmp[0].isdigit() and tmp[1].isdigit():
        itog = calcul(int(tmp[0]), int(tmp[1]), type_of_operations)
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат {itog}')
        bot.send_message(chat_id=msg.from_user.id, text=f'Для продолжения отправьте любое сообщение')
    else:
        bot.send_message(chat_id=msg.from_user.id, text=f'Ввеите два числа через пробел <Первое> <Второе>')
        bot.register_next_step_handler(msg, take_numbers)


def calcul(number_1, number_2, operation):
    if operation == 1:
        result = str(number_1 + number_2)
    elif operation == 2:
        result = str(number_1 - number_2)
    elif operation == 3:
        result = str(number_1 * number_2)
    elif operation == 4:
        result = str(number_1 / number_2)
    else:
        result = None
        print('Действие не поддерживается, вызывайте помощь')

    return result


@bot.message_handler()
def take_message(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text=f'Выберите, с какими числами будем работать?\n1. Рациональные числа\n2. Комплексные числа')
    bot.register_next_step_handler(msg, take_type_number)


print('Бот запущен')

bot.polling()