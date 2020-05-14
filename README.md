#  🐧 The Animal Show

![languages](https://img.shields.io/github/languages/top/micardona96/FADA)
![Size](https://img.shields.io/github/repo-size/micardona96/FADA)
![commits](https://img.shields.io/github/commit-activity/m/micardona96/FADA)
![last-commit](https://img.shields.io/github/last-commit/micardona96/FADA)
![LICENSE](https://img.shields.io/github/license/micardona96/FADA)

Este proyecto se basa en la construcción de un software de ordenamiento que permita gestionar el itinerario y orden de prestación para el The animal show. La construcción del software está fundamentada en el análisis de complejidad de las escenas y partes del show, haciendo que en cada escena esta ordenada, tal que la aparición de los animales sea según su grandeza, además las partes del show también estarán ordenadas de forma ascendente, permitiendo que cada escena será mas grande que la anterior. Tomando en cuenta esto, disponemos de un espectáculo maravilloso.

**Índice**   
- [Lineamentos The Animal Show](#id1)
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
    
  - [Solución O (n²)](#id8)
    - [Análisis](#id9)
    - [Resultados](#id10)
    - [Aplicativo](#id11)
    - [Instrucciones de uso](#id12)
    - [Testing](#id13)
  - [Solución O (n log n) ](#id14)
    - [Análisis](#id15)
    - [Resultados](#id16)
    - [Aplicativo](#id17)
    - [Instrucciones de uso](#id18)
    - [Testing](#id19)
  - [Solución O (n)](#id20)
    - [Análisis](#id21)
    - [Resultados](#id21)
    - [Aplicativo](#id23)
    - [Instrucciones de uso](#id24)
    - [Testing](#id25)

  - [Análisis general de resultados ](#id26)
  - [Conclusiones del proyecto](#id27)


## Lineamentos The Animal Show <a name="id1"></a>
### Descripción <a name="id2"></a>
- The animal show contará con n animales como participantes del espectáculo. Además, el evento consistir a en m partes.
- Una primera parte: Una gran apertura del evento, que consiste en (m−1) ∗k escenas, donde en cada escena participan 3 animales distintos.

- Seguido de la apertura: se presentarán m − 1 partes de k escenas cada una, donde, al igual que en la apertura, en cada escena participan 3 animales distintos. 

- Una escena es un conjunto de 3 elementos (animales).

Es decir, el evento tiene m partes, de las cuales 1 parte es la Gran apertura y que se presenta primero, y luego de ella se presentan las siguientes m − 1 partes, para completar el Gran espectáculo.

> Nota: el criterio de desempate entre dos escenas que tengan la misma grandeza total de escena, se hace tomando la máxima grandeza individual de cada una de las escenas en empate, y se presentan las escenas en orden ascendente según la máxima grandeza individual de las escenas.

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

### [Clases](./models) <a name="id7"></a>

#### [Animal](./models/Animal.py)  <a name="id99"></a>
Clase encargada de crear objetos tipo Animal, estos objetos cuentan con 3 propiedades las cules son:

- Propiedades 
  - **String** *Nombre:* Nombre del animal.
  - **Int** *Grandeza:* Grandeza del animal en el espectaculo.
  - **Int** *Cantidad:* Cantidad de apariciones del animal en las escenas.

#### [Escena](./models/Escena.py) <a name="id98"></a>
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

#### [Parte](./models/Parte.py) <a name="id97"></a>
Clase encargada de crear objetos tipo Parte,la cual se encarga de agrupar objetos tipo Escena, cuenta con una propiedad y 2 metodos que ayudan a la estructuracion de sus contenedores en el objeto espectaculo.

- Propiedades 
  - **Array(Escena)** *Escenas:* Lista de escenas que conforma la parte de un espectaculo.
  
- Metodos
  - **getGrandezaTotal():** Calculo de la grandeza total de la parte (Complejidad O(N)).
  - **sortN():** Algoritmo de ordenamiento Counting Sort (Complejidad O(N)), se usa para ordenar las escenas dentro de las partes.
  
#### [Espectáculo](./models/Espectaculo.py)  <a name="id96"></a>
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

### Archivos y datos de pruebas
En este apartado se especificaran los datos de prueba y en qué archivo se encuentran para su posterior ejecución

### Solución O (n²)  <a name="id8"></a>
Para obtener una solución O (n²) al problema planteado, se realizó un análisis de los respectivos algortimos ya existentes
que tuvieran esta complejidad y elegimos usar el BubbleSort.

Como se mencionó en el análisis general, cada clase tiene implementado los mismos algoritmos de ordenamiento con sus distintas
complejidades, en este caso, los objetos (Escena, Parte, Espéctaculo) tienen una función llamada sortNxN que implementa BubbleSort.

(Captura Algoritmo)

Esta función sortNxN es llamada secuencialmente por todos los objetos de las distintas clases que lo implementan en el siguiente orden.

- Primero se ejecuta la función para todas las escenas que hacen parte del espectáculo para ordenarlas (Animales por su grandeza)
- Una vez ordenadas las escenas, las partes obtienen sus respectivas escenas y con base a la grandeza total de todas las escenas
ejecuta el llamada a sortNxN, ordenando así las partes internamente.
- Ya por último el objeto instancia de la clase Espéctaculo recibe todas las partes ordenadas por sus respectivas escenas, y hace uso de la
grandeza total por partes para ejecutar el algoritmo sortNxN (QuickSort) para ordenar todo el espéctaculo 



#### Análisis <a name="id9"></a>
#### Resultados <a name="id10"></a>
#### Aplicativo <a name="id11"></a>
#### Instrucciones de uso<a name="id12"></a>
#### Testing <a name="id13"></a>

### Solución O (n log n)  <a name="id14"></a>
Para obtener una solución O (n log n) al problema planteado, se realizó un análisis de los respectivos algortimos ya existentes
que tuvieran esta complejidad, entre los que vimos en el curso, resaltaron especialmente dos(2), MergeSort y QuickSort. Elegimos Quicksort
con pivote aleatorio debido a la comprensión que teniamos sobre el algoritmo, simplicidad de implementación y a sus buenos resultados (evidenciados) con grupos pequeños de datos.

Como se mencionó en el análisis general, cada clase tiene implementado los mismos algoritmos de ordenamiento con sus distintas
complejidades, en este caso, los objetos (Escena, Parte, Espéctaculo) tienen una función llamada sortNLogN que implementa QuickSort.

(Captura Algoritmo)

Esta función sortNLogN es llamada secuencialmente por todos los objetos de las distintas clases que lo implementan en el siguiente orden.

- Primero se ejecuta la función para todas las escenas que hacen parte del espectáculo para ordenarlas (Animales por su grandeza)
- Una vez ordenadas las escenas, las partes obtienen sus respectivas escenas y con base a la grandeza total de todas las escenas
ejecuta el llamada a sortNLogN, ordenando así las partes internamente.
- Ya por último el objeto instancia de la clase Espéctaculo recibe todas las partes ordenadas por sus respectivas escenas, y hace uso de la
grandeza total por partes para ejecutar el algoritmo sortNLogN (QuickSort) para ordenar todo el espéctaculo 

#### Análisis <a name="id15"></a>
#### Resultados <a name="id16"></a>
#### Aplicativo <a name="id17"></a>
#### Instrucciones de uso <a name="id18"></a>
#### Testing <a name="id19"></a>


### Solución O (n) <a name="id20"></a>
Para obtener una solución O (n) al problema planteado, se realizó un análisis de los respectivos algortimos ya existentes
que tuvieran esta complejidad, entre los que vimos en el curso, resaltó especialmente el CountingSort. Elegimos este algoritmo
debido a que funciona correctamente con rangos de datos definidos, en nuestro caso, el problema nos da los valores de m (cantidad de partes),
k (cantidad de escenas) y n (cantidad de animales)

Como se mencionó en el análisis general, cada clase tiene implementado los mismos algoritmos de ordenamiento con sus distintas
complejidades, en este caso, los objetos (Escena, Parte, Espéctaculo) tienen una función llamada sortN que implementa CountingSort.

(Captura Algoritmo)

Esta función sortN es llamada secuencialmente por todos los objetos de las distintas clases que lo implementan en el siguiente orden.

- Primero se ejecuta la función para todas las escenas que hacen parte del espectáculo para ordenarlas (Animales por su grandeza)
- Una vez ordenadas las escenas, las partes obtienen sus respectivas escenas y con base a la grandeza total de todas las escenas
ejecuta el llamada a sortN, ordenando así las partes internamente.
- Ya por último el objeto instancia de la clase Espéctaculo recibe todas las partes ordenadas por sus respectivas escenas, y hace uso de la
grandeza total por partes para ejecutar el algoritmo sortN (CountingSort) para ordenar todo el espéctaculo

#### Análisis <a name="id21"></a>
#### Resultados <a name="id22"></a>
#### Aplicativo <a name="id23"></a>
#### Instrucciones de uso <a name="id24"></a>
#### Testing <a name="id25"></a>

### Análisis general de resultados  <a name="id26"></a>

### Solución Estadísticas solicitadas por el gerente del Zoologico

## Animal que participó en más escenas dentro del espectáculo
Para obtener el animal que más participo en escenas se hizo uso de lo llamado paso por referencia,
los animales que participan en el espectáculo son creados una sola vez, por lo tanto, se comparte la misma
instancia de los animales en todas las escenas.

En cada escena se le suma en uno(1) la propiedad cantidad del objeto Animal, para así, ir contando la cantidad
de apariciones en escenas.

La complejidad de este mecanismo de conteo es O(1), debido a que en cada escena sólo participan tres(3) animales,
esto implica que el ciclo for usado para aumentar en 1 la propiedad cantidad del objeto sólo realice operaciones (iteraciones)
tres veces.

(imagen algoritmo)

## Animal que participó en menos escenas dentro del espectáculo
Al igual que el Animal que más participó en escenas, se hace uso de la misma idea, sólo que esta vez, en la clase espéctaculo
existen los métodos minParticipacionAnimal y maxParticipacionAnimal, que ejecuta un ciclo for n(cantidad de animales) veces,
para encontrar el máximo y el mínimo animal. La complejidad de este algoritmo es O(n), ya que realiza n iteraciones, recorriendo
todos los animales que participan en espectaculo en busqueda del que participa en más y menos escenas.

(imagen algoritmo)

## Escena de menor grandeza
Para cumplir con este requerimiento, la clase Escena tiene una propiedad cuyo nombre es totalGrandeza, cada vez
que se realiza la instanciación de un objeto Escena, este calcula inmediatamente su total grandeza con la suma de las
grandezas de los animales que participan en la escena, almacenando el valor la propiedad, para luego ser usada en el método
minGradezaEscena del la clase espectáculo, la cual tiene acceso a todas las escenas y aplica un algritmo con complejidad O(k)
(con k cantidad de escenas) para encontrar la escena con grandeza total mínima

(imagen algoritmo)

## La escena de mayor grandeza total.
Al igual que en la escena de menor grandeza, se realiza el mismo procedimiento sólo que esta vez se usa el método de la 
clase espéctaculo llamado maxGradezaEscena, el cual nos permite calcular la escena con mayor grandeza cuya complejidad
es O(k)

(imagen algoritmo)

## Promedio de grandeza del espéctaculo
Debido a que se conoce la cantidad de escenas, la cantidad de partes del espectáculo y los animales que participan en ello,
se implementó un método llamado promedioGradezaEspectaculo en la clase Espectáculo que realiza la sumatoria de la grandeza total de todas las escenas y las divide (calculo del promedio) por m*k*2, el cuál indica la cantidad total de escenas que dieron lugar en el espectáculo.

(imagen algoritmo)

### Conclusiones del proyecto <a name="id27"></a>

