import numpy as np
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from datetime import datetime, timedelta

# Configura el estilo usando seaborn
sns.set_theme(style="whitegrid")

# Ticker del índice S&P 500
ticker = "^GSPC"
days = 10

# Calcular la fecha de inicio para los últimos 100 días
end_date = datetime.now()
start_date = end_date - timedelta(days=100)

# Descargar datos de Yahoo Finance usando yfinance
data = pd.DataFrame()
data[ticker] = yf.download(ticker, start=start_date, end=end_date)["Adj Close"]

# Calcular rendimientos logarítmicos
log_returns = np.log(1 + data.pct_change())
u = log_returns.mean()
var = log_returns.var()
drift = u - (0.5 * var)
stdev = log_returns.std()

# Configuración de la simulación
trials = 10000
Z = norm.ppf(np.random.rand(days, trials))
retornos_diarios = np.exp(drift.values + stdev.values * Z)
camino_de_precios = np.zeros_like(retornos_diarios)
camino_de_precios[0] = data.iloc[-1]

# Simular el camino de precios
for t in range(1, days):
    camino_de_precios[t] = camino_de_precios[t-1] * retornos_diarios[t]

# Calcular los percentiles 2.5 y 97.5 del precio final
precios_finales = camino_de_precios[-1]
percentil_2_5 = np.percentile(precios_finales, 2.5)
percentil_97_5 = np.percentile(precios_finales, 97.5)

print(f"95% de confianza de que el precio estará entre {percentil_2_5:.2f} y {percentil_97_5:.2f}")

# Graficar los resultados
plt.figure(figsize=(15, 6))
plt.plot(pd.DataFrame(camino_de_precios))
plt.xlabel("Número de días")
plt.ylabel("Precio del S&P 500")
plt.title("Simulación de Caminos de Precio para el S&P 500")

# Visualizar la distribución del precio final
plt.figure(figsize=(15, 6))
sns.histplot(pd.DataFrame(camino_de_precios).iloc[-1], kde=True)
plt.axvline(x=percentil_2_5, color='red', linestyle='--', label='Percentil 2.5')
plt.axvline(x=percentil_97_5, color='green', linestyle='--', label='Percentil 97.5')
plt.xlabel("Precio a " + str(days) + " días")
plt.ylabel("Frecuencia")
plt.title("Distribución de Precios Finales para el S&P 500")
plt.legend()
plt.show()
