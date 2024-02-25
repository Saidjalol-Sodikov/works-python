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

Sample Input 1:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n
Sample Output 1:
1 2 3

Sample Input 2:
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
Sample Output 2:
1 2 7 8
'''
keyword = 'anton'

fridge_dates = []
fridge_dates.append('6')
fridge_dates.append('222anton456')
fridge_dates.append('a1n1t1o1n1')
fridge_dates.append('0000a0000n00t00000o000000n')
fridge_dates.append('osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen')
fridge_dates.append('richard')
fridge_dates.append('antooooooooooooooooooooooooooooooooooooooooon')

infected_fridges_num = []

def Have_num_more (number, num_list):
    for i in num_list:
        if number<i:
            return True
    return False

fridges_key_letters_indexes = dict()

for i in range(len(fridge_dates)):
    for j in range(len(fridge_dates[i])):
        if fridge_dates[i][j] in keyword:
            temp_list = fridges_key_letters_indexes[i] + [j]
            fridges_key_letters_indexes[i] = temp_list