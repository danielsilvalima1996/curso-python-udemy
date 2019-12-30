from random import randint
randint(0, 9)

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número secreto: '))

print('O número secreto {} foi encontrado!'.format(numero_informado))
