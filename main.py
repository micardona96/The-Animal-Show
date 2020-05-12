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
escena4 = Escena([animal6, animal3, animal1])
escena5 = Escena([animal4, animal2, animal5])

parte1 = Parte([escena1, escena2, escena3])
parte2 = Parte([escena4, escena2, escena5])

print('Animales Ordenados por cada escena')
escena1.sortN()
print(escena1)
escena2.sortN()
print(escena2)
escena3.sortN()
print(escena3)
escena4.sortN()
print(escena4)
escena5.sortN()
print(escena5)

print('\n')

print('Escenas ordenadas por cada parte\n')
parte1.sortN()

parte2.sortN()

print(parte1)
print(parte1.getGrandezaTotal())

print(parte2)
print(parte2.getGrandezaTotal())

print('Partes Ordenadas por espectaculo\n')
espectaculo = Espectaculo(partes=[parte2, parte1])
espectaculo.sortN()

print(espectaculo)