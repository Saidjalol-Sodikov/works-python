'''
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''

inputList = [1, 1, 2, 0, -1, 3, 4, 4]
diffNumList = []

for i in inputList:
    if i not in diffNumList:
        diffNumList.append(i)


print(len(diffNumList))