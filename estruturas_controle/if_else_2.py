#!/usr/bin/python3
def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):  # range na ultima posicao não pega o ultimo valor, 65 a 99
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'idade inválida'


if __name__ == "__main__":
    for idade in (17, 35, 87, 113, -2):
        print(f'{idade}: {faixa_etaria(idade)}')
