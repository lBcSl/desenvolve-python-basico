#QUESTAO 04

def obter_lista(nome_lista):
    quantidade = int(input(f"Digite a quantidade de elementos da {nome_lista}: "))
    print(f"Digite os {quantidade} elementos da {nome_lista}:")
    return [int(input()) for _ in range(quantidade)]

def combinar_listas_alternadamente(lista1, lista2):
    lista_intercalada = []
    tamanho_max = max(len(lista1), len(lista2))
    
    for i in range(tamanho_max):
        if i < len(lista1):
            lista_intercalada.append(lista1[i])
        if i < len(lista2):
            lista_intercalada.append(lista2[i])
            
    return lista_intercalada

lista1 = obter_lista("lista 1")
lista2 = obter_lista("lista 2")

lista_intercalada = combinar_listas_alternadamente(lista1, lista2)

print("Lista intercalada:", lista_intercalada)
