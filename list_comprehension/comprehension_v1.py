# -*- coding: utf-8 -*-

# [ expressão for item in list if condicional ]
dobros = [i * 2 for i in range(1, 11)]
print(dobros)

# Versão "normal"
dobros = []
for i in range(1, 11):
    dobros.append(i * 2)
print(dobros)
