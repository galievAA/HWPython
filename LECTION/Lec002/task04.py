# Напишите программу в которой пользователи будут задавать две 
# строки а программа определять колличество вхождения одной строки в другую
# string= 'строка любая'
# subString = 'wen'


counter = 0
string= 'wen строка wen любая wen '
subString = 'wen'
print(string[0:10000]) # индекс в строке от и до 

for i in range (len(string)):
    if string [i:i+len(subString)] == subString:
        counter += 1