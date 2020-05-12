class Espectaculo:
    def __init__(self, partes, animales=[], escenas=[], apertura=[]):
        self.apertura = apertura

   # cantidad de elementos del espectaculo
        self.partes = partes        # m partes
        self.animales = animales    # n animales
        self.escenas = escenas      # k escenas

    
    def sortN(self):
        outputArray = [None]*len(self.partes)
        countArray = [0]*45

        for parte in self.partes:
            countArray[parte.getGrandezaTotal() - 1] += 1

        for i in range(1,len(countArray)):
            countArray[i] += countArray[i-1]

        for i in range(len(self.partes)-1, -1, -1):
            outputArray[countArray[self.partes[i].getGrandezaTotal() - 1] - 1] = self.partes[i]
        
        self.partes = outputArray 


    def __str__(self):
        description = ''
        for parte in self.partes:
            description += str(parte) + '\n'
        return description

