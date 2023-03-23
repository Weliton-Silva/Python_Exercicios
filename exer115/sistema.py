from exer115.libe.interface import *
from time import sleep

while True:
    resposta = menu(['opc01', 'opc02', 'opc03', 'Super opção'])
    if resposta == 1:
        cabecalho('opção 1')
    elif resposta == 2:
        cabecalho('opção 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)
