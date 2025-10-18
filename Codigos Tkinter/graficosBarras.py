import matplotlib.pyplot as plt
import numpy as np
from random import sample
#Datos
listanum=list(range(100))
listanum=sample(listanum,5)
categorias=['A','B','C','D','E']
valores=[1,5,2,8,3]
colores=['blue','blue','blue','blue','blue']
#colores[1]='yellow'
total=sum(listanum)
porcentajes=[valor/total*100 for valor in listanum]

print(listanum)
plt.figure(figsize=(5,5))
plt.bar(categorias,listanum,color=colores,width=1,)
plt.xlabel('Categorias',fontsize=10)
plt.ylabel('Valores',fontsize=10)
plt.tick_params(axis='both',labelsize=8.5)
plt.ylim=(0,110)
for i, (valor, porcentajes) in enumerate(zip(listanum,porcentajes)):
    plt.text(i,valor,f'{valor}\n{porcentajes:.1f}%',ha='center', fontsize=8)
plt.show()