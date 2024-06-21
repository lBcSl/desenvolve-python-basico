#QUESTAO 02

import random

num_elementos = random.randint(5, 20)


elementos = [random.randint(1, 10) for _ in range(num_elementos)]

soma_elementos = sum(elementos)
media_elementos = soma_elementos / len(elementos)


print("Lista elementos:", elementos)
print("Soma dos valores da lista:", soma_elementos)
print("Média dos valores da lista:", media_elementos)
