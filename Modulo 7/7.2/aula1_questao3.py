#questao 03

def eh_palindromo(frase):
    # Função para remover espaços em branco e pontuações
    def limpar_texto(texto):
        return ''.join(c for c in texto if c.isalnum()).lower()

    # Limpa a frase original e a sua versão invertida
    frase_limpa = limpar_texto(frase)
    frase_invertida = frase_limpa[::-1]

    # Verifica se são iguais
    if frase_limpa == frase_invertida:
        return True
    else:
        return False

# Loop para verificar múltiplas frases
while True:
    frase = input("Digite uma frase (digite 'fim' para encerrar): ")
    if frase.lower() == 'fim':
        break
    
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
