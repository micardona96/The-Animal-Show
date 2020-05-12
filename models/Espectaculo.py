class Espectaculo:
    def __init__(self, partes, apertura, n=9, k=3):
        self.apertura = apertura
        self.n = n
        self.k = k

   # cantidad de elementos del espectaculo
        self.partes = partes


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


    def __str__(self):
        description = ''
        for parte in self.partes:
            description += str(parte) + '\n\n'
        return description

