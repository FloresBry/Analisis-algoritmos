import random
def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def generador_permutas_fuerza_bruta(lista):
    permutas = []
    n = len(lista)
    
    while len(permutas) < factorial(n):
        nueva_lista = list(lista)
        random.shuffle(nueva_lista)
        
        if nueva_lista not in permutas:
            permutas.append(nueva_lista)
            print(f"Permutación encontrada: {nueva_lista}") 
            
    return permutas


mi_lista = [1,2,3,4,5,6,7,8] 
todas_las_permutaciones = generador_permutas_fuerza_bruta(mi_lista)

print("\n---")
print(f"Total de permutaciones encontradas: {len(todas_las_permutaciones)}")
print(f"Permutaciones finales: {todas_las_permutaciones}")