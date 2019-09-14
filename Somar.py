# coding=utf-8
def somar(valor1,valor2):

        return valor2 and somar(valor1 ^ valor2, (valor1 & valor2) << 1) or valor1
print(somar(4,4))
    #Exemplo de 4 + 4 = 8
    # 4 em binário = 00000100
    # 4 em binário = 00000100

    # (valor1 & valor2) 4 & 4 O operador copiao bit para o resultado, se existir nos dois operandos
    # segue tabela &
    # 0 & 0 = 0
    # 0 & 1 = 0
    # 1 & 0 = 0
    # 1 & 1 = 1
    # 00000100
    # 00000100
    #=00000100 = 4

    # valor1 ^ valor 2 = 4 XOR 4 Ele copia o bit se estiver definido em um operando, mas não em ambos.
    # segue tabela ^

    # 0 XOR 0 = 0
    # 0 XOR 1 = 1
    # 1 XOR 0 = 1
    # 1 XOR 1 = 0
    # 00000100
    # 00000100
    # =00000000 = 0

    #<< Binary Left Shift

    #<<-------------
    #add left shift
    #4 000000100
    #= 000001000 = 8



