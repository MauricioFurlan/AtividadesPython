preço1 = float(input("preço da banana: "))
preço2 = float(input("preço da melancia: "))
preço3 = float(input("preço do tomate: "))

if preço1 > preço2 and preço1 > preço3:
    print("O mais barato é a banana")
elif preço2 > preço1 and preço2 > preço3:
    print("O mais barato é a melancia")
elif preço3 > preço1 and preço3 > preço2:
    print("O mais barato é o tomate")
else:
    print("Melhor nao levar nada hoje, os preços não estão bons")