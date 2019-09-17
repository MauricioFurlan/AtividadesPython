
def somar(valor1, valor2):
    a = valor1
    b = valor2
    if (valor1 < 0 and valor2 > 0 or (valor1 > 0 and valor2 < 0)) and abs(a) == abs(b):
        return 0
    else:
        try:
            return a if b == 0 else somar(a ^ b )
        except Exception:
            a = ~valor1 >> 1
            b = ~valor2 >> 1
            try:
                resultado = a if b == 0 else somar(a ^ b, (a & b) << 1) if a < 0 else somar(b ^ a, (b & a) << 1)
                return resultado * -1
            except Exception:
                return '???????????'


def somaNaMao():
    valor1 = int(input('Valor1:'))
    valor2 = int(input('Valor2:'))
    resultado = somar(valor1, valor2)
    print(f'\n{valor1} + {valor2} =  {resultado}')


def somaAutomatica():
    valor1 = 0
    valor2 = 0
    for i in range(100):
        for j in range(10 + 1):
            result = somar(valor1, valor2)
            print(f'{valor1} + {valor2} = {result}')
            valor2 = valor2 - 1
        valor1 = valor1 - 1
        valor2 = 0



somaNaMao()

