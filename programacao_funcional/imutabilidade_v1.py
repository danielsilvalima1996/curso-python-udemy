#!/usr/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce


# português do Brasil
setlocale(LC_ALL, 'pt_BR.UTF-8')

# Listar todos os meses do ano com 31 dias
meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
# transformar em nome de meses
meses_nome = map(lambda mes: month_name[mes], meses_31)
# juntar os meses
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                      meses_nome, 'Meses com 31 dias:')

print(juntar_meses)

# tudo em uma só expressão
print(
    reduce(
        lambda todos, nome_mes: f'{todos}\n - {nome_mes}',
        map(
            lambda mes: month_name[mes],
            filter(
                lambda mes: mdays[mes] == 31,
                range(1, 13)
            )
        ),
        'Meses com 31 dias:'
    )
)
