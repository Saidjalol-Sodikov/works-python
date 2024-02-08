inputString = 'a a a b c a a d c d d'

inputString = inputString.split()
printDict = {}
printString = ""


for i in inputString:
    if i in printDict.keys():
        printDict[i] += 1
        printString += f'{i}_{str(printDict[i])} '
    else:
        printDict[i] = 0
        printString += f'{i} '
    
        
print(printString)        