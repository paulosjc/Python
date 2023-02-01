nome = str(input('Qual é o seu nome? '))

if nome == 'Paulo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'João' or nome == 'José' or nome == 'Maria':
    print('O seu nome é bastante popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('O seu nome é bem normal...')
print('Tenha um bom dia, {}!'.format(nome))
