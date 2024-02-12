'''
Напишите рекурсивную функцию sum(a, b), возвращающую 
сумму двух целых неотрицательных чисел. Из всех 
арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
Функция не должна ничего выводить, только возвращать значение.

Пример:
sum(2, 2)
# 4
'''
"""
При отправке кода на Выполнение раскомментируйте строку ниже, 
чтобы задать значения переменных `a` и `b`  и вызвать функцию
При отправке решения на Проверку закомментируйте эти строки 
обратно - система автоматически подставит разные значения 
`a` и `b` и сама вызовет функцию для проверки
"""
# Введите ваше решение ниже

def sum(a,b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else: 
        return sum(a+1,b-1)

a = 3
b = 5
print(sum(a=1, b=3))