import random
import math

def mergeSort (A, p, r):
    """"
    :A: int - Array
    :p: int - Primera pos del arreglo
    :r: int - Última pos del arreglo
    """
    if (p < r):  #El array tiene al menos 2
        #print(f'MergeSort: {A[p:r+1]} p={p} r={r}')
        q = math.trunc((p + r) / 2)
        mergeSort (A, p, q) #Mitad izquierda ordena
        mergeSort (A, q + 1, r) #Mitad derecha ordena
        merge (A, p, q, r)
    #else:
        #print(f'Base: {A} p={p} r={r}')

        

def merge(A, p, q, r):
    """"
    :A: int - Array
    :p: int - Primera pos del arreglo
    :q: int - Posicion a la mitad
    :r: int - Última pos del arreglo
    """
    L = []
    R = []

    for i in range(p, q + 1):
        L.append(A[i])
        
    for j in range(q + 1, r + 1):
        R.append(A[j])

    print(f'Left: {L}')
    print(f'Right: {R}')

    i = 0
    j = 0
    k = p

    while i < len(L) and j < len(R):
        if(L[i] <= R[j]):
            A[k] = L[i]
            i = i + 1  
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1
        print("1",A)

    while i < len(L): # Lista izquierda aún tiene elementos
       A[k] = L[i]
       i += 1
       k += 1
       print("segundo while", A)
    print("2",A)

    while j < len(R): # Lista izquierda aún tiene elementos
       A[k] = R[j]
       j += 1
       k += 1
       print("tercer while", A)
    print("3",A)


def main():
    print("Merge sort")
    n = 8
    #array = [random.randint(10, 100) for i in range (n)] #LIST COMPREHENSION
    array = [9,8,7,86,5,4,96,2,55555,-9999,1,86]
    print(array)
    mergeSort(array, 0, len(array)-1)
    print(array)

if __name__ == "__main__":
    main()