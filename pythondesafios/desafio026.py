frase = str(input('Digite uma frase: ')).upper().strip()
print(frase.count('A'))
print('A primeira ocorrência da letra A acontece na posição {}'.format(frase.find('A') + 1))
print('A última ocorrência da letra A acontece na posição {}'.format(frase.rfind('A') + 1))
