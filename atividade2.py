import matplotlib.pyplot as plt
import numpy as np

# Criando os dados para o gráfico
horas = list(range(0, 25))  # Horas de 0 a 24
temperaturas = []

# Gerando os valores de temperatura
for hora in horas:
    if hora <= 12:
        # Aumentando de 15°C até 30°C ao meio-dia
        temperatura = 15 + (15 * hora / 12)
    else:
        # Diminuindo de 30°C até 18°C à meia-noite
        temperatura = 30 - (12 * (hora - 12) / 12)
    temperaturas.append(temperatura)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(horas, temperaturas, marker='o', linestyle='-', color='red', linewidth=2)

# Adicionando título e rótulos
plt.title('Evolução da Temperatura Durante o Dia', fontsize=16)
plt.xlabel('Hora do Dia', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)

# Adicionando grade
plt.grid(True, linestyle='--', alpha=0.7)

# Configurando os eixos
plt.xlim(0, 24)
plt.xticks(range(0, 25, 2))

# Exibindo o gráfico
plt.tight_layout()
plt.show()
