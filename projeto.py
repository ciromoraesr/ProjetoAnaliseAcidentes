import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

datag = pd.read_csv('acidentes.csv', delimiter = ';')
estados = ['DF', 'SP', 'PE']
filtered = datag[datag['uf_acidente'].isin(estados)]
n = filtered.columns

columns_to_drop = ['ind_guardrail', 'ind_acostamento', 'lim_velocidade', 'tp_pavimento','tp_acidente', 'tp_cruzamento', 'chv_localidade']

filtered = filtered.drop(columns=columns_to_drop)


def mautopct(values):
    def sub(pct):
        total = sum(values)
        val = int(round(pct * total / 100))
        return '{p:.2f}%'.format(p=pct, v=val)
    return sub

#%%
filtered['data_acidente'] = pd.to_datetime(filtered['data_acidente'])
liminf = filtered['data_acidente'].min()
limsup = filtered['data_acidente'].max()
#%%
totalaci = filtered['qtde_acidente'].sum()
totalobi = filtered['qtde_acid_com_obitos'].sum()
datadf = filtered[filtered['uf_acidente'] == 'DF']
datasp = filtered[filtered['uf_acidente'] == 'SP']
datape = filtered[filtered['uf_acidente'] == 'PE']
totaldf = datadf['qtde_acidente'].sum()
totalsp = datasp['qtde_acidente'].sum()
totalpe = datape['qtde_acidente'].sum()

plt.figure(figsize = (20,6))
explode = (0.09,0,0.25)
y = np.array([totaldf,totalsp,totalpe])
colors = ('r', 'b', 'g')
plt.pie(y, labels=estados, explode=explode, autopct=mautopct(list(y)),colors = colors, shadow = True, startangle = 180,)
plt.gca().set_title("Acidentes de trânsito de 01/2018 até 08/2022", fontsize = 17)
plt.show()
#%%
filtered['data_acidente'] = pd.to_datetime(filtered['data_acidente'])
filtered['ano'] = filtered['data_acidente'].dt.year
filtered['mes'] = filtered['data_acidente'].dt.month
group = filtered.groupby(['ano', 'mes', 'uf_acidente'])['qtde_acidente'].count()
