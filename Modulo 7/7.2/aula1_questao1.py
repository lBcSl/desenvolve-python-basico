#questao 01

def data_por_extenso(data):
    # Dicionário para mapear o número do mês para o nome por extenso
    meses = {
        '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março',
        '04': 'Abril', '05': 'Maio', '06': 'Junho',
        '07': 'Julho', '08': 'Agosto', '09': 'Setembro',
        '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
    }
    
    # Separando o dia, mês e ano da data fornecida
    dia, mes, ano = data.split('/')
    mes_extenso = meses.get(mes, '')
    
    # Montando a frase formatada
    frase = f"Você nasceu em {dia} de {mes_extenso} de {ano}."
    
    return frase

# Solicitação da data de nascimento
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
print(data_por_extenso(data_nascimento))
4