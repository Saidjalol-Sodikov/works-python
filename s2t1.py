print('Нахождение факториала от числа n.')
n = int(input('Введите n: '))
i = 0
result = 0
while i<=n:
    result += i
    i +=  1
print(f'{n}!={result}')    
