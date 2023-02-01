from datetime import date

ano_nasc = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade < 18:
    print('Você ainda vai se alistar no serviço militar. Faltam {} anos para chegar a época de alistamento.'.format(18 - idade))
elif idade == 18:
    print('Você está na idade de alistamento. ALISTE-SE JÁ!')
else:
    print('Você passou da idade de alistamento. Já se passaram {} anos.'.format(idade - 18))
