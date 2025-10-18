def merge_sort(arr):
    if len(arr) >1: #si el tamanio del array es mayor a uno
        mid=len(arr)//2 #mide el punto medio del arreglo
        left_half=arr[:mid] #del centro a la izquierda
        right_half=arr[mid:] #del centro a la derecha
        merge_sort(left_half)#se llama recursivamente para volver a dividir los arrays
        merge_sort(right_half)
        merge(arr,left_half,right_half)
    return arr #regresa el arreglo ordenado

def merge(arr, left_half, right_half):
    i=j=k=0
    while i<len(left_half) and j< len(right_half):
        if left_half[i] <right_half[j]:
        
            arr[k]=left_half[i]
            i+=1
        else:
            arr[k]=right_half[j]
            j+=1
        k+=1
    while i<len(left_half):
        arr[k]=left_half[i]
        i+=1
        k+=1
    while j<len(right_half):
        arr[k]=right_half[j]
        j+=1
        k+=1
    
array=[7,38,27,43,3,9,82,10]
sorted_arr=merge_sort(array)
print("Arreglo ordenado: ",sorted_arr)