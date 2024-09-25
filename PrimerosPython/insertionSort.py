import random 

#SORT IN PLACE (Se ordena en el mismo arreglo, no es necesario returnear nada)
def insertionSort(array):
    # Consideramos el 1er elemento ya ordenado
    for j in range(1, len(array)):
        key = array[j]  # Inserción
        i = j - 1

        # Reacomodamos
        while i >= 0 and array[i] > key: #En algoritmo dice ">"
            array[i + 1] = array[i]
            i = i - 1

        # Insertamos el elemento en su posición correcta
        array[i + 1] = key


def miMain():
    arr = [12, 11, 13, 5, 6, 44, 9, -100]
    arr = [random.randint(10,100) for i in range(10)] #list comprehension
    err = [i                      for i in range(1,9)]
    
    print("Arreglo original:", arr)
    insertionSort(arr)
    print("Arreglo ordenado:", arr)
    print(err)

if __name__ == "__main__":
    miMain()
    
"""
arr = [random.randint(10,500) for i in range(1)] #list comprehension
eee = [i for i in range(1,9)]
    
print("Arreglo original:", arr)
insertionSort(arr)
print("Arreglo ordenado:", arr)
print(eee)
"""