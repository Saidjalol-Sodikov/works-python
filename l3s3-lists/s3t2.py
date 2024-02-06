'''
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.
'''

inputArr = [1, 2, 3, 4, 5]

# def move(lst, steps):
#     if steps > 0:
#         for i in range(steps):
#             lst.insert(0, lst.pop())
 
# nums = [1, 2, 3, 4, 5]
# print(nums)
 
# move(nums, 2)
# print(nums)

for i in range(5):
    temp = inputArr.pop()
    inputArr = inputArr.insert(0,temp)
print(inputArr)