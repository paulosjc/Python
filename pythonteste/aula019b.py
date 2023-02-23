brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['UF'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

