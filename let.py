'''
Требуется вычислить, сколько раз встречается 
некоторое число k в массиве list_1.
Найдите количество и выведите его.

Пример:
list_1 = [1, 2, 3, 4, 5] 
k = 3 
# 1
'''
"""
При отправке кода на Выполнение раскомментируйте 
строку ниже, чтобы задать значения `list_1` и `k`
При отправке решения на Проверку закомментируйте 
эту строку обратно - система автоматически 
подставит разные значения `list_1` и `k` для проверки
"""

list_1 = [1, 2, 3, 4, 5, 1, 3, 3]
k = 3

# Введите ваше решение ниже

count_k = list_1.count(k)
print(count_k)

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)
