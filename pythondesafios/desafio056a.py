listanome = []
listaidade = []
listasexo = []
i = 0

for c in range(0, 4):
    if i <= 3:
        nome = str(input('Qual é o seu nome? '))
        idade = int(input('Qual é a sua idade? '))
        sexo = str(input('Qual é o seu gênero? '))
        listanome.append(nome)
        listaidade.append(idade)
        listasexo.append(sexo)
        i += i

print(listanome)
print(listaidade)
print(listasexo)
média_idades = sum(listaidade) / len(listaidade)
print('A média das idades é de {}'.format(média_idades))

idade_max = listaidade.index(max(listaidade))
print(idade_max)

if listasexo[idade_max] == 'M':
    print('O homem mais velho tem {} anos.'.format(listaidade[idade_max]))

lista_menor_20 = []

for c in listaidade:
    if c < 20:
        lista_menor_20.append(listaidade.index(c))

print(lista_menor_20)
mulheres_abaixo_20 = []

for c in lista_menor_20:
    if listasexo[c] == 'F':
        mulheres_abaixo_20.append(listanome[c])

print(mulheres_abaixo_20)
print('São {} mulheres com menos de 20 anos.'.format(len(mulheres_abaixo_20)))
sub_20 = []
for c in listaidade:
    if c < 20:
        sub_20.append(c)

print(len(sub_20))
