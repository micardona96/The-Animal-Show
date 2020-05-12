class Animal:
    def __init__(self, nombre, grandeza):
        self.nombre = nombre
        self.grandeza = grandeza
    
    def __str__(self):
        return self.nombre
