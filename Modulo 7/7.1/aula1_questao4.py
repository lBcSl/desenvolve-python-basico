#questao 04

numero = input("Digite o número: ")

if len(numero) == 8:
    numero_completo = f"9{numero[:5]}-{numero[5:]}"
elif len(numero) == 9:
    if numero.startswith('9'):
        numero_completo = f"{numero[:5]}-{numero[5:]}"
    else:
        numero_completo = f"{numero[:2]}{numero[2:6]}-{numero[6:]}"
else:
    print("Número inválido.")
    numero_completo = None

if numero_completo:
    print(f"Número completo: {numero_completo}")
