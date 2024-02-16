import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

datag = pd.read_csv('acidentes.csv', delimiter = ';')

#%%



estados = ['DF', 'SP', 'MG', 'GO']
filtered = datag[datag['uf_acidente'].isin(estados)]
n = filtered.columns

columns_to_drop = ['ind_guardrail', 'ind_acostamento','bairro_acidente','end_acidente','cep_acidente', 'tp_pavimento','tp_acidente', 'tp_cruzamento', 'chv_localidade']

filtered = filtered.drop(columns=columns_to_drop)
datag = datag.drop(columns = columns_to_drop)
def mautopct(values):
    def sub(pct):
        total = sum(values)
        val = int(round(pct * total / 100))
        return '{p:.1f}%'.format(p=pct, v=val)
    return sub
#%%
filtered['data_acidente'] = pd.to_datetime(filtered['data_acidente'])
filtered['ano'] = filtered['data_acidente'].dt.year
filtered['mes'] = filtered['data_acidente'].dt.month

datag['data_acidente'] = pd.to_datetime(datag['data_acidente'])
datag['ano'] = datag['data_acidente'].dt.year
datag['mes'] = datag['data_acidente'].dt.month
#%%
totalaci = filtered['qtde_acidente'].sum()
totalobi = filtered['qtde_acid_com_obitos'].sum()
datadf = filtered[filtered['uf_acidente'] == 'DF']
datasp = filtered[filtered['uf_acidente'] == 'SP']
datamg = filtered[filtered['uf_acidente'] == 'MG']
datago = filtered[filtered['uf_acidente'] == 'GO']
datab = datag[~datag['uf_acidente'].isin(['DF', 'SP', 'MG', 'GO'])]
totaldf = datadf['qtde_acidente'].sum()
totalsp = datasp['qtde_acidente'].sum()
totalmg = datamg['qtde_acidente'].sum()
totalgo = datago['qtde_acidente'].sum()
totalb = datab['qtde_acidente'].sum()
estados = ['DF', 'SP', 'MG','GO', "OUTRAS UF'S"]
plt.figure(figsize = (20,6))
explode = (0.09,0,0, 0,0)
y = np.array([totaldf,totalsp,totalmg,totalgo, totalb])

colors = ('brown', 'royalblue', 'orange','yellow', 'darkgreen')

plt.pie(y, labels=estados, explode=explode, autopct=mautopct(list(y)),textprops={'fontsize': 13},colors = colors,pctdistance = 0.7, shadow = False, startangle = 30)
centre_circle = plt.Circle((0, 0), 0.30, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.gca().set_title("Acidentes de trânsito ", fontsize = 17)
plt.show()
#%%

filtered = filtered[~filtered['ano'].isin([2018, 2019, 2023])]
datag = datag[~datag['ano'].isin([2018, 2019, 2023])]


outras_ufs = datag.groupby(['ano', 'mes'])['qtde_acidente'].agg([np.sum]).reset_index()
outras_ufs['uf_acidente'] = "TODAS UF'S"


dff = filtered.groupby(['ano', 'mes', 'uf_acidente'])['qtde_acidente'].agg([np.sum])


dff = dff.reset_index()

dff = pd.concat([dff, outras_ufs])
plt.figure(figsize=(12, 6))
sns.set()

fig1 = sns.relplot(
    kind='line',
    data=dff,
    y='sum',
    x='mes',
    hue='uf_acidente',aspect = .8,
    col='ano', col_wrap = 3
    
)
fig1.set(ylabel = 'Quantidade de Acidents')




plt.show()
#%%

