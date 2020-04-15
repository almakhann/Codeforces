text = input()
text = text.lower()

vowels = 'aoyeui'
string = ''

for i in text:
    if i not in vowels:
        string += '.' + i

print(string)
