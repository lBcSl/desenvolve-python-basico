#questao 01
# Solicita ao usuário o comprimento do terreno
comprimento = float(input("Digite o comprimento do terreno em metros: "))

# Solicita ao usuário a largura do terreno
largura = float(input("Digite a largura do terreno em metros: "))

# Solicita ao usuário o preço do metro quadrado da região
preco_m2 = float(input("Digite o preço do metro quadrado da região: "))

# Calcula a área do terreno
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

#o resultado 
print(f"O terreno possui {area_m2}m² e custa R${preco_total:.2f}.")
