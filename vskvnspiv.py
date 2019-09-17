
def somar(valor1,valor2):
    a = valor1
    b = valor2
    return a if b == 0 or (valor1 < 0 and valor2 > 0 or (valor1 > 0 and valor2 < 0)) and abs(a) == abs(b) else somar(b ^ a, b & a <<1)

print(somar(10,25))