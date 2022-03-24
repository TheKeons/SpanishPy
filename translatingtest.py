text = 'si a == 10: brub()'
letters = []
tempword = ''
spaces = []
parenthesis = []

splittext = text.split(' ')

for i, letter in enumerate(text):
    if letter == ' ':
        spaces.append(i)
    elif letter == '(':
        parenthesis.append(i)
print(spaces)
print(parenthesis)


for i, a in enumerate(splittext):
    splittext[i] = splittext[i].split('(')
print(splittext)

