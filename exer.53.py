frase = str(input('Digite uma Frase: '))
frase = frase.upper()
frase2 = frase[::-1]
print(frase)
print(frase2)
if frase == frase2[::-1]:
    print('A Frase Formara um Palindromo')
else:
    print('A frase não formara um palindromo')
