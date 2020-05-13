from models.Animal import Animal
from models.Escena import Escena
from models.Espectaculo import Espectaculo
from models.Parte import Parte
from timeit import timeit

cienpies = Animal('Cienpies', 1)
libelula = Animal('Libelula', 2)
gato = Animal('Gato', 3)
perro = Animal('Perro', 4)
tapir = Animal('Tapir', 5)
nutria = Animal('nutria', 6)


Escena.n = 6
Parte.n = 6


escena1 = Escena([tapir, nutria, perro])
escena2 = Escena([tapir, perro, gato])
escena3 = Escena([cienpies, tapir, gato])
escena4 = Escena([gato, cienpies, libelula])


parteApertura = Parte([escena1, escena2, escena3, escena4])
Escena.escenas = parteApertura.escenas

parte1 = Parte([escena1, escena3])
parte2 = Parte([escena4, escena2])


print('\n')

espectaculo = Espectaculo(
                        n=6,
                        k=2,
                        m=3,
                        animales=[cienpies, libelula, gato, perro, tapir, nutria],
                        partes=[parte1, parte2], 
                        apertura=parteApertura, 
                        escenas=[escena1, escena2, escena3, escena4])

#espectaculo.main()

print('N')
resultado1=timeit("espectaculo.main(algoritmo='N')",
                 globals = globals(), number = 200)
print(resultado1 * 1000)
print('NLogN')
resultado2=timeit("espectaculo.main(algoritmo='NLogN')",
                 globals = globals(), number = 200)
print(resultado2 * 1000)
print('NxN')
resultado3=timeit("espectaculo.main(algoritmo='NxN')",
                 globals = globals(), number = 200)

print(resultado3 * 1000)