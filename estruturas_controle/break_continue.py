#!/usr/bin/python3

for x in range(1, 11):
    if x % 2 == 0:
        # continue interrompe e vai para o próximo
        continue
    print(x)

for x in range(1, 11):
    if x == 5:
        # o break saí do laço
        break
    print(x)

print('Fim')
