# Funções - Parte 1

def lin():
    print('-' * 30)


# Programa principal
lin()
print('        CURSO EM VÍDEO')
lin()
print('        APRENDA PYTHON')
lin()
print('         PAULO RENATO')
lin()


def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


título('        CURSO EM VÍDEO')
título('        APRENDA PYTHON')
título('         PAULO RENATO')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A + B = {s}')


# Programa principal
soma(4, 5)
soma(b=3, a=2)
soma(a=1, b=6)

# soma(b=3, 4) -> Não funciona, pois o Python não
# reconhece o segundo parâmetro como sendo o parâmetro faltante (neste caso, a).
# Ou explicita-se as variáveis ou os valores são colocados na ordem esperada,
# sem especificar quem é quem...
