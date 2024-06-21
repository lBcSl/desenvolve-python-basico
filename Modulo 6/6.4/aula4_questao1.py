#QUESTAO 01

#1
numeros_pares = [num for num in range(20, 51, 2)]
print("Números pares entre 20 e 50:", numeros_pares)

#2
quadrados = [num**2 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
print("Quadrados dos valores de 1 a 9:", quadrados)

#3
divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]
print("Números entre 1 e 100 divisíveis por 7:", divisiveis_por_7)

#4
paridade = ['par' if num % 2 == 0 else 'ímpar' for num in range(0, 30, 3)]
print("Paridade dos valores em range(0,30,3):", paridade)

