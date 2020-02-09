#!/usr/bin/python3
from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]
print('sorted', sorted(valores))

print('min', min(valores))
print('max', max(valores))
print('sum', sum(valores))
print('reduce', reduce(add, valores))
print('reversed', list(reversed(valores)))
print('valores', valores)
