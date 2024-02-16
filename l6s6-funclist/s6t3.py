def Input_Array ():
    Arr_len = int(input("Введите длину массива: "))
    Array = []
    for i in range(Arr_len):
        Array.append(int(input(f"Введите элемент {i+1}: ")))
    return Array

N = Input_Array()

D = dict()
result = 0

for i in N:
    if i not in D.keys():
        D[i] = 1
    else:
        D[i] += 1
        
for i in D.values():
    result += i//2

print(f"Результат: {result}")