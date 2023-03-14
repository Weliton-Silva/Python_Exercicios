def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de varios alunos.
    :param n:uma ou mais notas dos alunos (aceita varias)
    :param sit:valor opcional, indicando se deve ou não adicionar a situação.
    :return:dicionario com varias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
