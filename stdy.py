import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datadf = pd.read_csv('acidentesdf.csv')
datasp = pd.read_csv('acidentessp.csv')

x = list(datadf.columns.values)
y = list(datasp.columns.values)

for i in range(len(x)):
    if x[i] not in y:
        columname = x[i]
        del datadf[columname]
        
datadf.iloc[1]
        
popsp = 44411238
popdf = 2800000
#%%
datasp = datasp[datasp['Mes'] != 'Total']
datadf = datadf[datadf['Mes'] != 'Total']
plt.figure(figsize = (13,5))
z = list(datasp['2015'])
x = list(datadf['Mes'])
y = list(datadf['2015'])
plt.plot(x, y, z)
plt.show()


