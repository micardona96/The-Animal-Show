class Espectaculo:
    def __init__(self,escenas, partes, apertura, n=9, k=3):
        self.apertura = apertura
        self.partes = partes
        self.escenas = escenas
        self.n = n
        self.k = k



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

    def __str__(self):
        description = ''
        for parte in self.partes:
            description += str(parte) + '\n\n'
        return description

