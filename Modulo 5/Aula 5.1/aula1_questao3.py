#QUESTAO 03

#import bliblioteca 
import random

# Definindo o valor de aleatorio de 1 a 10
n = random.randint (1, 10)

# verificando o chute do usuario
while True:
    palpite = int(input("Tente adivinha o numero de 1 a 10: "))

    if palpite < n:
        print("Muito baixo, tente outro numero")
    if palpite > n:
        print("Muito alto, tente outro numero")
    else:
        palpite = n 
        print("Parebens Você acertou")
        break
        