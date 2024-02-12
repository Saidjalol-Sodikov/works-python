def show_fib (n):
    if n in [1,2]:
        return 1
    return show_fib (n-1) + show_fib (n-2)
    
input_int = int(input('Введите n: '))
print(show_fib(input_int))