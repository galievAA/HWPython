# <Задание 2>
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
from random import randint as rI

number = int(input('Введите размер списка: '))

mylist = []

for i in range(number):
    mylist.apped(rI(-10,10))
print(mylist)

listLenght = len(mylist)

mylist1 = []
for i in range(listLenght // 2 + 1):
    element = mylist[i] * mylist[listLenght - i - 1]
    mylist1.apped(element)
    
print(mylist1)
print(mylist1)