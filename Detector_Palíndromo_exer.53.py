frase = str(input('Digite uma Frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('Não formará um Palíndromo')
