
lista = [1,5,9,8,7,2,4,10,3]
p = 1


def quartil(lista):
    p_index = int(p*len(lista))
    ordenada = sorted(lista)
    tamanho = len(ordenada)
    if p == 2 and tamanho % 2 == 1:
        return ordenada[5]




print(quartil(lista))