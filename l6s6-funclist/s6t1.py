# N = [3,1,3,4,2,4,12]
# M = [4,15,43,1,15,1]

def Input_Array ():
    Arr_len = int(input("Введите длину первого массива: "))
    Array = []
    for i in range(Arr_len):
        Array.append(int(input(f"Введите элемент {i+1}: ")))
    return Array

N = Input_Array()
M = Input_Array()

R = []

for i in N:
    if i not in M:
        R.append(i)
        
print(f"Результат: {R}")