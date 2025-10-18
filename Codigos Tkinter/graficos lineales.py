import matplotlib.pyplot as plt
fuente1={'family': 'monospace','style':'italic','weight':'bold','color':'aqua','size':15}
fuente2={'family': 'monospace','style':'italic','weight':'bold','color':'deeppink','size':15}
x=list(range(9))
y=[i**2 for i in x]
# grafica sencilla
plt.plot(x,y, color='deeppink', linestyle='dashed',linewidth=2, marker='p', markersize=15, markerfacecolor='yellow', markeredgecolor='cyan', label="x**2")
plt.legend(loc='lower right')#ubicacion de la etiqueta
plt.xlabel('Eje de las x',fontdict=fuente2)
plt.ylabel('eje de las y',fontdict=fuente2)
plt.title("Mi primer grafica",fontdict=fuente1, loc='right')
plt.xticks(fontsize=15, color='red', family='sans-serif')
plt.yticks(fontsize=15, color='red', family='sans-serif')
fig=plt.figure()
#creando grafica con objeto ax
ax=plt.axes()
ax.plot(x,y,c='deeppink',ls='dashed',lw=2,marker='p',markersize=10,markerfacecolor='yellow',markeredgecolor='cyan',label='x**2')
plt.legend(loc='lower right')
ax.set_facecolor('orange')
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('deeppink')
ax.spines['right'].set_color('red')
ax.spines['top'].set_color('green')
#marcar un punto en la grafica
plt.axhline(20)
plt.axvline(4)
#sombreado en la parte horizontal que va del punto 30 a 40
plt.axhspan(30,40,color='pink',alpha=0.9)
#sombreado vertical que va del punto 5 a 7 
plt.axvspan(5,7,color='pink',alpha=0.9)
#para dejar un texto en una cordenada definida
plt.text(5,10,'Gráfica',fontdict=fuente2)
#caja de texto
ax.text(1, 60, 'Esto es una caja de texto', style='italic',
       bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
#marcar una cordenada en particular, hacer un punto
ax.plot([1], [10], 'o')
#hacer una flecha que marque a una coordenada y con un texto
ax.annotate('Este es el punto', xy=(1,10), xytext=(4,30),
           arrowprops=dict(facecolor='black', shrink=0.03))
#ponemos una ecuacion
ax.text(2,40,r'an equation: $E=mc^2$',fontsize=15)
#subtitulo

fig.suptitle('texto centrado en matplotlib', fontsize=14,fontweight='bold')

plt.grid(True)

plt.show()