frase = str(input('Digite sua frase ou expressão matemática: '))

if frase.count('(') == frase.count(')'):
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada...')