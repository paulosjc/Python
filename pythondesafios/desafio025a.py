nome = str(input('Qual é o seu nome completo? ')).upper().strip()

print('SILVA' in nome)

if 'SILVA' in nome:
    print('O {} possui Silva no nome.'.format(nome))
else:
    print('O {} não possui Silva no nome'.format(nome))
