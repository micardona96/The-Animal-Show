from random import randint

class Parte:
    n = None
    def __init__(self, escenas=[]):
        self.escenas = escenas
    
    def getGrandezaTotal(self):
        """ Algortimo para sumar la cantidad total de grandeza de una parte (suma de todas sus escenas)
            Complejidad Constante O(1)
        """
        contador = 0
        for escena in self.escenas:
            contador += escena.getGrandezaTotal()
        return contador

    def sortNxN(self):
        """ Algoritmo de ordenamiento burbuja (Complejidad O(N^2)) """
        for i in range(len(self.escenas)):
            for j in range(len(self.escenas) - i - 1):
                if self.escenas[j].getGrandezaTotal() > self.escenas[j+1].getGrandezaTotal():
                    escenaAux = self.escenas[j+1]
                    self.escenas[j+1] = self.escenas[j]
                    self.escenas[j] = escenaAux

    def sortNLogN(self, arrayEscenas):
        """ Algoritmo de ordenamiento QuickSort con complejidad O(NLogN), pivote seleccionado aleatoriamente """
        if len(arrayEscenas) < 1:
            return []

        posicionPivot = randint(0, len(arrayEscenas) - 1)
        pivot = arrayEscenas[posicionPivot]
        left = []
        right = []
        arrayEscenas.pop(posicionPivot)

        for i in range(len(arrayEscenas)):
            if arrayEscenas[i].getGrandezaTotal() < pivot.getGrandezaTotal():
                left.append(arrayEscenas[i])
            else:
                right.append(arrayEscenas[i])

        return self.sortNLogN(left) + [pivot] + self.sortNLogN(right)

    def quickSort(self):
        """ Función auxiliar que ayuda a ejecutar el algoritmo quicksort recursivamente """
        self.escenas = self.sortNLogN(self.escenas)

    def sortN(self):
        """ Algoritmo de ordenamiento Counting Sort (Complejidad O(N))  """
        maxGrandezaEscena = Parte.n + (Parte.n-1) + (Parte.n-2)
        outputArray = [None]*len(self.escenas)
        countArray = [0]*maxGrandezaEscena

        for escena in self.escenas:
            countArray[escena.getGrandezaTotal() - 1] += 1
        
        for i in range(1,len(countArray)):
            countArray[i] += countArray[i-1]

        for i in range(len(self.escenas)-1, -1, -1):
            outputArray[countArray[self.escenas[i].getGrandezaTotal() - 1] - 1] = self.escenas[i]
            countArray[self.escenas[i].getGrandezaTotal() - 1] -= 1

        self.escenas = outputArray 
        
    
    def __str__(self):
        description = []
        for escena in self.escenas:
            description.append(str(escena))
        return str(description)