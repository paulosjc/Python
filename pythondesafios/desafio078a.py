valores = list()
for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

pos_maior = valores.index(max(valores))
pos_menor = valores.index(min(valores))

print(valores)
print(sorted(valores))
print(f'O maior valor digitado é {max(valores)} na posição {pos_maior}')
print(f'O menor valor digitado é {min(valores)} na posição {pos_menor}')