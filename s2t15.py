''' 
Иван Васильевич пришел на рынок и решил купить два арбуза:
один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз потяжелей, 
а для тещи полегче. Но вот незадача: 
арбузов слишком много и он не знает как же выбрать 
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. 
Вторая строка содержит N чисел, записанных на новой 
строчке каждое. Здесь каждое число – это масса 
соответствующего арбуза 

Input: 5 -> 5 1 6 5 9 
Output: 1 9
'''

massArr = [5, 1, 6, 5, 9]

maxMass = massArr[0]
minMass = massArr[0]

for i in massArr:
    if i < minMass:
        minMass = i
    if i > maxMass:
        maxMass = i
print(minMass,' ',maxMass)        

#print(min(massArr),' ',max(massArr))