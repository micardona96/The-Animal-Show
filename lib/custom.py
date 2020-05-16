from models.Animal import Animal
from models.Escena import Escena
from models.Espectaculo import Espectaculo
from models.Parte import Parte
from timeit import timeit



####################################
#          ADD CUSTOM ARGS         #
####################################

N = 4  #                                                      <===  N ANIMALES
M = 3  #                                                      <===  M PARTES
K = 2  #                                                      <===  K ESCENAS

capibara = Animal('Capibara', 1)
loro = Animal('Loro', 2)
caiman = Animal('Caimán', 3)
perro = Animal('perro', 4) 
## nameN = Animal('name', N)                                  <=== AGREGAR OBJETOS ANIMALES 
ANIMALES = [capibara, loro, caiman, perro] ##                 <=== AGREGAR NUEVOS ANIMALES EN LA LISTA

escena1 = Escena([caiman, capibara, loro])
escena2 = Escena([perro, capibara, loro])
escena3 = Escena([perro, caiman, loro])
escena4 = Escena([perro, caiman, capibara]) 
## escena((M-1)* K) = Escena([..., ..., ...])                 <=== AGREGAR OBJETOS ESCENAS 
ESCENAS = [escena1, escena2, escena3, escena4] ##             <=== AGREGAR NUEVAS ESCENAS EN LA LISTA


parte1 = Parte([escena1, escena3])
parte2 = Parte([escena2, escena4]) 
parteApertura = Parte([escena1, escena2, escena3, escena4]) ## <=== AGREGAR NUEVAS ESCENAS EN LA LISTA
## parteM = Parte([..., ...])                                  <=== AGREGAR OBJETOS PARTES 
PARTES = [parte1, parte2] ##                                   <=== AGREGAR NUEVAS PARTES EN LA LISTA












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
