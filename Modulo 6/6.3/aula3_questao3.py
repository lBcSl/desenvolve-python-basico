#QUESTAO 03

import random

lista = [random.randint(-10, 10) for _ in range(20)]

print("Original:", lista)

inicio_intervalo = 0
fim_intervalo = 0
max_negativos = 0
contador = 0

for i, num in enumerate(lista):
    if num < 0:
        contador += 1
        if contador > max_negativos:
            max_negativos = contador
            fim_intervalo = i
    else:
        contador = 0

inicio_intervalo = fim_intervalo - max_negativos + 1

del lista[inicio_intervalo:fim_intervalo + 1]

print("Editada:", lista)
