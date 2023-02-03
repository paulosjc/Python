from datetime import date
lista = []
adultos = []

for c in range(0, 7):
    nasc = int(input('Digite o seu ano de nascimento: '))
    lista.append(nasc)

for c in lista:
    idade = date.today().year - c
    if idade >= 21:
        adultos.append(idade)

print('{} pessoas já atingiram a maioridade'.format(len(adultos)))
print('{} pessoas ainda não atingiram a maioridade'.format(len(lista) - len(adultos)))



