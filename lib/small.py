from models.Animal import Animal
from models.Escena import Escena
from models.Espectaculo import Espectaculo
from models.Parte import Parte
from timeit import timeit

# PARAMETROS
N = 6  # N ANIMALES
M = 3  # M PARTES
K = 2  # K ESCENAS

# INSTANCIAS ANIMALES
cienpies = Animal('Cienpies', 1)
libelula = Animal('Libelula', 2)
gato = Animal('Gato', 3)
perro = Animal('Perro', 4)
tapir = Animal('Tapir', 5)
nutria = Animal('nutria', 6)

ANIMALES = [cienpies, libelula, gato, perro,
            tapir, nutria]  # LISTA DE ANIMALES

# INSTANCIAS ESCENAS
escena1 = Escena([tapir, nutria, perro])
escena2 = Escena([tapir, perro, gato])
escena3 = Escena([cienpies, tapir, gato])
escena4 = Escena([gato, cienpies, libelula])

ESCENAS = [escena1, escena2, escena3, escena4]  # LISTA DE ESCENAS

# INSTANCIAS PARTES
# NO EDITAR EL NOMBRE
parteApertura = Parte([escena1, escena2, escena3, escena4])
parte1 = Parte([escena1, escena3])
parte2 = Parte([escena4, escena2])

PARTES = [parte1, parte2]  # LISTA DE PARTES



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


print('\033[94m' + '\n--- ANÁLISIS DE COMPLEJIDAD (seconds) ---' + '\033[0m')


resultado1 = timeit("espectaculo.main(algoritmo='N')",
                    globals=globals(), number=1000)
print('Solución O(N)  \t \t' + str(resultado1))

resultado2 = timeit("espectaculo.main(algoritmo='NLogN')",
                    globals=globals(), number=1000)
print('Solución O(N log N)  \t' + str(resultado2))

resultado3 = timeit("espectaculo.main(algoritmo='NxN')",
                    globals=globals(), number=1000)
print('Solución O(N²) \t \t' + str(resultado3) + '\n')
