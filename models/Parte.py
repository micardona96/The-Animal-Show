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