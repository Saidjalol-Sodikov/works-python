'''
Возвращает количество гласных в заданной строке.
Мы будем считать a, e, i, o, u гласными для этой Ката (но не y).
Входная строка будет состоять только из строчных букв и/или пробелов.
'''
#-------------------------
def get_count_my(sentence):
    return(sentence.count('a')+sentence.count('e')+sentence.count('i')+sentence.count('o')+sentence.count('u'))
#-------------------------
def get_count_sm(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
#-------------------------
def get_count_pr(s):
    return sum(c in 'aeiou' for c in s)
#-------------------------

print(get_count_my('qwertyuiop'))
print(get_count_pr('qwertyuiop'))
print(get_count_sm('qwertyuiop'))