from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário R$: '))
    dados['aposentadoria'] = dados['contratação'] + 35 - nasc
print('-=' * 30)
print(dados)

for k, v in dados.items():
    print(f'{k} tem o valor {v}')
