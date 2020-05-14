from models.Animal import Animal
from models.Escena import Escena
from models.Espectaculo import Espectaculo
from models.Parte import Parte
from timeit import timeit

capibara = Animal('Capibara', 1)
loro = Animal('Loro', 2)
caiman = Animal('Caimán', 3)
boa = Animal('Boa', 4)
cocodrilo = Animal('Cocodrilo', 5)
cebra = Animal('Cebra', 6)
pantera = Animal('Pantera negra', 7)
tigre = Animal('Tigre', 8)
leon = Animal('León', 9)

Escena.n = 9
Parte.n = 9


escena1 = Escena([caiman, capibara, loro])
escena2 = Escena([tigre, loro, capibara])
escena3 = Escena([tigre, cebra, pantera])
escena4 = Escena([pantera, cocodrilo, loro])
escena5 = Escena([leon, pantera, cebra])
escena6 = Escena([cocodrilo, capibara, loro])
escena7 = Escena([boa, caiman, capibara])
escena8 = Escena([leon, caiman, loro])
escena9 = Escena([leon, cocodrilo, boa])

parteApertura = Parte([escena1,escena7,escena6,escena4,escena2,escena8,escena9,escena5,escena3])
Escena.escenas = parteApertura.escenas

parte1 = Parte([escena1, escena2, escena3])
parte2 = Parte([escena4, escena5, escena6])
parte3 = Parte([escena7, escena8, escena9])


print('\n')

espectaculo = Espectaculo(
                        animales=[capibara, loro, caiman, boa, cocodrilo, cebra, pantera, tigre, leon],
                        partes=[parte1, parte2, parte3], 
                        apertura=parteApertura, 
                        escenas=[escena1, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena9])


espectaculo.main(algoritmo='NLogN')
espectaculo.imprimirResultados()

print('\n')

print('NxN')
resultado3=timeit("espectaculo.main(algoritmo='NxN')",
                 globals = globals(), number = 200)
print(resultado3 * 1000)

print('NLogN')
resultado2=timeit("espectaculo.main(algoritmo='NLogN')",
                 globals = globals(), number = 200)
print(resultado2 * 1000)

print('N')
resultado1=timeit("espectaculo.main(algoritmo='N')",
                 globals = globals(), number = 200)
print(resultado1 * 1000)


