inputString = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# inputString = inputString.lower()
# inputString = inputString.replace('.',' ').replace('\'',' ')
# inputString = inputString.replace('\'',' ')
# print(inputString)
words = set(inputString.lower().replace('.',' ').replace("'",' ').split())

print(len(words))