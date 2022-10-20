# Напишите программу которая принимает на вход число N и выдает последовательность из N членов

NumberN = int(input('Введите число: '))
result = []
for i in range(NumberN):
    result.append((-3)**i)
print(result)