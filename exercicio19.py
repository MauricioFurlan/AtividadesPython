#exercucui19
import math

lista1 = [1,2,8,9,3,4,6]

media = sum(lista1)/len(lista1)
amplitude = max(lista1) - min(lista1)

response = float(0)

for i in lista1:
    response = response + (i-media)**2

variancia = response/len(lista1)
desvio = math.sqrt(variancia)
print(f"A dispersão da lista esta em: {desvio}")