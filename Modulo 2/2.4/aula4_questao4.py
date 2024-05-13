#questao 4
#valor inteiro quantia em reais
quantia = int(input())

#notas possíveis
notas = [100, 50, 20, 10, 5, 2, 1]

#calcular a quantidade de notas necessárias para cada valor possível
for nota in notas:
    quantidade_notas = quantia // nota  # Calcula a quantidade de notas necessárias
    quantia %= nota  # Atualiza a quantia restante
    print(f"{quantidade_notas} nota(s) de R${nota},00")  #o resultado
