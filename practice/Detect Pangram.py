'''
Панграмма – это предложение, которое содержит каждую букву алфавита 
хотя бы один раз. Например, предложение «Быстрая бурая лиса прыгает 
через ленивую собаку» является панграммой, поскольку в нем хотя бы 
один раз используются буквы AZ (регистр не имеет значения).
Учитывая строку, определите, является ли она панграммой. Возвращайте 
True, если это так, и False, если нет. Не обращайте внимания на цифры 
и знаки препинания.
'''

#--------------------------
def is_pangram_my(s, alphabet = 'tyghbnrufjvmcdkeiwoslxzpaq'):
    s = s.lower()
    if len(alphabet) == 0:
        return True
    if alphabet[0] in s:
        return is_pangram_my(s, alphabet[1:])
    return False
#--------------------------
def is_pangram_sm(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
#--------------------------
import string
def is_pangram_pr(s):
    return set(string.ascii_lowercase).issubset(s.lower())

print(is_pangram_my('The quick brown fox jumps over the lazy dog'))
print(is_pangram_pr('The quick brown fox jumps over the lazy dog'))
print(is_pangram_sm('The quick brown fox jumps over the lazy dog'))