#Faça um programa que receba uma string e responda se ela tem
# alguma vogal, se sim, quais são? E também diga se ela é uma frase ou não.

nome = str(input('digite uma palavra ou frase: '))

for i in nome:
    if "a" == i:
       print("Vogal A")
    if "e" == i:
       print("Vogal E")
    if "i" == i:
       print("Vogal I")
    if "o" == i:
       print("Vogal O")
    if "u" == i:
       print("Vogal U")


if " " in nome:
    print("isso é uma frase")
else:
    print("não é uma frase")

