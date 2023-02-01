from datetime import date

ano_nasc = int(input('Qual o ano de seu nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    print('Modalidade: \033[33mMIRIM')
elif idade >= 10 and idade <= 14:
    print('Modalidade: \033[32mINFANTIL')
elif idade >= 15 and idade <= 19:
    print('Modalidade: \033[34mJÚNIOR')
elif idade == 20:
    print('Modalidade: \033[36mSÊNIOR')
else:
    print('Modalidade: \033[35mMASTER')
