# <Задание 3>
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform as uI
from random import uniform as rI
from random import Decimal

number = int (input('Р’РІРµРґРёС‚Рµ СЂР°Р·РјРµСЂ СЃРїРёСЃРєР°: '))
myList = []
for i in range(number):
    coef = rI(1,5)
    number = Decimal(f'{round(uI(-10,10), coef}')
    myList.append(number)
    
numList = []
mantissa = []

for num in myList:
    numList.append(float(num))
    if abs(num) - int(abs(num)) != 0.0:
        mantissa.append(abs(num) - abs(int(num)))
        
print (numList)
print(f'РњР°РєСЃРёРјР°Р»СЊРЅР°СЏ {max(mantissa)} Рё РјРёРЅРёРјР°Р»СЊРЅР°СЏ {min(mantissa)} РјР°РЅС‚РёСЃСЃС‹')
print(f'Р Р°Р·РЅРёС†Р° РјР°РЅС‚РёСЃСЃ {max(mantissa) - min(mantissa)}')