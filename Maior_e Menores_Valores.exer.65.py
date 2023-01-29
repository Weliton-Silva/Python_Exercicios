conti = 'S'
n1 = cont = media = maior = soma = 0

menor = 0
while not conti == 'N':
    n1 = int(input('Digite um valor inteiro: '))
    cont += 1
    soma += n1
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    conti = str(input('Deseja Continuar [S/N] ?')).upper().strip()[0]
print('=-'*20)
media = soma / cont
print('Final do programa.')
print('=-'*20)
print('''a Média de valores Digitados foi {:.2f}
O maior valor Digitado foi {}
O menor valor foi {}'''.format(media, maior, menor))
