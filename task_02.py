'''
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()
'''

smth_list = []
count = int(input('Input count of list elements: '))
for i in range(0,count):
    smth_list.append(input('input value of list element: '))

print(smth_list)
for i in range(0,count):
    if i%2>0:
        smth_list[i-1], smth_list[i] = smth_list[i], smth_list[i-1]

print(smth_list)
