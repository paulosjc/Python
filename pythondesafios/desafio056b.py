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

sub_20 = []
m_sub_20 = []

for c in listaidade:
    if c < 20:
        sub_20.append(listaidade.index(c))

for c in sub_20:
    if listasexo[c] == 'F':
        m_sub_20.append(c)

print('Há {} mulheres com menos de 20 anos'.format(len(m_sub_20)))
