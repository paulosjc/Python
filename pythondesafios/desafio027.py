nome = str(input('Digite o seu nome completo: '))
nome2 = nome.split()
print(len(nome2))
print('Primeiro nome: {}'.format(nome2[0]))
print('Último nome: {}'.format(nome2[len(nome2) - 1]))

