#QUESTAO 02

frase = input("Digite uma frase: ")

vogais = [char.lower() for char in frase if char.lower() in 'aeiou']
consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiou']

print("Vogais:", sorted(vogais))  
print("Consoantes:", consoantes)
