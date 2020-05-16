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


print('\033[94m' + '\n--- RESULTADOS DEL TEST (seconds) ---' + '\033[0m')
print('Array size in test ' + sys.argv[1] + ":\n")

print("Size\tN\tNlogN\tN²")
for k in range(int(sys.argv[1])):
    resultado1 = timeit(
        'sortN([randint(1, k+1) for i in range(k+1)])', globals=globals(), number=1000)

    resultado2 = timeit(
        'sortNLogN([randint(1, k+1) for i in range(k+1)])', globals=globals(), number=1000)

    resultado3 = timeit(
        'sortNxN([randint(1, k+1) for i in range(k+1)])', globals=globals(), number=1000)

    print(str(k+1) + "\t" + str(round(resultado1, 4)) + "\t" +
          str(round(resultado2, 4)) + "\t" + str(round(resultado3, 4)))


