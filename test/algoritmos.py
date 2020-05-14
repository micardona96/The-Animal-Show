from random import randint
from timeit import timeit

def sortN(numeros):
    outputArray = [None]*len(numeros)
    countArray = [0]*100

    for numero in numeros:
        countArray[numero - 1] += 1

    for i in range(1,len(countArray)):
        countArray[i] += countArray[i-1]

    for i in range(len(numeros) -1, -1, -1):
        outputArray[countArray[numeros[i] - 1] - 1] = numeros[i]
        countArray[numeros[i] - 1] -= 1

    return outputArray

def sortNxN(numeros):
    """ Algoritmo de ordenamiento burbuja (Complejidad O(N^2)) """
    for i in range(len(numeros)):
        for j in range(len(numeros) - i - 1):
            if numeros[j] > numeros[j+1]:
                numAux = numeros[j+1]
                numeros[j+1] = numeros[j]
                numeros[j] = numAux
    return numeros

def sortNLogN(numeros):
        if len(numeros) < 1:
            return []

        posicionPivot = randint(0, len(numeros) - 1)
        pivot = numeros[posicionPivot]
        left = []
        right = []
        numeros.pop(posicionPivot)

        for i in range(len(numeros)):
            if numeros[i] < pivot:
                left.append(numeros[i])
            else:
                right.append(numeros[i])

        return sortNLogN(left) + [pivot] + sortNLogN(right)


arrayNumeros = [randint(1,100) for i in range(500)]

print('Algoritmo NxN')
print(timeit('sortNxN(arrayNumeros)',globals = globals(), number = 1000) * 1000)

print('Algoritmo N')
print(timeit('sortN(arrayNumeros)',globals = globals(), number = 1000) * 1000)

print('Algoritmo NLogN')
print(timeit('sortNLogN(arrayNumeros)',globals = globals(), number = 1000) * 1000)

