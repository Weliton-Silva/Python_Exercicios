dados = dict()
lista = []
time = list()

while True:
    dados.clear()
    dados["Nome"] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou ? '))
    lista.clear()
    for p in range(partidas):
        lista.append(int(input(f'    Quantos gols na partida {p + 1} ? ')))
    dados["Jogos"] = lista[:]
    dados["Total"] = sum(lista)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*40)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 para parar):  '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca} !')
    else:
        print(f'Levantamento do jogador {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Jogos']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
