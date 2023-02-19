from time import sleep

lista = list()
dados = list()
alunos = list()
cont = 0


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    dados.append(média)
    alunos.append(dados[:])
    dados.clear()
    cont += 1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break

lista.append(alunos)

print(lista)

print('-=' * 20)
print(f'{"No.":<5}{"NOME":<20}{"MÉDIA":<10}')
print('-' * 35)

for i in range(0, cont):
    print(f'{i:<5}{lista[0][i][0]:<20}{lista[0][i][3]:<10.1f}')

print('-' * 35)

while True:
    resp = int(input('Mostrar nota de qual aluno? (999 interrompe) '))
    if resp == 999:
        sleep(1)
        print('FINALIZANDO...')
        sleep(1)
        break
    print(f'As notas de {lista[0][resp][0]} são {lista[0][resp][1]} e {lista[0][resp][2]}')


