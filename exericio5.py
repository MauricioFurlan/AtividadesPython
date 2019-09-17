nota1 = float(input("digite o valor da nota1: "))
nota2 = float(input("digite o valor da nota2: "))

media = (nota1+nota2)/2

if media < 7:
    print(f"a média do aluno foi {media} e esta REPROVADO")
elif media >= 7 and media < 10:
    print(f"a média do aluno foi {media} e esta  APROVADO!")
else:
    print(f"a nota do aluno foi 10 e esta  APROVADO COM DISTINÇÃO!")


