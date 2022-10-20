# Реализуйте алгоритм перемешивания списка, без использования встроеных методов 
# (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random


import random

def get_list(n, left, right):
    return [random.randint(left, right) for i in range(n)]

def list(list):
    return random.shuffle(list)

n = 6
left = -80
right = 70

mylist = get_list(n, left, right)
print(mylist)
list(mylist)
print(mylist)

