from models.Animal import Animal
from models.Escena import Escena
from models.Espectaculo import Espectaculo
from models.Parte import Parte

animal1 = Animal('Perro', 1)
animal2 = Animal('Gato', 2)
animal3 = Animal('Loro', 3)
animal4 = Animal('Cocodrilo', 4)
animal5 = Animal('Elefante', 5)
animal6 = Animal('Caballo', 6)

escena1 = Escena([animal1, animal2, animal4])
escena2 = Escena([animal3, animal1, animal2])
escena3 = Escena([animal5, animal1, animal6])

parte1 = Parte([escena1, escena2, escena3])

print('Animales Ordenados por cada escena')
escena1.sortN()
print(escena1)
escena2.sortN()
print(escena2)
escena3.sortN()
print(escena3)

print('\n')

print('Escenas ordenadas por cada parte')
parte1.sortN()

print(parte1)