coisa = "Mauricio"

# print(coisa.index("a")) #duvida sobre quando o nome tiver mais de uma letra igual
# print(coisa.count('i')) # CONTA QUANTOS I TEM
# print(coisa.partition("r")[0])
# print(coisa.replace("i", "c"))
# coisa1 = coisa.split("i")[0]
# print( coisa1.replace("u","a"))

def testando(num, b=1, *c,**x):
    return num,b, c, x


# print(testando([1,5,4,2],7,1,4,3,4,3,f=2))


def Empacotar(*c):
    return c

valor = Empacotar(10,30,20)
valor.count(valor)
print(type(valor))






