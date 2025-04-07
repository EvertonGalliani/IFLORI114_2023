import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#print("Código da estação:")
codigo = "IFLORI114"
ano = "2023"
path = f'/home/sifapsc/scripts/scripts_everton/{codigo}_{ano}/'
arch = f'dados_{codigo}_{ano}'
csv = f"{path}{arch}"
df = pd.read_csv(csv)
#print(df)

df['Hora (Local)'] = df['Hora (Local)'].astype(str).str.zfill(4)
df['data_hora'] = pd.to_datetime(df['data_hora'])
#print(df)
#print(df.dtypes)

data = []
temp_ano = [] #Lista onde serão armazenados os valores das 365 médias do ano medias_ano
temp_dias = [] #Lista temporária para armazenar os valores horários para calcular as médias media_semanas
prec_ano = [] #Lista onde serão armazenados os acumulados diários de chuva
prec_dias = [] #Lista temporária para armazenar os valores horários da chuva

for i in df.index:
	if np.isnan(df['Temp. Med. (C)'][i]) == False:
		temp_dias.append(df['Temp. Med. (C)'][i])
		prec_dias.append(df['Chuva (mm)'][i])
	if df['Hora (Local)'][i] == '2300':
		data.append(df["data_hora"][i-23])
		if len(temp_dias) != 0:
			temp_ano.append(np.mean(temp_dias))
			prec_ano.append(np.sum(prec_dias))
			temp_dias.clear()
			prec_dias.clear
		else:
			temp_ano.append('nan')
			prec_ano.append('nan')
		prec_dias.clear()

##Convertendo a data para Datetime para plotagem
data = pd.to_datetime(data, format = '%Y-%m-%d %H:%M:%S')
#print(data)

"""
# Plotando o Gráfico
fig, ax1 = plt.subplots()

# Eixo esquerdo - Temperatura
ax1.set_xlabel('Data')
ax1.set_ylabel('Temperatura (°C)') #, color='tab:red')
ax1.plot(data, temp_ano) #, color='tab:red', marker='o', linestyle='-')
#ax1.tick_params(axis='y', labelcolor='tab:red')

# Eixo direito - Precipitação
ax2 = ax1.twinx()
ax2.set_ylabel('Precipitação (mm)', color='tab:blue')
ax2.bar(data.astype(str), prec_ano, color='tab:blue')
#ax2.tick_params(axis='y', labelcolor='tab:blue')

# Melhorando a visualização
fig.autofmt_xdate()
fig.tight_layout()

plt.plot(data, temp_ano)
plt.title('Temperatura ao Longo do Ano')
plt.show()
plt.savefig(f"DAILY_{codigo}_{ano}.png")
print(f"Gráfico salvo como DAILY_{codigo}_{ano}")
"""

df1 = pd.DataFrame({"DATA": pd.to_datetime(data), "TMED": temp_ano, "CHUVA": prec_ano})
print(df1)
df1.to_csv(f"DAILY_{codigo}_{ano}.csv", index=False)
print(f"CSV salvo como DAILY_{codigo}_{ano}.csv.")
