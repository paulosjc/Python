maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa em kg: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O menor peso é de {} kg'.format(maior))
print('O menor peso é de {} kg'.format(menor))

