'''
Напишите функцию, которая принимает на вход целое число и 
возвращает количество битов, равных единице в двоичном 
представлении этого числа. Вы можете гарантировать, что 
ввод неотрицательен.
Пример : двоичное представление 1234is , поэтому в этом 
случае 10011010010функция должна вернуть результат.5
'''
#--------------------------
def to_make_a_bit(num_in_10, str_bit=''):
    if num_in_10==0:
        str_bit = '0' + str_bit
        return str_bit
    if num_in_10==1:
        str_bit = '1' + str_bit
        return str_bit
    if num_in_10%2==1:
        str_bit = ('1') + str_bit
    else:
        str_bit = ('0') + str_bit
    return to_make_a_bit(num_in_10//2,str_bit)

def count_bits_my(n):
    n = to_make_a_bit(n)
    return n.count('1')
#--------------------------
def count_bits_pr(n):
    return bin(n).count("1")
#--------------------------
def count_bits_sm(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total
#--------------------------
print(count_bits_my(0))
print(count_bits_pr(0))
print(count_bits_sm(0))
