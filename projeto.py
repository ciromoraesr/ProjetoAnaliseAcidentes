import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

datag = pd.read_csv('acidentes.csv', delimiter = ';')
#%%
#encontra o estado do nordeste com maior número de acidentes de trânsito
nordeste = ['MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA']
dfn = datag[datag['uf_acidente'].isin(nordeste)]
dfn = dfn.groupby('uf_acidente')['qtde_acidente'].sum()
state= dfn.idxmax()

#%%

estados = ['DF', 'SP', 'BA']
filtered = datag[datag['uf_acidente'].isin(estados)]
n = filtered.columns

columns_to_drop = ['ind_guardrail', 'ind_acostamento', 'lim_velocidade', 'tp_pavimento','tp_acidente', 'tp_cruzamento', 'chv_localidade']

filtered = filtered.drop(columns=columns_to_drop)


def mautopct(values):
    def sub(pct):
        total = sum(values)
        val = int(round(pct * total / 100))
        return '{p:.1f}%'.format(p=pct, v=val)
    return sub

#%%
totalaci = filtered['qtde_acidente'].sum()
totalobi = filtered['qtde_acid_com_obitos'].sum()
datadf = filtered[filtered['uf_acidente'] == 'DF']
datasp = filtered[filtered['uf_acidente'] == 'SP']
databa = filtered[filtered['uf_acidente'] == 'BA']
datab = filtered[filtered['uf_acidente'].isin(['DF', 'SP', 'BA'])]
totaldf = datadf['qtde_acidente'].sum()
totalsp = datasp['qtde_acidente'].sum()
totalba = databa['qtde_acidente'].sum()
totalb = datab['qtde_acidente'].sum()
estados = ['DF', 'SP', 'BA', "OUTRAS UF'S"]
plt.figure(figsize = (20,6))
explode = (0.09,0,0, 0)
y = np.array([totaldf,totalsp,totalba,totalb])
colors = ('brown', 'royalblue', 'orange', 'darkgreen')

plt.pie(y, labels=estados, explode=explode, autopct=mautopct(list(y)),textprops={'fontsize': 13},colors = colors,pctdistance = 0.7, shadow = False, startangle = 30)
centre_circle = plt.Circle((0, 0), 0.30, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.gca().set_title("Acidentes de trânsito de 01/2018 até 08/2022", fontsize = 17)
plt.show()
#%%
filtered['data_acidente'] = pd.to_datetime(filtered['data_acidente'])
filtered['ano'] = filtered['data_acidente'].dt.year
filtered['mes'] = filtered['data_acidente'].dt.month
group = filtered.groupby(['ano', 'mes', 'uf_acidente'])['qtde_acidente'].count()

#%%

