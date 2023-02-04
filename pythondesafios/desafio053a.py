frase = str(input('Digite uma frase qualquer sem pontuação no final: ')).lower().strip()

frase_sem_espaços = frase.replace(' ', '')
frase_sem_espaços_invertida = frase_sem_espaços[::-1]
print(frase)
print(frase_sem_espaços)
print(frase_sem_espaços_invertida)

if frase_sem_espaços == frase_sem_espaços_invertida:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')

'''Exemplos de palíndromos:
A sacada da casa
Apos a sopa
Anotaram a data da maratona
A torre da derrota
O lobo ama o bolo'''
