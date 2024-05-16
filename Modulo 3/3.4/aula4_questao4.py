#questao 4

distancia = int(input("Digite a distância em Km"))
peso = int(input("Digite o peso do pacote em Kg"))

if  distancia <= 100:
    valor_do_frete = distancia * 1 * peso
elif  distancia <= 300:
   valor_do_frete = distancia * 1.50 * peso

print(valor_do_frete)
