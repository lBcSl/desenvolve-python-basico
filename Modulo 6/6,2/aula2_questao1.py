#QUESTAO 01

import random


valores = [random.randint(-100, 100) for _ in range(20)]

valores_ordenados = sorted(valores)

indice_maior_valor = valores.index(max(valores))
indice_menor_valor = valores.index(min(valores))

print("Lista ordenada:", valores_ordenados)
print("Lista original:", valores)
print("Índice do maior valor da lista:", indice_maior_valor)
print("Índice do menor valor da lista:", indice_menor_valor)

########################################################################
