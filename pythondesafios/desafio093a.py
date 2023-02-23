dados = dict()
gols = list()
dados['nome'] = str(input('Nome do Jogador: '))
totpart = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(0, totpart):
    gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
dados['gols'] = gols.copy()
dados['total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {totpart} partidas.')
for i in range(0, len(gols)):
    print(f'    => Na partida {i + 1}, fez {gols[i]}.')
print(f'Foi um total de {dados["total"]} gols.')
