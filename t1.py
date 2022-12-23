# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

value = input('Input number: ')
my_list = list(value)
if '.' in my_list:
    my_list.remove('.')

sum = 0
for item in my_list:
    sum += int(item)
print(sum)
