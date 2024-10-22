from random import randint

class Escena:

    n = None

    def __init__(self, animales=[]):
        self.animales = animales
        self.totalGrandeza = 0

    def aumentarCantidad(self):
        """ Aumenta en 1 la cantidad de apariciones de los animales que participan en la escena Complejidad O(1)"""
        for animal in self.animales:
            animal.cantidad += 1

    def getGrandezaTotal(self):
        """ Calculo de la grandeza total de la escena (Complejidad O(N)) """

        if self.totalGrandeza == 0:
            contador = 0
            for animal in self.animales:
                contador += animal.grandeza
            self.totalGrandeza = contador

        return self.totalGrandeza

    def sortNxN(self):
        """ Algoritmo de ordenamiento burbuja (Complejidad O(N^2)) """
        for i in range(len(self.animales)):
            for j in range(len(self.animales) - i - 1):
                if self.animales[j].grandeza > self.animales[j+1].grandeza:
                    animalAux = self.animales[j+1]
                    self.animales[j+1] = self.animales[j]
                    self.animales[j] = animalAux
        self.aumentarCantidad()
    
    def sortN(self):
        """ Algoritmo de ordenamiento Counting Sort (Complejidad O(N)), se usa para ordenar los animales dentro de las escenas  """
        outputArray = [None]*3
        countArray = [0]*Escena.n
        for animal in self.animales:
            countArray[animal.grandeza - 1] += 1

        for i in range(1,len(countArray)):
            countArray[i] += countArray[i-1]

        for i in range(len(self.animales)-1, -1, -1):
            outputArray[countArray[self.animales[i].grandeza - 1] - 1] = self.animales[i]
            countArray[self.animales[i].grandeza - 1] -= 1
        
        self.aumentarCantidad()

        self.animales = outputArray

    def sortNLogN(self, arrayAnimales):
        """ Algoritmo de ordenamiento QuickSort con complejidad O(NLogN), pivote seleccionado aleatoriamente """
        if len(arrayAnimales) < 1:
            return []

        posicionPivot = randint(0, len(arrayAnimales) - 1)
        pivot = arrayAnimales[posicionPivot]
        left = []
        right = []
        arrayAnimales.pop(posicionPivot)

        for i in range(len(arrayAnimales)):
            if arrayAnimales[i].grandeza < pivot.grandeza:
                left.append(arrayAnimales[i])
            else:
                right.append(arrayAnimales[i])

        return self.sortNLogN(left) + [pivot] + self.sortNLogN(right)

    def quickSort(self):
        """ Función auxiliar que ayuda a ejecutar el algoritmo quicksort recursivamente """
        self.aumentarCantidad()
        self.animales = self.sortNLogN(self.animales)
        

    def __str__(self):
        description = []
        for animal in self.animales:
            description.append(str(animal))
        return str(tuple(description))      