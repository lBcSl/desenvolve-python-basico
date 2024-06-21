#questao 06

from collections import Counter

frase = input("Digite uma frase: ").lower()
palavra_objetivo = input("Digite a palavra objetivo: ").lower()

palavras_frase = frase.split()
anagramas = [palavra for palavra in palavras_frase if Counter(palavra) == Counter(palavra_objetivo)]

print(f"Anagramas: {anagramas}")
