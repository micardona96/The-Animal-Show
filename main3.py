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
a = Animal('a', 10)
b = Animal('b', 11)
c = Animal('c', 12)
d = Animal('d', 13)
e = Animal('e', 14)
f = Animal('f', 15)
g = Animal('g', 16)
h = Animal('h', 17)
i = Animal('i', 18)
j = Animal('j', 19)
k = Animal('k', 20)

Escena.n = 20
Parte.n = 20


escena1 = Escena([caiman, capibara, loro])
escena2 = Escena([tigre, loro, capibara])
escena3 = Escena([tigre, cebra, pantera])
escena4 = Escena([pantera, cocodrilo, loro])
escena5 = Escena([leon, pantera, cebra])
escena6 = Escena([cocodrilo, capibara, loro])
escena7 = Escena([boa, caiman, capibara])
escena8 = Escena([leon, caiman, loro])
escena9 = Escena([leon, cocodrilo, boa])
escena10 = Escena([a, b, c])
escena11 = Escena([d, f, g])
escena12 = Escena([h, i, j])
escena13 = Escena([caiman, k, capibara])
escena14 = Escena([caiman, a, capibara])
escena15 = Escena([caiman, h, capibara])
escena16 = Escena([caiman, b, capibara])
escena17 = Escena([caiman, c, capibara])
escena18 = Escena([caiman, d, capibara])
escena19 = Escena([caiman, e, capibara])

parteApertura = Parte([escena1, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena9, 
                        escena10, escena11, escena3, escena4, escena5, escena6, escena7, escena8, escena9, 
                        escena11, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena9, 
                        escena1, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19, 
                        escena13, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19, 
                        escena14, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19, 
                        escena15, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19, 
                        escena16, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19, 
                        escena17, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19, 
                        escena18, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19])

Escena.escenas = parteApertura.escenas

parte1= Parte([escena1, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena9])
parte2= Parte([escena10, escena11, escena3, escena4, escena5, escena6, escena7, escena8, escena9])
parte3= Parte([escena11, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena9])
parte4= Parte([escena1, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19])
parte5= Parte([escena13, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19])
parte6= Parte([escena14, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19])
parte7= Parte([escena15, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19])
parte8= Parte([escena16, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19])
parte9= Parte([escena17, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19])
parte10= Parte([escena18, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena19])

print('\n')

espectaculo= Espectaculo(
                        n = 20,
                        m=10,
                        k=19,
                        animales = [capibara, loro, caiman, boa,
                            cocodrilo, cebra, pantera, tigre, leon,a,b,c,d,e,f,g,h,i,j,k],
                        partes = [parte1, parte2, parte3,parte4,parte5,parte6,parte7,parte8,parte9,parte10],
                        apertura = parteApertura,
                        escenas = [escena1, escena2, escena3, escena4, escena5, escena6, escena7, escena8, escena9, 
                                    escena10, escena11, escena12, escena13, 
                                    escena14, escena15, escena16, escena17, escena18, escena19])


#espectaculo.main(algoritmo = 'NLogN')
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
