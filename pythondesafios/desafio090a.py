aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
aluno['Situação'] = ' '
if aluno['Média'] >= 5.0:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print(f'O nome é {aluno["Nome"]}')
print(f'Média é igual a {aluno["Média"]}')
print(f'Situação é igual a {aluno["Situação"]}')