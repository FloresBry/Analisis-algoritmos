import numpy as np
import matplotlib.pyplot as plt
valores=[7,10,15,9]
valores2=[8,13,11,12]
etiquetas=['a','b','c','d']
co=np.arange(len(valores))
an=.9
fig, ax=plt.subplots()
ax.bar(co,valores,an,label='Azules')
ax.set_title("Graficos de barras")
ax.set_ylabel("Numeros")
ax.set_xlabel("otros numeros")
ax.set_xticks(co)
ax.set_xticklabels(etiquetas)
ax.annotate('hola',xy=(0,0))
plt.show()