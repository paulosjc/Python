# Escopo de variáveis

def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
# print(f'B fora vale {b}')
# print(f'C fora vale {c}')
# Estas duas últimas linhas resultam em erro pois "b" e "c"
# tem escopo local (apenas dentro da função), enquanto "a" tem escopo global.
