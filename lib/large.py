from models.Animal import Animal
from models.Escena import Escena
from models.Espectaculo import Espectaculo
from models.Parte import Parte
from timeit import timeit

# PARAMETROS
N = 20  # N ANIMALES
M = 6  # M PARTES
K = 10  # K ESCENAS

# INSTANCIAS ANIMALES
capibara  = Animal('Capibara',1)
loro      = Animal('Loro',2)
caiman    = Animal('Caimán',3)
boa       = Animal('Boa',4)
cocodrilo = Animal('Cocodrilo',5)
cebra     = Animal('Cebra',6)
pantera   = Animal('Pantera negra',7)
tigre     = Animal('Tigre',8)
leon      = Animal('León',9)
vaca      = Animal('vaca',10)
abeja     = Animal('abeja',11)
aguila    = Animal('águila',12)
arana     = Animal('araña',13)
avispa    = Animal('avispa',14)
ballena   = Animal('ballena',15)
bisonte   = Animal('bisonte',16)
bufalo    = Animal('búfalo',17)
camello   = Animal('camello',18)
canario   = Animal('canario',19)
cangrejo  = Animal('cangrejo',20)


ANIMALES = [capibara, loro, caiman, boa, cocodrilo, cebra, pantera, tigre, leon, vaca,
            abeja, aguila, arana, avispa, ballena, bisonte, bufalo, camello, canario, cangrejo]


# INSTANCIAS ESCENAS
escena1  = Escena([capibara, abeja, cebra])
escena2  = Escena([capibara, abeja, pantera])
escena3  = Escena([capibara, abeja, tigre])
escena4  = Escena([capibara, abeja, leon])
escena5  = Escena([capibara, abeja, vaca])
escena6  = Escena([capibara, aguila, cebra])
escena7  = Escena([capibara, aguila, pantera])
escena8  = Escena([capibara, aguila, tigre])
escena9  = Escena([capibara, aguila, leon])
escena10 = Escena([capibara, aguila, vaca])

escena11 = Escena([loro, arana, cebra])
escena12 = Escena([loro, arana, pantera])
escena13 = Escena([loro, arana, tigre])
escena14 = Escena([loro, arana, leon])
escena15 = Escena([loro, arana, vaca])
escena16 = Escena([loro, avispa, cebra])
escena17 = Escena([loro, avispa, pantera])
escena18 = Escena([loro, avispa, tigre])
escena19 = Escena([loro, avispa, leon])
escena20 = Escena([loro, avispa, vaca])

escena21 = Escena([caiman, ballena, cebra])
escena22 = Escena([caiman, ballena, pantera])
escena23 = Escena([caiman, ballena, tigre])
escena24 = Escena([caiman, ballena, leon])
escena25 = Escena([caiman, ballena, vaca])
escena26 = Escena([caiman, bisonte, cebra])
escena27 = Escena([caiman, bisonte, pantera])
escena28 = Escena([caiman, bisonte, tigre])
escena29 = Escena([caiman, bisonte, leon])
escena30 = Escena([caiman, bisonte, vaca])

escena31 = Escena([boa, bufalo, cebra])
escena32 = Escena([boa, bufalo, pantera])
escena33 = Escena([boa, bufalo, tigre])
escena34 = Escena([boa, bufalo, leon])
escena35 = Escena([boa, bufalo, vaca])
escena36 = Escena([boa, camello, cebra])
escena37 = Escena([boa, camello, pantera])
escena38 = Escena([boa, camello, tigre])
escena39 = Escena([boa, camello, leon])
escena40 = Escena([boa, camello, vaca])

escena41 = Escena([cocodrilo, canario, cebra])
escena42 = Escena([cocodrilo, canario, pantera])
escena43 = Escena([cocodrilo, canario, tigre])
escena44 = Escena([cocodrilo, canario, leon])
escena45 = Escena([cocodrilo, canario, vaca])
escena46 = Escena([cocodrilo, cangrejo, cebra])
escena47 = Escena([cocodrilo, cangrejo, pantera])
escena48 = Escena([cocodrilo, cangrejo, tigre])
escena49 = Escena([cocodrilo, cangrejo, leon])
escena50 = Escena([cocodrilo, cangrejo, vaca])


ESCENAS = [escena50, escena1,  escena2,  escena3,  escena4,  escena5,  escena6,  escena7,  escena8,  escena9,
           escena10, escena11, escena12, escena13, escena14, escena15, escena16, escena17, escena18, escena19,
           escena20, escena21, escena22, escena23, escena24, escena25, escena26, escena27, escena28, escena29,
           escena30, escena31, escena32, escena33, escena34, escena35, escena36, escena37, escena38, escena39,
           escena40, escena41, escena42, escena43, escena44, escena45, escena46, escena47, escena48, escena49]

parteApertura = Parte([escena50, escena1,  escena2,  escena3,  escena4,  escena5,  escena6,  escena7,  escena8,  escena9,
                       escena10, escena11, escena12, escena13, escena14, escena15, escena16, escena17, escena18, escena19,
                       escena20, escena21, escena22, escena23, escena24, escena25, escena26, escena27, escena28, escena29,
                       escena30, escena31, escena32, escena33, escena34, escena35, escena36, escena37, escena38, escena39,
                       escena40, escena41, escena42, escena43, escena44, escena45, escena46, escena47, escena48, escena49])

parte1 = Parte([escena29, escena8, escena46, escena45, escena4,
                escena3, escena42, escena1, escena10, escena7])

parte2 = Parte([escena49, escena18, escena36, escena35, escena14,
                escena13, escena32, escena11, escena20, escena17])

parte3 = Parte([escena39, escena28, escena26, escena25, escena24,
                escena23, escena22, escena31, escena30, escena27])

parte4 = Parte([escena19, escena38, escena16, escena15, escena34,
                escena33, escena12, escena41, escena40, escena37])

parte5 = Parte([escena9, escena48, escena6, escena5, escena44,
                escena43, escena2, escena21, escena50, escena47])


PARTES = [parte1, parte2, parte3, parte4, parte5]  # LISTA DE PARTES


####################################
#          DON'T TOUCH ME          #
####################################

Escena.n = N
Parte.n = N
Escena.escenas = parteApertura.escenas
espectaculo = Espectaculo(
    n=N,
    m=M,
    k=K,
    animales=ANIMALES,
    partes=PARTES,
    escenas=ESCENAS,
    apertura=parteApertura)


print('\033[94m' + '\n--- RESULTADOS ---' + '\033[0m')
espectaculo.main(algoritmo='N')
espectaculo.imprimirResultados()


print('\033[94m' + '\n--- ANÁLISIS DE COMPLEJIDAD ---' + '\033[0m')
resultado1 = timeit("espectaculo.main(algoritmo='N')",
                    globals=globals(), number=200)
print('Solución O(N)  \t \t' + str(resultado1 * 1000))

resultado2 = timeit("espectaculo.main(algoritmo='NLogN')",
                    globals=globals(), number=200)
print('Solución O(N log N)  \t' + str(resultado2 * 1000))

resultado3 = timeit("espectaculo.main(algoritmo='NxN')",
                    globals=globals(), number=200)
print('Solución O(N²) \t \t' + str(resultado3 * 1000) + '\n')
