
list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
element_list1 = 0

while element_list1 < len(list1):
    if list1[element_list1].isdigit():
        if (int(list1[element_list1]) // 10 == 0):
            list1[element_list1] = '0' + list1[element_list1]
        list1.insert(element_list1, '"')
        list1.insert(element_list1 + 2, '"')
        element_list1 = element_list1 + 2
    if list1[element_list1] == '+5':
        list1[element_list1] = '+05'
        list1.insert(element_list1, '"')
        list1.insert(element_list1 + 2, '"')
        element_list1 = element_list1 + 2
    element_list1 = element_list1 + 1
    print(list1)
mess_str = ' '.join(list1)
print(mess_str)