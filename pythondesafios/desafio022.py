nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
nome_semespaços = nome.replace(' ', '')
print('O seu nome sem espaços fica: {}'.format(nome_semespaços))
print('O seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
nome_splitted = nome.split()
print('O seu primeiro nome é {} e tem {} letras.'.format(nome_splitted[0], len(nome_splitted[0])))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
