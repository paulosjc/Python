lista = []
dados = dict()
cont = 0
idades = []
mulheres = []

while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('ERRO! Por favor, digite apenas M ou F: '))
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    cont += 1
    resp = ' '
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp not in 'SN':
        resp = str(input('ERRO! Responda apenas S ou N: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)

for i in lista:
    for k, v in i.items():
        if k == 'idade':
            idades.append(v)

média = sum(idades) / cont

print(f' - O grupo tem {cont} pessoas')
print(f' - A média de idade é de {média} anos')
print(f' - As mulheres cadastradas foram {mulheres}')
print('Lista das pessoas com idade acima da média:')
for i in lista:
    if i['idade'] >= média:
        print('     ', end='')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
print('-=' * 30)
print('<<< ENCERRADO >>>')
