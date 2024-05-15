#questao 5
#gênero da pessoa, idade e tempo de serviço
genero = input("Digite ( M ) para masculino e ( F ) para feminino ")
idade = int(input("Digite sua idade"))
tempo_de_serviço = int(input("Digite seu tempo de serviço"))

#Verificar se pode aposentar
aposentar = (
    (genero == "F" and (idade > 60 or (idade >= 60 and tempo_de_serviço >= 25))) or
    (genero == "M" and (idade > 65 or tempo_de_serviço >= 30))
)
 
print(f"poder se aposentar {aposentar}")