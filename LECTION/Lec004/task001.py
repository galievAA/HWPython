# создайте в файле считайте из файла строку из набора чисел напишите 
# программу которая покажет большее и меньшее число 
# в качестве символа разделителя используйте пробел 
import random

size = random.randint(5,10)

string = ''

for _ in range(size):
    string = f'{random.randint(1,9999)}'

print(string)
