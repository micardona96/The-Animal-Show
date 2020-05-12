class Escena:

    def __init__(self, animales=[], n=9):
        self.animales = animales
        self.n = n

    def aumentarCantidad(self):
        """ Aumenta en 1 la cantidad de apariciones de los animales que participan en la escena Complejidad O(1)"""
        for animal in self.animales:
            animal.cantidad += 1

    def getGrandezaTotal(self):
        """ Calculo de la grandeza total de la escena (Complejidad O(N)) """
        contador = 0
        for animal in self.animales:
            contador += animal.grandeza

        return contador

    def sortNxN(self):
        """ Algoritmo de ordenamiento burbuja (Complejidad O(N^2)) """
        for i in range(len(self.animales)):
            for j in range(len(self.animales) - i - 1):
                if self.animales[j].grandeza > self.animales[j+1].grandeza:
                    animalAux = self.animales[j+1]
                    self.animales[j+1] = self.animales[j]
                    self.animales[j] = animalAux
    
    def sortN(self):
        """ Algoritmo de ordenamiento Counting Sort (Complejidad O(N))  """
        outputArray = [None]*3
        countArray = [0]*self.n
        for animal in self.animales:
            countArray[animal.grandeza - 1] += 1

        for i in range(1,len(countArray)):
            countArray[i] += countArray[i-1]

        for i in range(len(self.animales)-1, -1, -1):
            outputArray[countArray[self.animales[i].grandeza - 1] - 1] = self.animales[i]
            countArray[self.animales[i].grandeza - 1] -= 1
        
        self.aumentarCantidad()

        self.animales = outputArray


    def __str__(self):
        description = []
        for animal in self.animales:
            description.append(str(animal))
        return str(tuple(description))      