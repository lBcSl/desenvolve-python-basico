#questao 04

import re

def validador_senha(senha):
    # Pelo menos 8 caracteres de comprimento
    if len(senha) < 8:
        return False
    
    # Pelo menos uma letra maiúscula e uma minúscula
    if not re.search(r'[a-z]', senha) or not re.search(r'[A-Z]', senha):
        return False
    
    # Pelo menos um número
    if not re.search(r'\d', senha):
        return False
    
    # Pelo menos um caractere especial
    if not re.search(r'[@#$%^&+=]', senha):
        return False
    
    return True

# Exemplos de uso
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False
