#!/usr/bin/python3


def nota_conceito(valor):
    nota = float(valor)
    conceito: str = ''
    if nota > 10:
        conceito = 'Nota inválida'
    elif nota >= 9.1:
        conceito = 'A'
    elif nota >= 8.1:
        conceito = 'A-'
    elif nota >= 7.1:
        conceito = 'B'
    elif nota >= 6.1:
        conceito = 'B-'
    elif nota >= 5.1:
        conceito = 'C'
    elif nota >= 4.1:
        conceito = 'C-'
    elif nota >= 3.1:
        conceito = 'D'
    elif nota >= 2.1:
        conceito = 'D-'
    elif nota >= 1.1:
        conceito = 'E'
    elif nota >= 0:
        conceito = 'E-'
    else:
        conceito = 'Nota inválida'
    return conceito


if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)
