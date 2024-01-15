
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dataset.csv')
#%%
#Questão 1
new = df[df['Categoria'] == 'Office Supplies'] 
valor = new.groupby('Cidade')['Valor_Venda'].sum()
valor = valor.to_frame()
arr = np.array(valor)
maior = 0
for i in range(len(arr)):
    if arr[i] > maior:
        maior = arr[i]
        index = i 
        
maior = int(maior[0])        
print('a cidade com maior valor em vendas foi',valor.index[index], 'com', maior,'vendas')
#%%
#Questão 2
new = df.groupby('Data_Pedido')['Valor_Venda'].sum()
new.head()
plt.figure(figsize = (25,9))
new.plot(x = 'Data_Pedido', y = 'Valor_venda', color = 'g')
plt.xlabel('Request Day')
plt.ylabel('Sale Value')
plt.title ('Sales per Request Day')

#%%
#Questão 3
new = df.groupby('Estado')['Valor_Venda'].sum()


plt.figure(figsize = (30,10))
new.plot(kind = 'bar',x = 'Estado', y = 'Valor_Venda', color = 'red')
#%%
#Questão 4
new = df.groupby('Cidade')['Valor_Venda'].sum()
pf = new.to_frame()
pf.sort_values('Valor_Venda', ascending = False, inplace = True)
top10 = pf.head(10)

newarr = np.array(top10.index)
top10['Cidade'] = newarr 
top10.plot(kind = 'bar', x = 'Cidade', y = 'Valor_Venda')
plt.title('top 10 cities with biggest total value in sales')
#%%
#Questão 5
seg = df.groupby('Segmento')['Valor_Venda'].sum()
newarr = np.array(seg.to_frame())
maior = 0
fig, ax = plt.subplots(figsize=(5, 5))
pie = seg.plot.pie(startangle=170, explode=explode, shadow=True, ax  =ax)

centre_circle = plt.Circle((0,0),0.65,fc='white')  
ax.add_patch(centre_circle)


plt.ylabel('Total Sales per Segment')
plt.title(f"{int(maior[0])} {seg.to_frame().index[index]}")


plt.show()

print(int(maior[0]), seg.to_frame().index[index])

#%%

#Questão 6
#df['Ano'] = df['Data_Pedido'].str[-4:]
df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], dayfirst = True)

#teste1 = df.groupby(['Ano','Segmento'])['Valor_Venda'].sum()
