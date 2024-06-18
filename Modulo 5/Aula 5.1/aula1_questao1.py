# QUESTAO 01

# Solicita ao usuário para inserir dois números decimais
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

# Verifica se as entradas são válidas
if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
    num1 = float(num1)
    num2 = float(num2)

    # Calcula a diferença absoluta entre os dois números
    Arredondamento = abs(num1 - num2)

    # Arredonda o resultado para duas casas decimais
    diferenca_arredondamento = round(Arredondamento, 2)

    # Exibe o resultado
    print(f"A diferença absoluta entre os números é: {diferenca_arredondamento}")
else:
    print("Por favor, insira valores numéricos válidos.")
