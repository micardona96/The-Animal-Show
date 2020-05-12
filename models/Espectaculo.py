class Espectaculo:
    def __init__(self, partes, animales, escenas, apertura=[],  resto=[]):
        self.apertura = apertura
        self.resto = resto

   # cantidad de elementos del espectaculo
        self.partes = partes        # m partes
        self.animales = animales    # n animales
        self.escenas = escenas      # k escenas
