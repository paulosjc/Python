times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
cincoprimeiros = times[:5]
últimosquatro = times[16:]
últimosquatro2 = times[-4:]

print('-=-' * 30)
print(f'Os cinco primeiros colocados são {cincoprimeiros}')
print('-=-' * 30)
print(f'Os últimos quatro colocados são {últimosquatro}')
print('-=-' * 30)
print(f'Os últimos quatro colocados são {últimosquatro2}')
print('-=-' * 30)
print(f'Em ordem alfabética a lista fica assim: {sorted(times)}')
print('-=-' * 30)
print(f'O Corinthians está na {times.index("Corinthians") + 1}ª posição')
print('-=-' * 30)
