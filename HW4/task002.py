# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

number = int (input('Введите размер списка: '))
i = 2 
lst = []
old = number
while i <= number:
    if number % i == 0:
        lst.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} указаны в списке: {lst}")
