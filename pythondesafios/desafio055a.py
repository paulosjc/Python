lista = []

for c in range(0, 5):
    peso = float(input('Qual é o seu peso em kg? '))
    lista.append(peso)

print('O maior peso é de {}'.format(max(lista)))
print('O menor peso é de {}'.format(min(lista)))
