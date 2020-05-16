from random import randint
from timeit import timeit
import sys


def sortN(numeros):
    outputArray = [None]*len(numeros)
    countArray = [0]*int(sys.argv[1])

    for numero in numeros:
        countArray[numero - 1] += 1

    for i in range(1, len(countArray)):
        countArray[i] += countArray[i-1]

    for i in range(len(numeros) - 1, -1, -1):
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


[randint(1, int(sys.argv[1])) for i in range(int(sys.argv[1]))]
print('\033[94m' + '\n--- RESULTADOS DEL TEST (seconds) ---' + '\033[0m')
print('Array size in test: ' + sys.argv[1])

resultado1 = timeit(
    'sortN([randint(1, int(sys.argv[1])) for i in range(int(sys.argv[1]))])', globals=globals(), number=1000)
print('Solución O(N)  \t \t' + str(resultado1))

resultado2 = timeit(
    'sortNLogN([randint(1, int(sys.argv[1])) for i in range(int(sys.argv[1]))])', globals=globals(), number=1000)
print('Solución O(N log N)  \t' + str(resultado2))

resultado3 = timeit(
    'sortNxN([randint(1, int(sys.argv[1])) for i in range(int(sys.argv[1]))])', globals=globals(), number=1000)
print('Solución O(N²) \t \t' + str(resultado3) + '\n')
