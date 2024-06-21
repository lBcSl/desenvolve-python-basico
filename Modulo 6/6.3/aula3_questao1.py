#QUESTAO 01

def obter_valores():
    valores = []
    print("Digite pelo menos 4 valores inteiros. Digite 'fim' para terminar a entrada de dados:")
    while True:
        entrada = input()
        if entrada.lower() == 'fim':
            if len(valores) >= 4:
                break
            else:
                print("Você precisa digitar pelo menos 4 valores. Continue digitando.")
        else:
            try:
                valores.append(int(entrada))
            except ValueError:
                print("Por favor, insira um número inteiro ou 'fim' para terminar.")
    return valores

def imprimir_fatiamento(valores):
    print("Lista original:", valores)
    print("Os 3 primeiros elementos:", valores[:3])
    print("Os 2 últimos elementos:", valores[-2:])
    print("Lista invertida:", valores[::-1])
    print("Elementos de índice par:", valores[::2])
    print("Elementos de índice ímpar:", valores[1::2])


valores = obter_valores()
imprimir_fatiamento(valores)
