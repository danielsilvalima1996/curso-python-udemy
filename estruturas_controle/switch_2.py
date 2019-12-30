# -*-coding:utf-8-*-

# minha tentativa


def dias_uteis(dia):
    semana = {
        'domingo': 'Final de Semana',
        'segunda': 'Dia Útil',
        'terca': 'Dia Útil',
        'quarta': 'Dia Útil',
        'quinta': 'Dia Útil',
        'sexta': 'Dia Útil',
        'sabado': 'Final de Semana'
    }
    return semana.get(dia.lower(), '** Dia inválido **')


# resposta professor
def get_tipo_dia(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana'
    }

    return dias.get(dia, '** Dia inválido **')


if __name__ == '__main__':
    # minha tentativa
    # for dia in ('segunda', 'domingo', 'terca', 'sabado'):
    #     print(dias_uteis(dia))

    # resposta professor
    for dia in range(8):
        print(get_tipo_dia(dia))
