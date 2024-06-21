#questao 07

import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_cript = []
    for nome in nomes:
        nome_criptografado = ''.join(chr(ord(c) + chave) if 33 <= ord(c) <= 126 else c for c in nome)
        nomes_cript.append(nome_criptografado)
    return nomes_cript, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print("Nomes criptografados:", nomes_cript)
print("Chave de criptografia:", chave_aleatoria)
