def is_simple (n):
    kol_del = 0
    for i in range(1,n+1):
        if n%i==0:
            kol_del += 1
    if kol_del > 2:
        return False
    else:
        return True

def is_simple_r (n, d = 2):
    if d*d > n:
        return True
    elif n%d==0:
        return False
    return is_simple_r (n, d+1)

while True:
    num = int(input('Ведите число:'))
    if is_simple(num):
        print('yes')
    else:
        print('no')
    if is_simple_r(num):
        print('yes')
    else:
        print('no')
    