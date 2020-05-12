class Animal:
    def __init__(self, nombre, grandeza):
        self.nombre = nombre
        self.grandeza = grandeza
        self.cantidad = 0
    
    def __str__(self):
        return self.nombre
