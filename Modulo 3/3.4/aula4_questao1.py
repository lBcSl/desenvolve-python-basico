#questão 01

x =  int(input("Digite um numero: "))
y =  int(input("Digite um numero: "))

soma = x + y
print(f" x + Y = {soma}")

if soma % 2 == 0:
    print("a soma dos numeros e par.")
else:
    print("A soma dos numeros e impar.")