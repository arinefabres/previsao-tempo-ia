import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o estilo
sns.set(style="whitegrid")

# Criando dados fictícios de vendas para uma semana
np.random.seed(42)  # Para reprodutibilidade
dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
vendas = np.random.randint(5000, 15000, 7)
clientes = np.random.randint(100, 500, 7)
lucro = vendas * np.random.uniform(0.15, 0.25, 7)  # Lucro entre 15% e 25% das vendas

# Criando o DataFrame
df_vendas = pd.DataFrame({
    'Dia': dias_semana,
    'Vendas': vendas,
    'Clientes': clientes,
    'Lucro': lucro
})

# Configurando a figura para os três gráficos
plt.figure(figsize=(18, 12))

# 1. Gráfico de barras - Total de vendas por dia
plt.subplot(2, 2, 1)
ax = sns.barplot(x='Dia', y='Vendas', data=df_vendas, palette='Blues_d')
plt.title('Total de Vendas por Dia da Semana', fontsize=14)
plt.xlabel('Dia da Semana', fontsize=12)
plt.ylabel('Vendas (R$)', fontsize=12)
plt.xticks(rotation=45)

# Adicionando valores no topo das barras
for i, v in enumerate(vendas):
    ax.text(i, v + 500, f'{v}', ha='center', fontsize=10)

# 2. Gráfico de dispersão - Relação entre número de clientes e vendas
plt.subplot(2, 2, 2)
sns.scatterplot(x='Clientes', y='Vendas', size='Lucro', sizes=(100, 500), 
                hue='Dia', data=df_vendas, palette='viridis')
plt.title('Relação entre Número de Clientes e Total de Vendas', fontsize=14)
plt.xlabel('Número de Clientes', fontsize=12)
plt.ylabel('Vendas (R$)', fontsize=12)

# 3. Heatmap - Correlação entre as variáveis
plt.subplot(2, 2, 3)
# Calculando a matriz de correlação
corr = df_vendas[['Vendas', 'Clientes', 'Lucro']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlação entre Vendas, Clientes e Lucro', fontsize=14)

# Adicionando espaço entre os subplots
plt.tight_layout(pad=3.0)

# Explicação dos gráficos
plt.figtext(0.5, 0.01, """
Análise dos Gráficos:
1. Gráfico de Barras: Mostra o total de vendas para cada dia da semana, permitindo identificar os dias de maior faturamento.
2. Gráfico de Dispersão: Revela a relação entre o número de clientes e o total de vendas, onde o tamanho dos pontos representa o lucro obtido.
3. Mapa de Calor: Apresenta a correlação entre vendas, clientes e lucro, indicando como essas variáveis se influenciam mutuamente.
""", ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Exibindo o gráfico
plt.show()
