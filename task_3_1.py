
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


def num_translate(num=None):
    for key, val in dict_num.items():
        if num == key:
            return val
        elif num == val:
            return key

print(num_translate(str(input())))
