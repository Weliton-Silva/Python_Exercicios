from time import sleep

print('=~' * 20)
sleep(1)
print('            T A B U A D A     ')
sleep(1)
print('=~' * 20)
sleep(1)
n1 = int(input('Digite o número que gostaria de saber a tabuada: '))
n2 = 11
for c in range(1, 11):
    resp = n1 * c
    print('{} x {:2} = {}'.format(n1, c, resp))
    sleep(1)
print('Fim da Tabuada.')
