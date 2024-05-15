#questao 4
#escolha de classe
classe = (input("Escolha uma classe (guerreiro, mago ou arqueiro): "))
print(f"{classe} foi escolhida") 

print("AGORA VAMOS CRIAR SUA FICHA")
pontos_forca = int(input("Digite os pontos de força (de 1 a 20): "))
pontos_magia = int(input("Digite os pontos de magia (de 1 a 20): "))

resultado_ficha = {
    (classe == "guerreiro" and pontos_forca >= 15 and pontos_magia <= 10) or
    (classe == "mago" and pontos_forca <= 10 and pontos_magia >= 15) or
    (classe == "arqueiro" and 6 <= pontos_forca <= 14 and 6 <= pontos_magia <= 14)
} 
print("Pontos de atributo consistentes com a classe escolhida:", resultado_ficha)
