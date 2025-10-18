cadena="hola como estas?"
cadena2 = "Bienvenido maquinola"
resultado= cadena.capitalize()
resultado=cadena.find("d")
resultado=cadena.isnumeric()
resultado=cadena.isalpha()
resultado=cadena.count("a")
resultado=len(cadena)
resultado=cadena.startswith("ho")
resultado=cadena.endswith("?")
resultado=cadena.replace("hola","adios")
resultado=cadena.split(" ")
print(resultado)
lista=list([33,100,34])
resultado=len(lista)
lista.append(30)
lista.insert(2,12)
print(lista)
lista.extend([11,32])
lista.pop(-1)
lista.remove(12)
#lista.clear()
lista.sort()
lista.sort(reverse=True)
lista.reverse()
diccionario= {
    "nombre": "Bryan",
    "apellido": "Flores",
    "Edad": 20
}
claves= diccionario.get("nombre")
#diccionario.clear()

diccionario.pop("nombre")
diccionario_iterable=diccionario.items()
print(diccionario_iterable)
#pedirle un dato al usuario
#nombre=input("Dame tu nombre: ")
#numero=input("dame un numero: ")
#resultado= int(numero)*2
print(resultado)

#promedio de duracion
otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_promedio=4
dalto_curso=1.5
#duracion de crudos
crudo_dalto=3.5
crudo_promedio=5
#diferencia de duracion

diferencia_con_min=100-dalto_curso/otros_cursos_min*100
diferencia_con_max=100-dalto_curso*1000//otros_cursos_max/10
diferencia_con_promedio=100-dalto_curso/otros_cursos_promedio*100
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento")
print(f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio")
print("------------------------------")
#calculando tiempo vacio
tiempo_vacio_promedio=100-otros_cursos_promedio*1000//crudo_promedio/10
tiempo_vacio_dalto=100-dalto_curso*1000// crudo_dalto/10
print(f"Un curso promedio el {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este curso elimino e {tiempo_vacio_dalto}% de tiempo vacio")
print("------------------------------")
#mostrando diferencias si los cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio*100//dalto_curso/10} horas de otros cursos")
print(f"Ver 10 horas de otros curso equivale a ver {dalto_curso*100//otros_cursos_promedio/10} horas de otros cursos")
print("------------------------------")

print("EJERCICIO 2")
frase=input("Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")
palabras_separadas=frase.split(" ")
cantidad_de_palabras=len(palabras_separadas)
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos")
print(f"Dalto lo diria en {cantidad_de_palabras*100//2*1.3/100} segundos en decirlo")
if cantidad_de_palabras > 120:
    print("Son un monton de palabras")
    