def print_invers (n):
    if len(n) < 1:
        return 
    print (n[-1], end="")
    return (print_invers (n[:(len(n))-1]))

print_invers("1234567890")
