#questao 01

def salvar_frase_em_arquivo(frase):
    # Caminho completo onde o arquivo será salvo
    caminho_arquivo = "frase.txt"
    
    # Abrir o arquivo para escrita ('w' para escrita, 'utf-8' para encoding)
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(frase)
    
    return caminho_arquivo

# Solicitar a frase ao usuário
frase = input("Digite uma frase: ")

# Salvar a frase em um arquivo e obter o caminho completo
caminho_completo = salvar_frase_em_arquivo(frase)

# Imprimir o caminho completo onde o arquivo foi salvo
print(f"Frase salva em {caminho_completo}")

