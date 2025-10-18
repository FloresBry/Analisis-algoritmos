import matplotlib.pyplot as plt
import numpy as np
x0 = np.arange(0,1050,50)
print(x0)
x=np.linspace(0,1000,21)
print(x)
#datos
y=np.sin(x)
y2=np.cos(x)
y3=x
y4=x**(1/2)
#esta linea siempre debe ir prmero para modificar el tamanio del grafico
plt.figure(figsize=(7,5))
#funciones( lw -l ine weight | ms =marker size (tamanio bolitas))
plt.plot(x,y,'*',label="f(x)=sen(x)",color="indigo",lw=10,ms=1)
plt.plot(x,y2,"--",label="f(x)=cos(x)",color="steelblue",lw=0.7)
plt.legend(loc='lower right',fontsize=8,ncol=2,edgecolor='indigo')#posicion de mi etiqueta
#titulos y nombres ejes
plt.title("Ondas", fontsize=12)
plt.xlabel("Tiempo (s)",fontsize=10)
plt.ylabel("Rango(m)",fontsize=10)
#limites de los ejes
plt.xlim(0,25)
plt.ylim(-1.60,1)
#tamanio de los numeros de los ejes
plt.tick_params(axis='both',labelsize=10)
#mostrar
plt.grid(True)
plt.show()