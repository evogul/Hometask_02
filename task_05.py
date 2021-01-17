'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
'''

# my_list = [7, 5, 3, 3, 2]
# num = int(input('input num: '))
# while num>0:
#     my_list.append(num)
#     my_list.sort(reverse=True)
#
#     print(my_list)
#     num = int(input('input num: '))

my_list = [7, 5, 3, 3, 2]
num = int(input('input num: '))
while num>0:
     if my_list.count(num)>0:                                       #если такой балл найден в списке,
         my_list.insert(my_list.index(num)+my_list.count(num),num)  #вставляем его последним из таких же
     elif num>my_list[0]:                                           #если балл больше, чем первый в списке
        my_list.insert(0,num)                                       #вставляем его в начало списка
     else:
        f_found = False
        for i in range(num,0,-1):                                   #перебор баллов в меньшую сторону от введенного
            if my_list.count(i) > 0:                                #если найден в списке
                my_list.insert(my_list.index(i), num)               #добавляем введенный перед ним
                f_found = True
                break
        if f_found == False:                                        #если ничего не найдено
            my_list.append(num)                                     #добавляем в конец списка
     print(my_list)
     num = int(input('input num: '))