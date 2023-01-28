import random

a1 = str(input('Digite o nome de um aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

lista = ['Paulo', 'João', 'Gustavo', 'Jonas']
lista2 = [a1, a2, a3, a4]

ae = random.choice(lista)
print('O aluno escolhido é {}.'.format(ae))
