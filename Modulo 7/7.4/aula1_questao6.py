#questao 6

import csv

# Nome do arquivo CSV
nome_arquivo = 'spotify-2023.csv'

# Lista para armazenar as músicas mais populares de cada ano
top_musicas_por_ano = {}

# Abrir o arquivo CSV para leitura
with open(nome_arquivo, mode='r', encoding='latin-1') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    # Ignorar cabeçalho
    next(leitor_csv)
    
    # Processar cada linha do arquivo CSV
    for linha in leitor_csv:
        # Extrair informações da linha
        track_name = linha[0].strip()
        artist_name = linha[1].strip()
        artist_count = int(linha[2].strip())
        released_year = int(linha[3].strip())
        streams = int(linha[8].strip())
        
        # Verificar se é uma música válida
        if released_year >= 2012 and released_year <= 2022 and artist_count == 1:
            # Verificar se já temos registro para este ano
            if released_year not in top_musicas_por_ano:
                top_musicas_por_ano[released_year] = [track_name, artist_name, streams]
            else:
                # Comparar com a música registrada para ver se é mais popular
                if streams > top_musicas_por_ano[released_year][2]:
                    top_musicas_por_ano[released_year] = [track_name, artist_name, streams]

# Formatar a lista final conforme solicitado
lista_final = [[info[0], info[1], ano, info[2]] for ano, info in top_musicas_por_ano.items()]

# Ordenar a lista final por ano
lista_final.sort(key=lambda x: x[2])

# Imprimir a lista final
print(lista_final)

