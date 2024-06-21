#questao 05

frase = input("Digite uma frase: ").lower()

vogais = "aeiou"
indices_vogais = [i for i, c in enumerate(frase) if c in vogais]
quantidade_vogais = len(indices_vogais)

print(f"{quantidade_vogais} vogais")
print(f"Índices {indices_vogais}")
