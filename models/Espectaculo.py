from random import randint

class Espectaculo:
    def __init__(self,escenas, animales, partes, apertura, n=9, k=3, m=4):
        self.apertura = apertura
        self.partes = partes
        self.escenas = escenas
        self.animales = animales
        self.n = n
        self.k = k
        self.m = m

    def promedioGradezaEspectaculo(self):
        """ Algoritmo para calcular el promedio del espectaculo (escenas) con complejidad O(k) (número de escenas)"""
        contador = 0
        for escena in self.escenas:
            contador += escena.totalGrandeza
        contador *= 2

        promedio = contador / (((self.m -1) * self.k) * 2)

        print('El promedio de grandeza total del espectaculo fue de:')
        print(round(promedio,2))

    def maxGradezaEscena(self):
        """ Algoritmo para calcular la escena con mayor grandeza con complejidad O(k) (número de escenas)"""
        maxEscena = self.escenas[0]
        for i in range(1, len(self.escenas)):
            if self.escenas[i].totalGrandeza > maxEscena.totalGrandeza:
                maxEscena = self.escenas[i]

        print('La escena de mayor grandeza total fue:')
        print(maxEscena)

    def minGradezaEscena(self):
        """ Algoritmo para calcular la escena con menor grandeza con complejidad O(k) (número de escenas)"""
        minEscena = self.escenas[0]
        for i in range(1, len(self.escenas)):
            if self.escenas[i].totalGrandeza < minEscena.totalGrandeza:
                minEscena = self.escenas[i]

        print('La escena de menor grandeza total fue:')
        print(minEscena)

    def maxParticipacionAnimal(self):
        """ Algoritmo para calcular los animales con mayor participación en escenas. Complejidad O(n) (número de animales)"""
        arrayMaxAnimales = []
        maxAnimal = self.animales[0]
        for i in range(1,len(self.animales)):
            if self.animales[i].cantidad > maxAnimal.cantidad:
                maxAnimal = self.animales[i]
            elif self.animales[i].cantidad == maxAnimal.cantidad:
                arrayMaxAnimales.append(self.animales[i])
        
        print('El/Los animales que más partició/participaron en escenas fueron: ')
        if len(arrayMaxAnimales) == 0:
            print(maxAnimal.nombre + " con " + str(maxAnimal.cantidad * 2) + " escenas")
        else:
            for animal in arrayMaxAnimales:
                print(animal.nombre + " con " + str(animal.cantidad * 2) + " escenas")
            print(maxAnimal.nombre + " con " + str(animal.cantidad * 2) + " escenas")

    def minParticipacionAnimal(self):
        """ Algoritmo para calcular los animales con menor participación en escenas. Complejidad O(n) (número de animales)"""
        arrayMinAnimales = []
        minAnimal = self.animales[0]
        for i in range(1,len(self.animales)):
            if self.animales[i].cantidad < minAnimal.cantidad:
                minAnimal = self.animales[i]
            elif self.animales[i].cantidad == minAnimal.cantidad:
                arrayMinAnimales.append(self.animales[i])
        
        print('El/Los animales que menos partició/participaron en escenas fueron: ')
        if len(arrayMinAnimales) == 0:
            print(minAnimal.nombre + " con " + str(minAnimal.cantidad * 2) + " escenas")
        else:
            
            for animal in arrayMinAnimales:
                print(animal.nombre + " con " + str(animal.cantidad * 2) + " escenas")
            print(minAnimal.nombre + " con " + str(animal.cantidad * 2) + " escenas")

    def sortNxN(self):
        """ Algoritmo de ordenamiento burbuja (Complejidad O(N^2)) """
        for i in range(len(self.partes)):
            for j in range(len(self.partes) - i - 1):
                if self.partes[j].getGrandezaTotal() > self.partes[j+1].getGrandezaTotal():
                    parteAux = self.partes[j+1]
                    self.partes[j+1] = self.partes[j]
                    self.partes[j] = parteAux

    def sortNLogN(self, arrayPartes):
        """ Algoritmo de ordenamiento QuickSort con complejidad O(NLogN), pivote seleccionado aleatoriamente """
        if len(arrayPartes) < 1:
            return []

        posicionPivot = randint(0, len(arrayPartes) - 1)
        pivot = arrayPartes[posicionPivot]
        left = []
        right = []
        arrayPartes.pop(posicionPivot)

        for i in range(len(arrayPartes)):
            if arrayPartes[i].getGrandezaTotal() < pivot.getGrandezaTotal():
                left.append(arrayPartes[i])
            else:
                right.append(arrayPartes[i])

        return self.sortNLogN(left) + [pivot] + self.sortNLogN(right)
    
    def quickSort(self):
        """ Función auxiliar que ayuda a ejecutar el algoritmo quicksort recursivamente """
        self.partes = self.sortNLogN(self.partes)

    def sortN(self):
        """ Algoritmo para ordenar las partes del espectaculo con Complejidad O(n) utilizando el algoritmo CountingSort"""
        maxGrandezaParte = (self.n + (self.n - 1) + (self.n - 2))*self.k
        outputArray = [None]*len(self.partes)
        countArray = [0]*maxGrandezaParte

        for parte in self.partes:
            countArray[parte.getGrandezaTotal() - 1] += 1

        for i in range(1,len(countArray)):
            countArray[i] += countArray[i-1]

        for i in range(len(self.partes)-1, -1, -1):
            outputArray[countArray[self.partes[i].getGrandezaTotal() - 1] - 1] = self.partes[i]
            countArray[self.partes[i].getGrandezaTotal() - 1] -= 1
        
        self.partes = outputArray 

    def main(self, algoritmo='N'):
        if algoritmo == 'N':
            for escena in self.escenas:
                escena.sortN()
            for parte in self.partes:
                parte.sortN()
            self.apertura.sortN()
            self.sortN()        
        elif algoritmo == 'NxN':
            for escena in self.escenas:
                escena.sortNxN()
            for parte in self.partes:
                parte.sortNxN()
            self.apertura.sortNxN()               
            self.sortNxN()
        elif algoritmo == 'NLogN':
            for escena in self.escenas:
                escena.quickSort()
            for parte in self.partes:
                parte.quickSort()
            self.apertura.quickSort()
            self.quickSort()

        
        
        # print('Apertura:')
        # print(self.apertura)
        # print('\n')
        #print(self)

        # self.maxParticipacionAnimal()
        # print('\n')
        # self.minParticipacionAnimal()
        # print('\n')
        # self.minGradezaEscena()
        # print('\n')
        # self.maxGradezaEscena()
        # print('\n')
        # self.promedioGradezaEspectaculo()

    def __str__(self):
        description = ''
        for i in range(len(self.partes)):
            description += "parte " + str(i+1)+ "\n" + str(self.partes[i]) + '\n\n'
        return description

