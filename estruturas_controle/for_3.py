#!/usr/bin/python3

produto = {
    'nome': 'Caneta Chic',
    'preco': 14.99,
    'importada': True,
    'estoque': 793
}

# é redundante colocar o .keys(), sem funciona as chaves
for chave in produto.keys() or produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)
