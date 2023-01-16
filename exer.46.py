from time import sleep

print('\033[33m=-\033[m' * 20)
print('\033[33m{:=^40}'.format('\033[31m CONTAGEM REGRESSIVA PARA FOGOS \033[m'))
print('\033[33m=-\033[m' * 20)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('💥💥💥  \033[31mExplosão !\033[m 💥💥💥')
