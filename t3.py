# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int
import random

my_list = []
for i in range(50):
    my_list.append(i)

print(my_list)

for i in range(len(my_list)):
    randI = random.randint(i, len(my_list)-1)
    temp = my_list[i]
    my_list[i] = my_list[randI]
    my_list[randI] = temp

print(my_list)