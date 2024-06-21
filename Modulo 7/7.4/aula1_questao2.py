#questao 02
import string

def limpar_palavra(palavra):
    # Remove caracteres não alfabéticos
    palavra_limpa = ''.join(filter(lambda char: char.isalpha(), palavra))
    return palavra_limpa

def salvar_palavras_em_arquivo(caminho_arquivo_entrada, caminho_arquivo_saida):
    # Abrir o arquivo de entrada para leitura ('r' para leitura, 'utf-8' para encoding)
    with open(caminho_arquivo_entrada, 'r', encoding='utf-8') as arquivo_entrada:
        # Ler o conteúdo do arquivo
        conteudo = arquivo_entrada.read()

        # Remover espaços em branco e quebrar em palavras
        palavras = conteudo.split()

        # Limpar cada palavra
        palavras_limpas = [limpar_palavra(palavra) for palavra in palavras]

    # Abrir o arquivo de saída para escrita ('w' para escrita, 'utf-8' para encoding)
    with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        # Escrever cada palavra limpa em uma linha
        for palavra in palavras_limpas:
            if palavra:
                arquivo_saida.write(palavra + '\n')

    # Retornar o caminho completo do arquivo de saída
    return caminho_arquivo_saida

# Caminho dos arquivos
caminho_arquivo_entrada = "frase.txt"
caminho_arquivo_saida = "palavras.txt"

# Salvar palavras limpas em um arquivo
caminho_completo_saida = salvar_palavras_em_arquivo(caminho_arquivo_entrada, caminho_arquivo_saida)

# Ler e imprimir o conteúdo do arquivo de palavras limpas
with open(caminho_completo_saida, 'r', encoding='utf-8') as arquivo_palavras:
    conteudo_palavras = arquivo_palavras.read()
    print(conteudo_palavras)
