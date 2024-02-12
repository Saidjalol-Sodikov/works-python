def good_to_bad (n):
    if n in [1,2,3]:
        return n
    if n in [4,5]:
        return 1
        
import random

num_1 = int(input('Количество оценок: '))
arr = []
for i in range(num_1): 
    arr.append(random. randint(1,5))
print (arr)
for i in range(len(arr)):
    arr[i] = good_to_bad(arr[i])
print (arr)   