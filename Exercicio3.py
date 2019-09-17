import math

metroq = float(input("Digite os metros quadrados que vc deseja pintar: "))

litros = metroq/3
latas = litros/18
latas1 = math.ceil(latas)
preço = latas1*80


print(f"Latas: {latas1} preco: {preço}")


