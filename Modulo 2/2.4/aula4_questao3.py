#questao 03
# Inicializa uma variável para armazenar o preço total da compra
preco_total = 0

#Loop das informações de cada produto
for i in range(1, 4):
    #nome do produto
    nome_produto = input("*Digite o nome do produto {i}:* ")

    #preço unitário do produto
    preco_unitario = float(input("f*Digite o preço unitário do produto {i}:* "))

    #quantidade do produto
    quantidade = int(input("f*Digite a quantidade do produto {i}:* "))

    # Calcula o preço total do produto e adiciona ao preço total da compra
    preco_total += preco_unitario * quantidade

#preço total 
print("Total: R${:,.2f}".format(preco_total))
