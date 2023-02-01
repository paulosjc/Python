r1 = float(input('Primeiro lado: '))
r2 = float(input('Segundo lado: '))
r3 = float(input('Terceiro lado: '))

lista = [r1, r2, r3]
i = lista.index(max(lista))
maior = lista[i]
print(lista)
lista.pop(i)
print(i)
print(lista)
soma = sum(lista)
sub = abs(lista[0] - lista[1])
print(soma)
print(sub)

if maior < soma and maior > sub:
    print('Este triângulo pode ser construído.')
else:
    print('Nenhum triângulo pode ser construído com estas medidas.')

