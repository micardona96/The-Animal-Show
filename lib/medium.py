from models.Animal import Animal
from models.Escena import Escena
from models.Espectaculo import Espectaculo
from models.Parte import Parte
from timeit import timeit

# PARAMETROS
N = 9  # N ANIMALES
M = 4  # M PARTES
K = 3  # K ESCENAS

# INSTANCIAS ANIMALES
capibara = Animal('Capibara', 1)
loro = Animal('Loro', 2)
caiman = Animal('Caimán', 3)
boa = Animal('Boa', 4)
cocodrilo = Animal('Cocodrilo', 5)
cebra = Animal('Cebra', 6)
pantera = Animal('Pantera negra', 7)
tigre = Animal('Tigre', 8)
leon = Animal('León', 9)

ANIMALES = [capibara, loro, caiman, boa, cocodrilo,
            cebra, pantera, tigre, leon]  # LISTA DE ANIMALES

# INSTANCIAS ESCENAS
escena1 = Escena([caiman, capibara, loro])
escena2 = Escena([tigre, loro, capibara])
escena3 = Escena([tigre, cebra, pantera])
escena4 = Escena([pantera, cocodrilo, loro])
escena5 = Escena([leon, pantera, cebra])
escena6 = Escena([cocodrilo, capibara, loro])
escena7 = Escena([boa, caiman, capibara])
escena8 = Escena([leon, caiman, loro])
escena9 = Escena([leon, cocodrilo, boa])

ESCENAS = [escena1, escena2, escena3, escena4, escena5,
           escena6, escena7, escena8, escena9]  # LISTA DE ESCENAS

# INSTANCIAS PARTES
parteApertura = Parte([escena1, escena7, escena6, escena4, escena2,
                       escena8, escena9, escena5, escena3])  # NO EDITAR EL NOMBRE
parte1 = Parte([escena1, escena2, escena3])
parte2 = Parte([escena4, escena5, escena6])
parte3 = Parte([escena7, escena8, escena9])

PARTES = [parte1, parte2, parte3]  # LISTA DE PARTES



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
