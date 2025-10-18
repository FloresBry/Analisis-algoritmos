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

def hacer_inversa(lista):
    lista_aux=list(lista)
    j=len(lista)-1
    i=0
    while i<len(lista):
        lista[i]=lista_aux[j]
        i=i+1
        j=j-1
    
def intercambio(lista,j,elemento):
    
    lista.insert(j,elemento)
    

def generador_permutas(lista):
    global permutas
    global num
    permutas.append(list(lista))
    num=1
    lista_aux=list(lista)

    while num != factorial(len(lista)) :
        
        for i in range(0,len(lista)):
            
            
            for j in range(0, len(lista)):
                lista_aux=list(lista)
                lista_aux2=list(lista)
                elemento=lista_aux[i]
                lista_aux.remove(lista_aux[i])
                intercambio(lista_aux,j,elemento)
                hacer_inversa(lista_aux2)
                lista_aux2.remove(lista[i])
                intercambio(lista_aux2,j,elemento)
                condicion(lista_aux2)
                print(num)
                print(permutas)


        
                
                                  


                    

lista=[]
generador_permutas(lista);
print(f"Permutas Posibles {num} son: {permutas}")