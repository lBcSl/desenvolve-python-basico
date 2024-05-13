#questao 02
# Solicita ao usuário a temperatura em Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Calcula a temperatura em Celsius 
celsius = int((fahrenheit - 32) * (5/9))

# o resultado 
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
