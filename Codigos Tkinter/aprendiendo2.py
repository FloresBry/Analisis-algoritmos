#variables 2.0
datos=("lucas","dalto",1000)
datos_en_lista=["Bry","Flores",10]
#desempaquetado
nombre,apellido,dinero=datos_en_lista
#imprimiendo datos
print(nombre)
print(apellido)
print(dinero)
tupla1=tuple(["dato1","dato2"])
print(tupla1)
tupla3="dato1","dato2"#se crea una dupla
print(tupla3)
tupla3="dato2", # creando una dupla sin parentesis de un solo dato
print(tupla3)
#conjutos
conjunto=set(["dato1","dato2"])
print(conjunto)
#bucle for
animales=["perro", "gato","loro","cocodrilo","pez"]
numeros=[42,23,12,12,32]
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")
#recoriendo la lista numeros
for numero in numeros:
    numero=numero*10
    print(numero)
#recorriendo 2 listas se puede hacer con mas de 2 listas pero que sean del mismo tamanio
for numero,animal in zip(numeros,animales):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
#forma no optima de recorrer una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])
#forma correcta
for num in enumerate(numeros):
    print(num[1])
for num in enumerate(numeros):
    indice=num[0]
    valor=num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
for num,i in enumerate(numeros):
    print(f"el indice es: {i} y el valor es: {num}")
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")

else:
    print("El bucle termino")
frutas=["banana", "pera", "manzana","granadas"]
for fruta in frutas:
    if fruta == "granadas": #si la fruta es granada lo saltamos
        continue
    print(fruta)
for fruta in frutas:
    if fruta == "pera":
        break# si es pera detiene el bucle
    print(fruta)
print("bucle terminado")
#recorrer una cadena
cadena="hOLA BRY"
for letra in cadena:
    print(letra)
numeros= [2,5,8,10]
#for en una sola linea de codigo
numeros_duolicados=list()
for numero in numeros:
    numeros_duolicados.append(numero*2)
    
print(numeros_duolicados)
#duplicamos los numeros el for de arriba hace lo mismo que este for
numeros_duolicados=[x*2 for x in numeros]
print(numeros_duolicados)
#bucle while
contador=0
while contador<18:#de 0 a 17
    print(contador)
    contador+=1
print("el while llego a su fin")
#funciones integradas
 
 #encontraddo el numero mayor de una lista
numeros=[4,7,5,3,2]
numero_mas_alto=max(numeros)
print(numero_mas_alto)
#encontrando el numero menor
numero_menor=min(numeros)
print(numero_menor)
#redondeando a 6 decimales con la funcion round
numero= round(12.345,3)
print(numero)

#retorno False -> 0 vacio, False, ninguno
resultado_booleano=bool(True)
print(resultado_booleano)
#retorna True, si todos los valores son verdaderos
resultado_all=all([1213,"true",[]])
print(resultado_all)
#sum suma todos los valores de un iterable
suma=sum(numeros)
print(suma)
#creando propias funciones
def saludar():
    print("Hola lucas mi maestro como andas?")
#funcion con parametros
def saludar(nombre,sexo):
    sexo=sexo.lower()
    if sexo=="mujer":
        adjetivo="amiga"
    elif sexo=="hombre":
        adjetivo="amigo"
    else:
        adjetivo="amigue"
    print(f"Hola {nombre}, como estas {adjetivo}?")


nombre=input("Ingresa el nombre: ")
sexo=input("Ingresa el sexo: ")
saludar(nombre,sexo)

#crear una funcion que me retorne valores
def contrasena_random(num):
    chars="abcdefghij"

    num_entero=str(num)
    num=int(num_entero[0])#obtenemos de un numero de mas de dos diitos solo el primer digito
    c1=num-2
    c2=num
    c3=num-5
    contrasenia=f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasenia

crear_contrasenia=contrasena_random(10)
print(crear_contrasenia)
#crear una funcion que retorna multiples valores
def contrasena_random2(num):
    chars="abcdefghij"

    num_entero=str(num)
    num=int(num_entero[0])#obtenemos de un numero de mas de dos diitos solo el primer digito
    c1=num-2
    c2=num
    c3=num-5
    contrasenia=f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasenia,num
#desempaquetando la funcion
password,primernumero=contrasena_random2(10)
print(type(password))
print(primernumero)
#esto no esta muy bien
def suma(lista):
    numeros_sumados=0
    for numero in lista:
        numeros_sumados=numeros_sumados+numero
    return numeros_sumados

resultado=suma([3,4,3])
#utilizando el parametro args
def suma2(*numeros):
    return sum(numeros)
resultado=suma2(4,3,3)
print(resultado)

def frase(nombre, apellido, adjetivo="tonta"): # aqui definimos un valor a adjetivo pero podemos cambiarlo
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"
#parametros posicionales
frase_resultante=frase("bryan","flores","guapa")
print(frase_resultante)
#forzamos argumentos acomodamos
frase_resultante2=frase(adjetivo="bryan",nombre="flores",apellido="guapa")
print(frase_resultante2)
#funciones lambda
multiplicar_por_dos =lambda x :x*2
# la funcion de arriba es igual a esto
# def multiplicar_por_dos(x):
#   return x*2
print(multiplicar_por_dos(5))
