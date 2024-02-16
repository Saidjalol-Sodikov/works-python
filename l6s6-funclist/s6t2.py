def Input_Array ():
    Arr_len = int(input("Введите длину массива: "))
    Array = []
    for i in range(Arr_len):
        Array.append(int(input(f"Введите элемент {i+1}: ")))
    return Array

N = Input_Array()
result = 0

for i in range(1,len(N)-1):
    if N[i-1]<N[i] and N[i+1]<N[i]:
        result +=1 

print(f"Результат: {result}")