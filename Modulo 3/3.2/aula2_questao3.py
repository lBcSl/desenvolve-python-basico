#questao 3

#variaveis 
idade = int(input("quantos anos você tem?"))
min_jogos = int(input("quantos jogos de tabuleiro ja jogou??"))
min_vencidos = int(input("qauntos jogos de tabulueiro você ja venceu?"))

#verificar se esta apto a receber o ingresso

pode_ingressar = 16 <= idade <= 18 and min_jogos >= 3 and min_vencidos >= 1
print(f"stats da carteira:{pode_ingressar}")