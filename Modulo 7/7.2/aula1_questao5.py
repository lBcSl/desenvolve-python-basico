#questao 05

import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    frase_embaralhada = []
    
    for palavra in palavras:
        if len(palavra) <= 3:
            frase_embaralhada.append(palavra)
        else:
            inicio = palavra[0]
            fim = palavra[-1]
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = ''.join([inicio] + meio + [fim])
            frase_embaralhada.append(palavra_embaralhada)
    
    return ' '.join(frase_embaralhada)

# Exemplo de uso
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
# Saída esperada: "Ptohy*n é uma lgiunagme de pmorgmaaçro"
