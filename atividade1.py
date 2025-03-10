import pandas as pd
import numpy as np
#instalar pandas e dependencias com comando "pip install pandas numpy"

# Criação do DataFrame
dados = {
    'Data': ['15/01/2025', '15/01/2025', '15/01/2025', '15/01/2025', '15/01/2025'],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Porto Alegre', 'Salvador'],
    'Temperatura Máxima (°C)': [30.5, 35.0, 24.0, 28.0, 31.0],
    'Temperatura Mínima (°C)': [22.0, 25.0, 18.0, 20.0, 24.5],
    'Precipitação (mm)': [12.0, np.nan, 8.0, 15.0, np.nan],
    'Umidade Relativa (%)': [78, 70, np.nan, 82, 80]
}

df = pd.DataFrame(dados)

print("DataFrame Original:")
print(df)
print("\n")

media_precipitacao = df['Precipitação (mm)'].mean()
df['Precipitação (mm)'] = df['Precipitação (mm)'].fillna(media_precipitacao)

mediana_umidade = df['Umidade Relativa (%)'].median()
df['Umidade Relativa (%)'] = df['Umidade Relativa (%)'].fillna(mediana_umidade)

df['Amplitude Térmica'] = df['Temperatura Máxima (°C)'] - df['Temperatura Mínima (°C)']

print("DataFrame após substituições e adição da Amplitude Térmica:")
print(df)
print("\n")

df_acima_30 = df[df['Temperatura Máxima (°C)'] > 30]
print("DataFrame com cidades com Temperatura Máxima acima de 30°C:")
print(df_acima_30)
print("\n")

df = df[['Data', 'Cidade', 'Temperatura Máxima (°C)', 'Temperatura Mínima (°C)', 
         'Amplitude Térmica', 'Precipitação (mm)', 'Umidade Relativa (%)']]

print("DataFrame final com colunas reordenadas:")
print(df)
