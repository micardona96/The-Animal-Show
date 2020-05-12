class Espectaculo:
    def __init__(self,escenas, animales, partes, apertura, n=9, k=3):
        self.apertura = apertura
        self.partes = partes
        self.escenas = escenas
        self.animales = animales
        self.n = n
        self.k = k

    def maxGradezaEscena(self):
        maxEscena = self.escenas[0]
        for i in range(1, len(self.escenas)):
            if self.escenas[i].totalGrandeza > maxEscena.totalGrandeza:
                maxEscena = self.escenas[i]

        print('La escena de mayor grandeza total fue:')
        print(maxEscena)

    def minGradezaEscena(self):
        minEscena = self.escenas[0]
        for i in range(1, len(self.escenas)):
            if self.escenas[i].totalGrandeza < minEscena.totalGrandeza:
                minEscena = self.escenas[i]

        print('La escena de menor grandeza total fue:')
        print(minEscena)

    def maxParticipacionAnimal(self):
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

    def sortN(self):
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

    def main(self):
        for escenas in self.escenas:
            escenas.sortN()

        self.apertura.sortN()
        
        for parte in self.partes:
            parte.sortN()

        print('Apertura:')
        print(self.apertura)
        print('\n')

        self.sortN()
        print(self)

        self.maxParticipacionAnimal()
        print('\n')
        self.minParticipacionAnimal()
        print('\n')
        self.minGradezaEscena()
        print('\n')
        self.maxGradezaEscena()

    def __str__(self):
        description = ''
        for parte in self.partes:
            description += str(parte) + '\n\n'
        return description

