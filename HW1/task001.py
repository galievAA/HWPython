# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Введите чило дня недели  '))

if 0 < day < 8:
    if day == 6 or day == 7:
        print('Выходной')
    else:
        print('Будний день')
else:
    print('Нет такого дня недели')
# from calendar import day_name


# match day_name:
#     case 1:
#         print('понедельник')
#     case 2:
#         print('Вторник')
#     case 3:
#         print('среда')
#     case 4:
#         print('четверг')
#     case 5:
#         print('пятница')
#     case 6:
#         print('суббота')
#     case 7:
#         print('воскресенье')
#     case _ :
#         print("Нет такого дня недели")