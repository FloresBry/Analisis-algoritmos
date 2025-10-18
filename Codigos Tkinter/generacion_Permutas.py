permutas=[]
num=0
def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return 
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i 
    return resultado

def condicion(lista):
    global permutas
    global num
    encontrado=False
    k=0
    while k< len(permutas):
        
        if permutas[k]==lista:
            encontrado=True  
        k=k+1
    if encontrado==False:
        permutas.append(list(lista))  
        num=num+1


def intercambio(lista,i,j):
    
    lista[i], lista[j]=lista[j], lista[i]
    

def generador_permutas(lista):
    global permutas
    global num
    permutas.append(list(lista))
    num=1

    while num != factorial(len(lista)) :
        
        for i in range(0,len(lista)):
            
            for j in range(1, len(lista)):
                    intercambio(lista,i,j)
                    condicion(lista)
                    if len(lista)>3:
                        for k in range(2, len(lista)):
                            intercambio(lista,i,j)
                            condicion(lista)
                            intercambio(lista,i,k)
                            condicion(lista)
                            intercambio(lista,j,k)
                            condicion(lista)
                            if len(lista)>4:
                                for l in range(3, len(lista)):
                                    intercambio(lista,i,j)
                                    condicion(lista)
                                    intercambio(lista,i,k)
                                    condicion(lista)
                                    intercambio(lista,j,k)
                                    condicion(lista)
                                    intercambio(lista,i,l)
                                    condicion(lista)
                                    intercambio(lista,j,l)
                                    condicion(lista)
                                    intercambio(lista,k,l)
                                    condicion(lista)
                                  


                    

lista=['a','b']
generador_permutas(lista);
print(f"Permutas Posibles {num} son: {permutas}")