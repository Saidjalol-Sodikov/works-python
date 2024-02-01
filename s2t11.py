'''
Дано натуральное число A > 1. Определите, 
каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи, выведите 
число -1.
'''
print('Определение порядкового номера числа n из ряда ',
'чисел Фибоначчи.')
n = int(input('Введите n: '))
isFib = False
fib1 = 0
fib2 = 1
fib3 = 1
nNomer = 0

while fib1<=n:
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1+fib2
    nNomer += 1
    if fib1==n:
        isFib = True

if isFib:
    # print(f'φ({nNomer})={n}')
    print(nNomer)
else:
    print(-1)    