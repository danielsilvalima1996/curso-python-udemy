# -*-coding:utf-8-*-
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim')
"""
Função sortear_numero entre 1 e 6
For com range 1 a 6
se numero impar continue
se o numero par e igual ao valor sorteado
pela funcao dados imprimir 'acertou!' e depois chamar o break
se não acertar chamar o else ... print('nao acertou o numero!')
"""
from random import randint


def sortear_dado():
    return randint(1, 6)


for numero in range(1, 7):
    if numero % 2 == 1:
        continue

    if numero == sortear_dado():
        print('Acertou!')
        break
else:
    print('Não acertou o número')
