# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

with open('file_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('file_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('file_1.txt','r') as file:
    file_1 = file.readline()
    list_of_file_1 = file_1.split()

with open('file_2.txt','r') as file:
    file_2 = file.readline()
    list_of_file_2 = file_2.split()

print(f'{list_of_file_1} + {list_of_file_2}')
sum_file = list_of_file_1 + list_of_file_2

with open('sum_file.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_file_1} + {list_of_file_2}')
