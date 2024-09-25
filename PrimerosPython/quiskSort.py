import random
def quickSort(A, p, r):
    if p < r: #Si tiene al menos 2 elementos
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def partition(A, p, r):
    x = A[r] #Asignar el pivote en la úlltima posición
    i = p - 1
    for j in range (p, r):
        if A[j] <= x:
            i += 1
            exchange(A, i, j)
    exchange(A, i+1, r)
    return i + 1 #retorna la posición ya ordenada del pivote

def exchange(A, i, j):
    A[i], A[j] =  A[j], A[i]

def main():
    print("Quick sort")
    n = 0000
    array = [random.randint(1,100) for i in range (n)]
    #print(f'Desordenado {array}')

    quickSort(array, 0, len(array)-1)
   # print(array)

if __name__ == '__main__':
    main()