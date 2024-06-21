#questao 04

import random

# Função para ler as palavras do arquivo gabarito_forca.txt
def ler_palavras():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras

# Função para escolher aleatoriamente uma palavra do arquivo
def escolher_palavra(palavras):
    return random.choice(palavras)

# Função para imprimir o enforcado de acordo com o número de erros
def imprime_enforcado(erros):
    # Carregar estágios do enforcado do arquivo gabarito_enforcado.txt
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
        enforcado = arquivo.read().strip().split("\n\n")

    # Imprimir estágio correspondente aos erros
    if erros < len(enforcado):
        print(enforcado[erros])
    else:
        print(enforcado[-1])  # Caso o número de erros ultrapasse os estágios disponíveis

# Função principal do jogo
def jogo_da_forca():
    print("Bem-vindo ao Jogo da Forca!\n")

    # Ler palavras do arquivo
    palavras = ler_palavras()

    # Escolher uma palavra aleatoriamente
    palavra_secreta = escolher_palavra(palavras)
    tamanho_palavra = len(palavra_secreta)
    letras_acertadas = ["_" for _ in palavra_secreta]  # Inicializa com underscores

    # Número máximo de tentativas (estágios do enforcado)
    max_tentativas = 6
    tentativas = 0
    letras_digitadas = []

    # Loop principal do jogo
    while tentativas < max_tentativas:
        # Imprime o estado atual da palavra
        print("Palavra:", " ".join(letras_acertadas))

        # Solicita uma letra ao jogador
        letra = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi digitada
        if letra in letras_digitadas:
            print(f"A letra '{letra}' já foi digitada. Tente outra letra.")
            continue
        else:
            letras_digitadas.append(letra)

        # Verifica se a letra está na palavra secreta
        if letra in palavra_secreta:
            print(f"Parabéns! A letra '{letra}' está na palavra.")
            # Atualiza as letras acertadas na posição correta
            for i in range(tamanho_palavra):
                if palavra_secreta[i] == letra:
                    letras_acertadas[i] = letra
        else:
            print(f"Ops! A letra '{letra}' não está na palavra.")
            tentativas += 1
            imprime_enforcado(tentativas)

        # Verifica se todas as letras foram descobertas
        if "_" not in letras_acertadas:
            print("Parabéns! Você ganhou!")
            print("A palavra era:", palavra_secreta)
            break

    # Se o número de tentativas esgotar
    if tentativas == max_tentativas:
        print("Que pena! Você foi enforcado.")
        print("A palavra era:", palavra_secreta)

# Executar o jogo
jogo_da_forca()

