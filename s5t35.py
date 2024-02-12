def is_simple (n):
    kol_del = 0
    for i in range(1,n+1):
        if n%i==0:
            kol_del += 1
    if kol_del > 2:
        return False
    else:
        return True
        
num = 1117
if is_simple(num):
    print('yes')
else:
    print('no')