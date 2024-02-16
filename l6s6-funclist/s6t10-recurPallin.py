def pallindrom(stroka):
    if len(stroka) <=1:
        return True
    if stroka[0]!=stroka[-1]:
        return False    
    return pallindrom(stroka[1:-1])
    
print (pallindrom("qwewq")) 