list = [1,2,3,4,5,6]

def listamediana(list):
    tamanho = len(list)
    listaordenada = sorted(list)
    posicao = tamanho // 2
    if tamanho %2 == 1:
        return listaordenada[posicao]
    else:
        return sum(listaordenada[posicao - 1:posicao + 1])/2
print(listamediana(list))