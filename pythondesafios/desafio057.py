sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite novamente o seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))




