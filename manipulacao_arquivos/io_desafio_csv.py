#!/usr/bin/python3
# tentativa Daniel, realizada com sucesso
# import csv


# with open('desafio-ibge.csv', encoding='latin1') as entrada:
#     for item in csv.reader(entrada):
#         # print(type(item))
#         print('{8}: {3}'.format(*item))

# Resposta professor

import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
