#!/usr/bin/python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    # leitura do argumento via linha de comando
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo', area)
