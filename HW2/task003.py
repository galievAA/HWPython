# Задайте список из n чисел последовательности (1+1/n)^n
# Выведитте на экран саму последовательность и сумму элеементов этой последовательности 
# (для проверки сумма для 4 элементов = 9,06 (примерно))

# n = int(input('Введите число: ')) 

# def Number(n):

#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(Number(n))
# print(round(sum(Number(n))))


n = int(input('Введите число N: '))

f = 1
factorial = []
for i in range (1, n + 1):
    f = (1 + 1/i) ** i
    factorial.append(f)
print(factorial)
print(sum(factorial))


