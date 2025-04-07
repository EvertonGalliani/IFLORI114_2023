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

data = [] #Armazena as datas de domingo referentes às semanas que tiveram suas médias calculadas
data_temporário = 0 #Cria uma variável para armazenar a data quando chega em domingo 00h

temp_ano = [] # Armazena as médias de temperatura das 52 semanas do ano medias_ano
temp_semanas = [] #Armazena as temperaturas de cada hora para calcular a média quando chega em sábado 23h
prec_ano = []
prec_semanas = []

for i in df.index:
	if np.isnan(df['Temp. Med. (C)'][i]) == False:
		temp_semanas.append(df['Temp. Med. (C)'][i])
		prec_semanas.append(df["Chuva (mm)"][i])
	if df['Hora (Local)'][i] == '0000' and df['data_hora'][i].weekday() == 6:
		data_temporario = df["data_hora"][i]
	if df['Hora (Local)'][i] == '2300' and df['data_hora'][i].weekday() == 5:
		data.append(data_temporario)
	#	data.append(df["data_hora"][i])
		if len(temp_semanas) != 0:
			temp_ano.append(np.mean(temp_semanas))
			prec_ano.append(np.sum(prec_semanas))
#			data.append(df["data_hora"][i-23])
#			print(f"Temperatura média do dia {df['data_hora'][i-23]}: {np.mean(media_semanas)}")
			temp_semanas.clear()
			prec_semanas.clear()
		else:
			temp_ano.append('nan')
			prec_ano.append('nan')
#			print(f"Temperatura média do dia {df['data_hora'][i-23]}: {np.mean(media_semanas)}")
"""
plt.plot(data, temp_ano)
plt.show()
plt.savefig(f'WEEKLY_{codigo}_{2023}.png')

"""
#print(data, medias_ano)

teste = df.columns
#for i in d:
#	print(i)
#print(data)

df1 = pd.DataFrame({"DATA": pd.to_datetime(data), "TMED": temp_ano, "CHUVA": prec_ano})
print(df1)
df1.to_csv(f"WEEKLY_{codigo}_{2023}.csv", index=False)
print(f"CSV salvo como WEEKLY_{codigo}_{ano}.csv.")
