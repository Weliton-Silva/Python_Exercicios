aluno = {}
aluno['nome'] = str(input('Aluno: '))
aluno['media'] = float(input(f'Qual a média do {(aluno)["nome"]}: '))
for a, m in aluno.items():
    print(f'{a} é igual a {m}')
print('=-'*20)
if aluno['media'] < 7:
    print(f'{aluno["nome"]} esta Reprovado !')
else:
    print(f'{aluno["nome"]} foi aprovado ! Parabens.')
