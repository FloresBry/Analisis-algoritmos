import matplotlib.pyplot as plt
import numpy as np
#datos
x=np.linspace(0,25,100)
y=np.sin(x)
y2=np.cos(x)
y3=x
y4=x**(1/2)
#se definen cuantos graficos seran y de que tamanio

#ahora se programa cada grafico, parecido a lo que se hizo en graficos.py
fig, axes=plt.subplots(2,2,figsize=(6,6))
#primero
ax=axes[0][0]
#ax.title("seno",fontsize=10)
ax.plot(x,y,'--',color='navy',lw=0.7)
ax.set_xlabel('Tiempo (s)',fontsize=8)
ax.set_ylabel('sen(x)',fontsize=8)
ax.tick_params(axis='both',labelsize=8)
ax.grid(True)
#segundo
ax=axes[0][1]
ax.plot(x,y2,'o--',color='darkred',lw=0.7,ms=3)
ax.set_xlabel('$Tiempo [s]$', fontsize=9)
ax.set_ylabel('$cos(x)$',fontsize=9)
ax.tick_params(axis='both',labelsize=8)
#ax.legend(loc='upper left',fontsize=8,edgecolor='black')
ax.grid(True)


#tercero
ax=axes[1][0]
ax.plot(x,y3,'--',color='deeppink',lw=0.7,label='simiulacion',ms=2)
ax.set_xlabel('Tiempo[S]',fontsize=9)
ax.set_ylabel('$x$',fontsize=9)
ax.tick_params(axis='both',labelsize=8)
ax.legend(loc='upper left',fontsize=8,edgecolor='black')
ax.grid(True)
#cuarto
ax=axes[1][1]
ax.plot(x,y4,'--',color='navy',lw=0.7,ms=2)
ax.set_xlabel('Tiempo[s]',fontsize=8)
ax.set_ylabel('$\sqrt{x}$',fontsize=8)
ax.tick_params(axis='both', labelsize=8)
ax.grid(True)
#se ajustan los parametros de los subplots para que no esten amontonados, los valores de top, bot, left, y right son de aqui
# Cambia los de hspace, wspace para separar
plt.subplots_adjust(hspace=0.4, wspace=0.45)
plt.grid(True)
plt.show()
