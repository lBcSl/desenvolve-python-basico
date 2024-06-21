#questao 02

def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    frase_modificada = ''.join('*' if c in vogais else c for c in frase)
    return frase_modificada

# Solicitação da frase
frase = input("Digite uma frase: ")
frase_modificada = substituir_vogais(frase)
print(f"Frase modificada: {frase_modificada}")
