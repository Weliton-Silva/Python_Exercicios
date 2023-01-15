nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Média {:.1f} Aluno Reprovado.'.format(media))
elif media <= 6.9:
    print('Média {:.1f} Aluno de Recuperação.'.format(media))
else:
    print('Média {:.1f} Aluno Aprovado.'.format(media))
