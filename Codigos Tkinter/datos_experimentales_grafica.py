import matplotlib.pyplot as plt
import numpy as  np
#datos muestra
x1= np.array([1.98,3.02,5.1,7.64,9.72,11.28])
y1= np.array([20.27,14.08,21.8,-54.56,-103.9,-119.9])
dest1=np.array([4.57,1.99,3.39,7.46,7.81,9.69])
#datos muestra 2
x2= np.array([1.66,2.96,4.8,7.21,10.37,11.54])
y2= np.array([0,-16.39,-31.51,-53.43,-78.97,-94.39])
dest2=np.array([0,7.3,6.43,6.51,6.91,8.19])
#datos muestra 3
x3= np.array([1.61,3.05,5.01,6.43,10.26,11.65])
y3= np.array([35.49,-23.33,-72.36,-87.77,-112.9,-102.31])
dest3=np.array([4.7,5.25,5.72,13.37,14.47,12.53])
#se crea una figura y un solo subplot
fig, ax=plt.subplots(figsize=(7,5))
#graficar datos
ax.errorbar(x1,y1,dest1,fmt='o--',capsize=6,elinewidth=0.75,capthick=0.75,color='navy',lw=0.5,ms=7,label='muestra 1')
ax.errorbar(x2,y2,dest1,fmt='o--',capsize=6,elinewidth=0.75,capthick=0.75,color='red',lw=0.5,ms=7,label='muestra 2')
ax.errorbar(x3,y2,dest1,fmt='o--',capsize=6,elinewidth=0.75,capthick=0.75,color='violet',lw=0.5,ms=7,label='muestra 3')
plt.legend(loc='upper right', fontsize=8,edgecolor='violet')
#Titulos y nombres ejes
ax.set_xlabel('ph',fontsize=8)
ax.set_ylabel('Potencial Zeta(mv)', fontsize=8)
#Limites de ejes
plt.xlim(1,12)
#mostrar
plt.grid(True)
plt.show()