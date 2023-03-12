def leiaInt(msg):
    try:
        a = float(input(msg))
    except (ValueError, TypeError, ZeroDivisionError, KeyboardInterrupt):
        print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
        a = float(input(msg))
    return a


def leiaFloat(msg):
    try:
        b = float(input(msg))
    except (ValueError, TypeError, ZeroDivisionError, KeyboardInterrupt):
        print('\033[0;31mERRO: Digite um número real válido.\033[0m')
        b = float(input(msg))
    return b


# Programa principal
a = leiaInt('Digite um Inteiro: ')
b = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {a} e o real foi {b}')