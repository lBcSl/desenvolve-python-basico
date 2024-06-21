#questao 05

import csv

# Dados dos carros (exemplo)
carros = [
    {"Modelo": "Civic", "Fabricante": "Honda", "Ano de fabricação": 2020, "Quilometragem": 15000},
    {"Modelo": "Corolla", "Fabricante": "Toyota", "Ano de fabricação": 2019, "Quilometragem": 20000},
    {"Modelo": "Gol", "Fabricante": "Volkswagen", "Ano de fabricação": 2018, "Quilometragem": 30000},
    {"Modelo": "Onix", "Fabricante": "Chevrolet", "Ano de fabricação": 2021, "Quilometragem": 10000},
    {"Modelo": "Fusion", "Fabricante": "Ford", "Ano de fabricação": 2017, "Quilometragem": 40000},
    {"Modelo": "HB20", "Fabricante": "Hyundai", "Ano de fabricação": 2020, "Quilometragem": 18000},
    {"Modelo": "Compass", "Fabricante": "Jeep", "Ano de fabricação": 2019, "Quilometragem": 25000},
    {"Modelo": "HR-V", "Fabricante": "Honda", "Ano de fabricação": 2018, "Quilometragem": 28000},
    {"Modelo": "Uno", "Fabricante": "Fiat", "Ano de fabricação": 2016, "Quilometragem": 50000},
    {"Modelo": "Creta", "Fabricante": "Hyundai", "Ano de fabricação": 2022, "Quilometragem": 5000},
]

# Nome do arquivo CSV
nome_arquivo = "meus_carros.csv"

# Abrir o arquivo CSV para escrita
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    # Configurar o escritor CSV
    escritor_csv = csv.writer(arquivo_csv)

    # Escrever os cabeçalhos
    escritor_csv.writerow(["Modelo", "Fabricante", "Ano de fabricação", "Quilometragem"])

    # Escrever os dados de cada carro
    for carro in carros:
        escritor_csv.writerow([carro["Modelo"], carro["Fabricante"], carro["Ano de fabricação"], carro["Quilometragem"]])

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
