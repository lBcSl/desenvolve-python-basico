#questao 03

import urllib.request

# URL do arquivo de texto
url = "https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt"
local_filename = "estomago.txt"

# Baixar o arquivo e salvá-lo localmente
urllib.request.urlretrieve(url, local_filename)

# Função para contar menções aos nomes dos personagens
def contar_mencoes_personagem(nome, texto):
    texto_lower = texto.lower()
    nome_lower = nome.lower()
    return texto_lower.count(nome_lower)

# Abrir o arquivo para leitura
with open(local_filename, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    # Imprimir as primeiras 25 linhas
    print("Texto das primeiras 25 linhas:")
    for i in range(min(25, len(linhas))):
        print(linhas[i].rstrip())  # rstrip() para remover o '\n'

    # Número total de linhas do arquivo
    num_linhas = len(linhas)
    print(f"\nNúmero total de linhas do arquivo: {num_linhas}")

    # Encontrar a linha com maior número de caracteres
    maior_linha = max(linhas, key=len)
    num_caracteres_maior_linha = len(maior_linha)
    print(f"\nLinha com maior número de caracteres:")
    print(maior_linha.rstrip())
    print(f"Número de caracteres: {num_caracteres_maior_linha}")

    # Contar menções aos nomes dos personagens "Nonato" e "Íria"
    texto_completo = ''.join(linhas)
    mencoes_nonato = contar_mencoes_personagem("Nonato", texto_completo)
    mencoes_iria = contar_mencoes_personagem("Íria", texto_completo)
    total_mencoes = mencoes_nonato + mencoes_iria
    print(f"\nNúmero de menções aos personagens 'Nonato' e 'Íria': {total_mencoes}")
