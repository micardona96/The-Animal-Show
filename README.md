#  🐧 The Animal Show

![languages](https://img.shields.io/github/languages/top/micardona96/FADA)
![Size](https://img.shields.io/github/repo-size/micardona96/FADA)
![commits](https://img.shields.io/github/commit-activity/m/micardona96/FADA)
![last-commit](https://img.shields.io/github/last-commit/micardona96/FADA)
![LICENSE](https://img.shields.io/github/license/micardona96/FADA)

Este proyecto se basa en la construcción de un software de ordenamiento que permita gestionar el itinerario y orden de prestación para el The animal show. La construcción del software está fundamentada en el análisis de complejidad de las escenas y partes del show, haciendo que en cada escena esta ordenada, tal que la aparición de los animales sea según su grandeza, además las partes del show también estarán ordenadas de forma ascendente, permitiendo que cada escena será mas grande que la anterior. Tomando en cuenta esto, disponemos de un espectáculo maravilloso.

**Índice**   
- [Lineamientos The Animal Show](#id1)
  - [Descripción](#id2)
  - [Características adicionales](#id3)
  - [Requerimientos de optimización](#id4)
  
- [Reporte The Animal Show](#id5)
  - [Análisis general de la implementación ](#id6)
   - [Clases](#id7)
      - [Animal](#id99)
      - [Escena](#id98)
      - [Parte](#id97)
      - [Espectáculo](#id96)
  - [Archivos y datos de pruebas](#id200)
    - [Instrucciones de uso](#id11)
    
- [Implementaciones ](#id12)
  - [Solución O (n²)](#id8)
    - [Análisis y solución](#id9)
    - [Implementación](#id10)
    
  - [Solución O (n log n) ](#id14)
    - [Análisis y solución](#id15)
    - [Implementación](#id16)

  - [Solución O (n)](#id20)
    - [Análisis y solución](#id21)
    - [Implementación](#id22)
    
  - [Solución Estadísticas solicitadas por el gerente del Zoologico](#id30)
    - [Animal que participó en más escenas dentro del espectáculo](#id31)
    - [Animal que participó en menos escenas dentro del espectáculo](#id32)
    - [Escena de menor grandeza](#id33)
    - [La escena de mayor grandeza total](#id34)
    - [Promedio de grandeza del espéctaculo](#id35)
    
 - [Análisis general de resultados ](#id26)
 - [Conclusiones del proyecto](#id27)
 - [Correr script online](#id100) 


---


## 📏 Lineamientos The Animal Show <a name="id1"></a>
### Descripción <a name="id2"></a>
- The animal show contará con n animales como participantes del espectáculo. Además, el evento consistir a en m partes.
- Una primera parte: Una gran apertura del evento, que consiste en (m−1) ∗k escenas, donde en cada escena participan 3 animales distintos.

- Seguido de la apertura: se presentarán m − 1 partes de k escenas cada una, donde, al igual que en la apertura, en cada escena participan 3 animales distintos. 

- Una escena es un conjunto de 3 elementos (animales).

Es decir, el evento tiene m partes, de las cuales 1 parte es la Gran apertura y que se presenta primero, y luego de ella se presentan las siguientes m − 1 partes, para completar el Gran espectáculo.


### Características adicionales <a name="id3"></a>
Adicionalmente, el gerente del The animal show desea saber ciertos datos acerca de su espectáculo: 
- El animal que participo en más escenas dentro del espectáculo y en cuantas participo. (En caso de haber empate entre animales, se deben mostrar todos) 
- El animal que menos participo en escenas dentro del espectáculo y en cuantas participo. (En caso de haber empate entre animales, se deben mostrar todos) 
- La escena de menor grandeza total. 
- La escena de mayor grandeza total. 
- El promedio de grandeza de todo el espectáculo (se tienen en cuenta todas las escenas, incluidas las de la apertura y las de los m−1 bloques siguientes).

### Requerimientos de optimización  <a name="id4"></a>

1. [Plantear una solución al problema cuya complejidad sea O (n²)](#id8)
2. [Plantear una solución al problema cuya complejidad sea O (n log(n)) ](#id14)
3. [Plantear una solución al problema cuya complejidad sea O (n)](#id20)

---

## 🚀 Reporte The Animal Show <a name="id5"></a>
### Análisis general de la implementación <a name="id6"></a>
The animal show app hace uso lenguaje de programación Python que permite un paradigma orientados a objetos, además es un lenguaje interpretado, dinámico y su filosofía hace hincapié en la legibilidad de su código.

La forma en que atacamos el problema se basa en dos puntos principales, el primero es la implementación orientada a objetos 
con python, y la segundad fue el ordenamiento secuencial que se realizó tanto a las escenas, las partes y el espectáculo en general.

Con ordenamiento secuencial nos referimos a ir ordenando desde las partes mas internas en el arbol de objetos (Animal, Escena) hasta las
partes mas externas (Parte, Espectáculo).

En primera instancia procedimos a ordenar todas las escenas que hacían parte del espectáculo, en este caso, una escena es representada mediante un objeto, la cual incluye todos los métodos de ordenamiento con su diferente complejidad, seguido, ordenamos las partes del espectáculo (objeto), el cúal ya recibe las escenas ordenadas, y para finalizar, ordenamos el Espectáculo recibiendo las partes con todos
sus objetos internos (escenas) ordenados.

La característica que comparten cada objeto (excluyendo el objeto Animal) es que todos tienen dentro la implementación de su clase
los mismos algortimos de ordenamiento con sus distintas complejidades, para así, poder realizar el ordenamiento secuencial explicado
anteriormente.

Para el calculo del tiempo de ejecución de los distintos algoritmos, se hará uso del método timeit, perteneciente al módulo timeit
de la libreria estandar de python, ***El método timeit() ejecuta la instrucción de configuración una vez, luego ejecuta la instrucción primaria repetidamente y devuelve la cantidad de tiempo que pasa. El argumento de timeit() controla cuántas veces ejecutar la declaración; el valor predeterminado es 1,000,000.***

[Más información sobre timeit](https://rico-schmidt.name/pymotw-3/timeit/#contenido-del-modulo)

---


### Clases <a name="id7"></a>


#### _Animal_ <a name="id99"></a>
[Ir al contexto de la implementación](./lib/models/Animal.py)


Clase encargada de crear objetos tipo Animal, estos objetos cuentan con 3 propiedades las cules son:

- Propiedades 
  - **String** *Nombre:* Nombre del animal.
  - **Int** *Grandeza:* Grandeza del animal en el espectaculo.
  - **Int** *Cantidad:* Cantidad de apariciones del animal en las escenas.

#### _Escena_ <a name="id98"></a>
[Ir al contexto de la implementación](./lib/models/Escena.py)


Clase encargada de crear objetos tipo Escena, la cual se encarga de agrupar objetos tipo animal, cuenta con dos propiedades y 5 metodos que ayudan a la estructuracion de sus contenedores en el objeto parte.

- Propiedades 
  - **Array(Animal)** *Animales:* Lista de animales que conforma la escena.
  - **Int** *TotalGrandeza:* Sumatoria total de las grandezas individuales de cada animal.

- Metodos
  - **aumentarCantidad():** Aumenta en 1 la cantidad de apariciones de los animales que participan en la escena, Complejidad O(1)
  - **getGrandezaTotal():** Calculo de la grandeza total de la escena (Complejidad O(N)).
  - **sortNxN():** Algoritmo de ordenamiento Bubble Sort (Complejidad O(N²)), se usa para ordenar los animales dentro de las escenas.
  - **sortN():** Algoritmo de ordenamiento Counting Sort (Complejidad O(N)), se usa para ordenar los animales dentro de las escenas.
  - **sortNLogN():** Algoritmo de ordenamiento Quick Sort (Complejidad O(N log (N))), se usa para ordenar los animales dentro de las escenas.

#### _Parte_ <a name="id97"></a>
[Ir al contexto de la implementación](./lib/models/Parte.py)

Clase encargada de crear objetos tipo Parte,la cual se encarga de agrupar objetos tipo Escena, cuenta con una propiedad y 2 metodos que ayudan a la estructuracion de sus contenedores en el objeto espectaculo.

- Propiedades 
  - **Array(Escena)** *Escenas:* Lista de escenas que conforma la parte de un espectaculo.
  
- Metodos
  - **getGrandezaTotal():** Calculo de la grandeza total de la parte (Complejidad O(N)).
  - **sortN():** Algoritmo de ordenamiento Counting Sort (Complejidad O(N)), se usa para ordenar las escenas dentro de las partes.
  
#### _Espectáculo_  <a name="id96"></a>
[Ir al contexto de la implementación](./lib/models/Espectaculo.py)

Clase encargada de crear objetos tipo Espectáculo,la cual se encarga de agrupar objetos tipo Parte, cuenta con una 7 propiedades y 7 metodos que despliean los resultados esperados por parte del administrador.

- Propiedades 
  - **Int** *apertura:* Lista de escenas que dan apertura al evento
  - **Array(partes)** *partes:* Lista de partes que dan continuidad al evento, despues de la apertura.
  - **Array(escenas)** *escenas:* Lista de escenas que conforman el evento.
  - **Array(animales)** *animales:* Lista de animales que participan en el espectaculo.
  - **Int** *m:* Cantidad de partes en el espectáculo.
  - **Int** *n:* Cantidad de animales en el espectáculo.
  - **Int** *k:* Cantidad de escenas por parte en el espectáculo.
  
- Metodos
  - **promedioGradezaEspectaculo():**  Algoritmo para calcular el promedio del espectaculo (escenas) con complejidad O(k) (número de escenas).
  - **maxGradezaEscena():**  Algoritmo para calcular la escena con mayor grandeza con complejidad O(k) (número de escenas).
  - **minGradezaEscena():**  Algoritmo para calcular la escena con menor grandeza con complejidad O(k) (número de escenas).
  - **maxParticipacionAnimal():**  Algoritmo para calcular los animales con mayor participación en escenas. Complejidad O(n) (número de animales).
  - **minParticipacionAnimal():** Algoritmo para calcular los animales con menor participación en escenas. Complejidad O(n) (número de animales).
  - **sortN():**  Algoritmo para ordenar las partes del espectaculo con Complejidad O(n) utilizando el algoritmo CountingSort.
  - **main():**  Funcion que hace la invocaicon de cada uno de los eventos de forma secuencial.

---

### Archivos y datos de pruebas <a name="id200"></a>

El proyecto se organiza de forma jerárquico, con los siguientes directorios, `./lib` `./test` estos direcctorios contienen los archivos necesarios para la ejecucion del sistema.

El directorio `./lib` contiene algunas instancias predefinidas para la ejecuacion rapida de 3 casos particulares de The Animal Show, estas instancias se carcterizan por su tamaño, ademas contiene el archivo custom que permite agregar instancias personalizadas editando, dicho archivo,

El directorio `./lib/models` contiene la implemtancion de las clases y algoritmos para la ejecuion del sistema.

Antes de realizar la implementacion particular de los algoritmos de ordenamiento, realizamos algunas prueba en frio, para comprobar sus funcionalidades; la implementacion de estos estara en el directorio `./test`, ademas esta parametrizado para realizar pruebas personalizadas,  `run-test [size]` sera tamaño de una lista genereado de forma aleatoria. 

con la ejecucion del siguiente comando en la raiz del proyecto, se ejecutaran n cantidad de test, de los cuales nos arrojara una tabla de los resultados con los algoritmos ***N*** vs ***NlogN*** vs ***N²***

``` sh
> python main.py run-test 10

--- RESULTADOS DEL TEST (seconds) ---
Array size in test 10:

Size    N       NlogN   N²
1       0.0069  0.0041  0.0022
2       0.0073  0.0078  0.0039
3       0.0105  0.0111  0.0057
4       0.0099  0.0163  0.0077
5       0.0125  0.0178  0.011
6       0.0122  0.0242  0.0149
7       0.0156  0.0252  0.0147
8       0.0168  0.0311  0.0187
9       0.0179  0.0343  0.0217
10      0.0196  0.0364  0.0259

```

La ejecucion de estos algoritmos en frio, permitira comprender de forma general el funcionamiento y la complejidad de The Animal Show,
estos datos seran utilizados para [Análisis general de resultados ](#id26)

### Instrucciones de uso<a name="id11"></a>
Todas las ejecuciones de los ardemientos para The Animal Show, ejecutaran las distintas complejidades para comparalas por cada ejecuccion. para la ejecucion de las instancias predefinidas small, medium, large, custom; Ejecutar el siguiente comando en la raiz del proyecto:


```sh
> python main.py small     
```

```sh
> python main.py medium     
```

```sh
> python main.py large     
```

Para la ejecucion de la instancia ***custom***, primero modificar el archivo custo, que se encuenta en el directorio `./lib/custom`
agregando las instancias de los animales, las escenas y las partes del espectaculo, con base a la siguiente guia de 4 animales, 3 partes y 2 escenas

***Custom File***
```  python
...

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
parteApertura = Parte([escena1, escena2, escena3, escena4]) #  <=== AGREGAR NUEVAS ESCENAS EN LA LISTA
## parteM = Parte([..., ...])                                  <=== AGREGAR OBJETOS PARTES 
PARTES = [parte1, parte2] ##                                   <=== AGREGAR NUEVAS PARTES EN LA LISTA
```

```sh
> python main.py custom     
```

Tambien puede ejecutar el comando ***help*** para obtener informacion sobre el uso de la linea de comandos CLI.

```sh
> python main.py help     
```

---
## Implementaciones <a name="id12"></a>
### Solución O (n²)  <a name="id8"></a>
#### Análisis y solución <a name="id9"></a>
Para obtener una solución O (n²) al problema planteado, se realizó un análisis de los respectivos algortimos ya existentes
que tuvieran esta complejidad y elegimos usar el BubbleSort.

Como se mencionó en el análisis general, cada clase tiene implementado los mismos algoritmos de ordenamiento con sus distintas
complejidades, en este caso, los objetos (Escena, Parte, Espéctaculo) tienen una función llamada sortNxN que implementa BubbleSort.

#### Implementación <a name="id10"></a>
Esta sera una implementacion generica del algoritmo burbuja, solo es usado para referenciar su implementacion en el proyecto, en cada una de las instancias Animal, Escena, Parte y Espectaculo, toman como guia esta misma implementacion, con variaciones en los llamados a sus propiedades.

***Algoritmo genérico BubbleSort***

[Ir al contexto de la implementación](./test/algoritmos.py#L23)

```python
def sortNxN(numeros):
    """ Algoritmo de ordenamiento burbuja (Complejidad O(N^2)) """
    for i in range(len(numeros)):
        for j in range(len(numeros) - i - 1):
            if numeros[j] > numeros[j+1]:
                numAux = numeros[j+1]
                numeros[j+1] = numeros[j]
                numeros[j] = numAux
    return numeros
```


Esta función sortNxN es llamada secuencialmente por todos los objetos de las distintas clases que lo implementan en el siguiente orden.

- Primero se ejecuta la función para todas las escenas que hacen parte del espectáculo para ordenarlas (Animales por su grandeza)
- Una vez ordenadas las escenas, las partes obtienen sus respectivas escenas y con base a la grandeza total de todas las escenas
ejecuta el llamada a sortNxN, ordenando así las partes internamente.
- Ya por último el objeto instancia de la clase Espéctaculo recibe todas las partes ordenadas por sus respectivas escenas, y hace uso de la
grandeza total por partes para ejecutar el algoritmo sortNxN (QuickSort) para ordenar todo el espéctaculo 



---

### Solución O (n log n)  <a name="id14"></a>

#### Análisis y solución <a name="id15"></a>
Para obtener una solución O (n log n) al problema planteado, se realizó un análisis de los respectivos algortimos ya existentes
que tuvieran esta complejidad, entre los que vimos en el curso, resaltaron especialmente dos(2), MergeSort y QuickSort. Elegimos Quicksort
con pivote aleatorio debido a la comprensión que teniamos sobre el algoritmo, simplicidad de implementación y a sus buenos resultados (evidenciados) con grupos pequeños de datos.

Como se mencionó en el análisis general, cada clase tiene implementado los mismos algoritmos de ordenamiento con sus distintas
complejidades, en este caso, los objetos (Escena, Parte, Espéctaculo) tienen una función llamada sortNLogN que implementa QuickSort.

#### Implementación <a name="id16"></a>
Esta sera una implementacion generica del algoritmo QuickSort, solo es usado para referenciar su implementacion en el proyecto, en cada una de las instancias Animal, Escena, Parte y Espectaculo, toman como guia esta misma implementacion, con variaciones en los llamados a sus propiedades.

***Algoritmo genérico QuickSort***

[Ir al contexto de la implementación](./test/algoritmos.py#L34)

``` python
def sortNLogN(numeros):
        if len(numeros) < 1:
            return []

        posicionPivot = randint(0, len(numeros) - 1)
        pivot = numeros[posicionPivot]
        left = []
        right = []
        numeros.pop(posicionPivot)

        for i in range(len(numeros)):
            if numeros[i] < pivot:
                left.append(numeros[i])
            else:
                right.append(numeros[i])

        return sortNLogN(left) + [pivot] + sortNLogN(right)

```


Esta función sortNLogN es llamada secuencialmente por todos los objetos de las distintas clases que lo implementan en el siguiente orden.

- Primero se ejecuta la función para todas las escenas que hacen parte del espectáculo para ordenarlas (Animales por su grandeza)
- Una vez ordenadas las escenas, las partes obtienen sus respectivas escenas y con base a la grandeza total de todas las escenas
ejecuta el llamada a sortNLogN, ordenando así las partes internamente.
- Ya por último el objeto instancia de la clase Espéctaculo recibe todas las partes ordenadas por sus respectivas escenas, y hace uso de la
grandeza total por partes para ejecutar el algoritmo sortNLogN (QuickSort) para ordenar todo el espéctaculo 

---

### Solución O (n) <a name="id20"></a>

#### Análisis y solución <a name="id21"></a>
Para obtener una solución O (n) al problema planteado, se realizó un análisis de los respectivos algortimos ya existentes
que tuvieran esta complejidad, entre los que vimos en el curso, resaltó especialmente el CountingSort. Elegimos este algoritmo
debido a que funciona correctamente con rangos de datos definidos, en nuestro caso, el problema nos da los valores de m (cantidad de partes),
k (cantidad de escenas) y n (cantidad de animales)

Como se mencionó en el análisis general, cada clase tiene implementado los mismos algoritmos de ordenamiento con sus distintas
complejidades, en este caso, los objetos (Escena, Parte, Espéctaculo) tienen una función llamada sortN que implementa CountingSort.

#### Implementación <a name="id22"></a>
Esta sera una implementacion generica del algoritmo Counting Sort, solo es usado para referenciar su implementacion en el proyecto, en cada una de las instancias Animal, Escena, Parte y Espectaculo, toman como guia esta misma implementacion, con variaciones en los llamados a sus propiedades.

***Algoritmo genérico CountingSort***

[Ir al contexto de la implementación](./test/algoritmos.py#L6)

``` python 
def sortN(numeros):
    outputArray = [None]*len(numeros)
    countArray = [0]*100

    for numero in numeros:
        countArray[numero - 1] += 1

    for i in range(1,len(countArray)):
        countArray[i] += countArray[i-1]

    for i in range(len(numeros) -1, -1, -1):
        outputArray[countArray[numeros[i] - 1] - 1] = numeros[i]
        countArray[numeros[i] - 1] -= 1

    return outputArray
```

Esta función sortN es llamada secuencialmente por todos los objetos de las distintas clases que lo implementan en el siguiente orden.

- Primero se ejecuta la función para todas las escenas que hacen parte del espectáculo para ordenarlas (Animales por su grandeza)
- Una vez ordenadas las escenas, las partes obtienen sus respectivas escenas y con base a la grandeza total de todas las escenas
ejecuta el llamada a sortN, ordenando así las partes internamente.
- Ya por último el objeto instancia de la clase Espéctaculo recibe todas las partes ordenadas por sus respectivas escenas, y hace uso de la
grandeza total por partes para ejecutar el algoritmo sortN (CountingSort) para ordenar todo el espéctaculo

---

### Solución Estadísticas solicitadas por el gerente del Zoologico <a name="id30"></a>

#### Animal que participó en más escenas dentro del espectáculo <a name="id31"></a>
Para obtener el animal que más participo en escenas se hizo uso de lo llamado paso por referencia,
los animales que participan en el espectáculo son creados una sola vez, por lo tanto, se comparte la misma
instancia de los animales en todas las escenas.

En cada escena se le suma en uno(1) la propiedad cantidad del objeto Animal, para así, ir contando la cantidad
de apariciones en escenas.

La complejidad de este mecanismo de conteo es O(1), debido a que en cada escena sólo participan tres(3) animales,
esto implica que el ciclo for usado para aumentar en 1 la propiedad cantidad del objeto sólo realice operaciones (iteraciones)
tres veces.

``` python

    def maxParticipacionAnimal(self):
        """ Algoritmo para calcular los animales con mayor participación en escenas,
            con Complejidad O(n) (número de animales)"""
        arrayMaxAnimales = []
        maxAnimal = self.animales[0]
        for i in range(1,len(self.animales)):
            if self.animales[i].cantidad > maxAnimal.cantidad:
                maxAnimal = self.animales[i]
            elif self.animales[i].cantidad == maxAnimal.cantidad:
                arrayMaxAnimales.append(self.animales[i])
        
        print('El/Los animales que más partició/participaron en escenas fueron: ')
        if len(arrayMaxAnimales) == 0:
            print(maxAnimal.nombre + " con " + str(maxAnimal.cantidad * 2) + " escenas")
        else:
            for animal in arrayMaxAnimales:
                print(animal.nombre + " con " + str(animal.cantidad * 2) + " escenas")
            print(maxAnimal.nombre + " con " + str(animal.cantidad * 2) + " escenas")

```
[Ir al contexto de la implementación](./lib/models/Espectaculo.py#L45)

---

#### Animal que participó en menos escenas dentro del espectáculo <a name="id32"></a>
Al igual que el Animal que más participó en escenas, se hace uso de la misma idea, sólo que esta vez, en la clase espéctaculo
existen los métodos minParticipacionAnimal y maxParticipacionAnimal, que ejecuta un ciclo for n(cantidad de animales) veces,
para encontrar el máximo y el mínimo animal. La complejidad de este algoritmo es O(n), ya que realiza n iteraciones, recorriendo
todos los animales que participan en espectaculo en busqueda del que participa en más y menos escenas.

``` python

       def minParticipacionAnimal(self):
        """ Algoritmo para calcular los animales con menor participación en escenas,
            con Complejidad O(n) (número de animales)"""
        arrayMinAnimales = []
        minAnimal = self.animales[0]
        for i in range(1,len(self.animales)):
            if self.animales[i].cantidad < minAnimal.cantidad:
                minAnimal = self.animales[i]
            elif self.animales[i].cantidad == minAnimal.cantidad:
                arrayMinAnimales.append(self.animales[i])
        
        print('El/Los animales que menos partició/participaron en escenas fueron: ')
        if len(arrayMinAnimales) == 0:
            print(minAnimal.nombre + " con " + str(minAnimal.cantidad * 2) + " escenas")
        else:
            
            for animal in arrayMinAnimales:
                print(animal.nombre + " con " + str(animal.cantidad * 2) + " escenas")
            print(minAnimal.nombre + " con " + str(animal.cantidad * 2) + " escenas")

```
[Ir al contexto de la implementación](./lib/models/Espectaculo.py#L63)

---

#### Escena de menor grandeza <a name="id33"></a>
Para cumplir con este requerimiento, la clase Escena tiene una propiedad cuyo nombre es totalGrandeza, cada vez
que se realiza la instanciación de un objeto Escena, este calcula inmediatamente su total grandeza con la suma de las
grandezas de los animales que participan en la escena, almacenando el valor la propiedad, para luego ser usada en el método
minGradezaEscena del la clase espectáculo, la cual tiene acceso a todas las escenas y aplica un algritmo con complejidad O(k)
(con k cantidad de escenas) para encontrar la escena con grandeza total mínima

``` python

    def minGradezaEscena(self):
        """ Algoritmo para calcular la escena con menor grandeza 
            con complejidad O(k) (número de escenas)"""
        minEscena = self.escenas[0]
        for i in range(1, len(self.escenas)):
            if self.escenas[i].totalGrandeza < minEscena.totalGrandeza:
                minEscena = self.escenas[i]

        print('La escena de menor grandeza total fue:')
        print(minEscena)

```
[Ir al contexto de la implementación](./lib/models/Espectaculo.py#L35)

---


#### La escena de mayor grandeza total <a name="id34"></a>
Al igual que en la escena de menor grandeza, se realiza el mismo procedimiento sólo que esta vez se usa el método de la 
clase espéctaculo llamado maxGradezaEscena, el cual nos permite calcular la escena con mayor grandeza cuya complejidad
es O(k)

``` python

    def maxGradezaEscena(self):
        """ Algoritmo para calcular la escena con mayor grandeza 
            con complejidad O(k) (número de escenas)"""
        maxEscena = self.escenas[0]
        for i in range(1, len(self.escenas)):
            if self.escenas[i].totalGrandeza > maxEscena.totalGrandeza:
                maxEscena = self.escenas[i]

        print('La escena de mayor grandeza total fue:')
        print(maxEscena)

```
[Ir al contexto de la implementación](./lib/models/Espectaculo.py#L25)

---


#### Promedio de grandeza del espéctaculo <a name="id35"></a>
Debido a que se conoce la cantidad de escenas, la cantidad de partes del espectáculo y los animales que participan en ello,
se implementó un método llamado promedioGradezaEspectaculo en la clase Espectáculo que realiza la sumatoria de la grandeza total de todas las escenas y las divide (calculo del promedio) por m*k*2, el cuál indica la cantidad total de escenas que dieron lugar en el espectáculo.

``` python

    def promedioGradezaEspectaculo(self):
        """ Algoritmo para calcular el promedio del espectaculo (escenas) con 
            complejidad O(k) (número de escenas)"""
        contador = 0
        for escena in self.escenas:
            contador += escena.totalGrandeza
        contador *= 2

        promedio = contador / (((self.m -1) * self.k) * 2)

        print('El promedio de grandeza total del espectaculo fue de:')
        print(round(promedio,2))


```
[Ir al conexto de la implementación](./lib/models/Espectaculo.py#L13)

---


## 👨‍🔬 Análisis general de resultados  <a name="id26"></a>

Análisis realizado tomando muestras de arreglos(numéricos) de cien(100) tamaños diferentes ordenandolos con los
algoritmos de distintas complejidades para poder obtener su comparación.

![grafico1](https://user-images.githubusercontent.com/37484798/82126397-1ace1200-9772-11ea-8d97-79c098ae9e64.png)

---


## 🎉 Conclusiones del proyecto <a name="id27"></a>


## 💻 Correr script online <a name="id100"></a>
[Ir a la implementación online](https://repl.it/@MiguelCardona/The-Animal-Show)
Puedes correr la implementcion desde el navegador haciendo uso de una maquina virtual de linux; con la plataforma [repl.it](https://repl.it/).

### Comentarios anexos
Esta implementacion (software) requiere tener python3.  ***En maquinas macOS se pueden presenta errores por la implementacion integrada de python 2.7 del sistema operativo.*** Recomendamos el uso de la consola de intepretación de Visual Studio Code, o en su defecto usar el interpretador online.




