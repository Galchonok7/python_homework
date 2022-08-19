
dict_num = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(num=None):
    for key, val in dict_num.items():
        if num == key:
            return val
        elif num == val:
            return key
        if num == key.title():
            return val.title()
        elif num == val.title():
            return key.title()

print(num_translate_adv(input()))

