class Parte:
    def __init__(self, escenas=[]):
        self.escenas = escenas
    
    def getGrandezaTotal(self):
        pass

    def sortN(self):
        outputArray = [None]*3
        countArray = [0]*15

        for escena in self.escenas:
            countArray[escena.getGrandezaTotal() - 1] += 1

        for i in range(1,len(countArray)):
            countArray[i] += countArray[i-1]

        for i in range(len(self.escenas)-1, -1, -1):
            outputArray[countArray[self.escenas[i].getGrandezaTotal() - 1] - 1] = str(self.escenas[i])

        print(outputArray)    
    