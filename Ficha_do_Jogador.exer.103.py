def ficha(jogo='<desconhecido>', gols=0):
    print(f'O jogador {jogo} fez {gols} gol(s) no campeonado.')


# Programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Números de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
    