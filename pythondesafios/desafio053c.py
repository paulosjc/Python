frase = str(input('Digite uma frase qualquer sem acentos: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')



