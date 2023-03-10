from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')

print('-=' * 30)
ano = int(input('Em que ano você nasceu? '))
voto(ano)
