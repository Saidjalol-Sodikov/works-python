'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

Пример
На входе:
var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
На выходе:
3 5
'''

#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов 
#и вызвать функцию
#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически 
#подставит разные значения аргументов и вызовет функцию для проверки

var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

# Введите ваше решение ниже

var2_int = {int(i) for i in var2.split()}
var3_int = {int(i) for i in var3.split()}

result = var2_int.intersection(var3_int)
print(*sorted(result))

# Эталонное решение
mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')