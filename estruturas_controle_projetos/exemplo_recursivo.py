def imprimir(maximo, atual):
    # if atual >= maximo:
    #     return
    # print(atual)
    # imprimir(maximo, atual + 1)

    # condicao de parada
    if atual < maximo:
        print(atual)
        imprimir(maximo, atual + 1)


imprimir(990, 1)
