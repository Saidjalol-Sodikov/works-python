'''
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть 
умных холодильников. Теперь он использует их в качестве серверов 
"Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные 
холодильники.
Для каждого холодильника существует строка с данными, состоящая из 
строчных букв и цифр, и если в ней присутствует слово "anton" 
(необязательно рядом стоящие буквы, главное наличие последовательности 
букв), то холодильник заражен и нужно вывести номер холодильника, 
нумерация начинается с единицы.

Формат входных данных
В первой строке подаётся число n – количество холодильников. В последующих 
строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
5 до 100 символов.
Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если 
таких холодильников нет, ничего выводить не нужно.

Sample Input:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
Sample Output:
1, 2, 3, 8, 9, 14, 15
'''
keyword = 'anton'

fridge_dates = []
fridge_dates.append('6')
fridge_dates.append('222anton456')
fridge_dates.append('a1n1t1o1n1')
fridge_dates.append('0000a0000n00t00000o000000n')
fridge_dates.append('gylfole')
fridge_dates.append('richard')
fridge_dates.append('ant0n')
fridge_dates.append('9')
fridge_dates.append('osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen')
fridge_dates.append('anton')
fridge_dates.append('aoooooooooontooooo')
fridge_dates.append('elelelelelelelelelel')
fridge_dates.append('ntoneeee')
fridge_dates.append('tonee')
fridge_dates.append('253235235a5323352n25235352t253523523235oo235523523523n')
fridge_dates.append('antoooooooooooooooooooooooooooooooooooooooooooooooooooon')
fridge_dates.append('unton')

infected_fridges_num = []

def cheking (string1, string2):
    if len(string1)==0 and len(string2)>0:
        return False
    if len(string2)==0:
        return True
    if string1[0]!=string2[0]:
        return cheking (string1[1:],string2)
    else:
        return cheking (string1[1:],string2[1:])

for i in range(len(fridge_dates)):
    if cheking(fridge_dates[i],keyword):
        infected_fridges_num.append(i)
    
print(*infected_fridges_num)