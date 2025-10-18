#generadores nos permite extraer valores en una funcion y almacenarlos en objetos iterables
#sin la necesidad de alacenar todos a la vez en nuestra computadora

def generaMultiplo7(limite):
    numero=1
    listaNumeros=[]
    while numero<=limite:
        listaNumeros.append(numero*7)
        numero =numero+1
    return listaNumeros

print(generaMultiplo7(10))
#generadores
def generadorMultiplos8 (limite):
    numero=1
    while numero <= limite:
        yield numero *8#la instruccion yield genera un objeto iterable
        numero=numero+1

obtieneMultiplo8=generadorMultiplos8(10)
print(obtieneMultiplo8)
'''
for n in obtieneMultiplo8:
    print(n)
'''
#next() funcion que retorna el siguiente elemento d eun objeto iterable:
print(next(obtieneMultiplo8))
print("300 lineas de codigo")
print(next(obtieneMultiplo8))
print("Aca hay 1000 lineas de codigo")
print(next(obtieneMultiplo8))
#son mas eficientes que las funciones tradicionales
#son utiles con listas de valores infinitos
#entre llamada y llamada del objeto iterable este objeto entra en estado de pausa

def devuelveLenguajes(*lenguajes):# con el asterisco se indica que sse va a recibir un numero indeterminado de parametro ademas 
    # esos parametros se recibiran de forma de tupla
    for leng in lenguajes:
        yield leng

lenguajesObtenidos=devuelveLenguajes("python","Java","PHP","Ruby","javaScript")
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
#esta funcion me obtuvo letra por letra de las cadenas
def devuelveLenguajes2(*lenguajes):
    for leng in lenguajes:
        for letra in leng:
            yield letra
#lo mismo que la funcion de arriba solo que con yiel from
def devuelveLenguaje3(*lenguajes):
    for leng in lenguajes:
        yield from leng
lenguajesObtenidos=devuelveLenguajes2("python","Java","PHP","Ruby","javaScript")
print(next(lenguajesObtenidos))#p
print(next(lenguajesObtenidos))#y
#otros ejemplos con yield
def squares(numbers):
    for number in numbers:
        yield number*number
#esta vez si hacemos la siguiente llamada, no  obtendremos resultados
#si no un generador
numerosCuadrado=squares([1,2,3,4,5,6,7])
print(numerosCuadrado)
print(next(numerosCuadrado))
print(next(numerosCuadrado))
print(next(numerosCuadrado))
print(next(numerosCuadrado))
print(next(numerosCuadrado))
print(next(numerosCuadrado))
print(next(numerosCuadrado))
#print(next(numerosCuadrado))
#otro ejemplo
def testyield():
    yield "Welcome to guru99 python tutoriales"
output=testyield()
print(output)
print(next(output))
def even_numbers(n):
    for x in range(n):
        if (x%2==0):
            yield x
num=even_numbers(10)
print(list(num))#tamien se puede imprimir el generador en forma de lista
