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

1. Plantear una solución al problema cuya complejidad sea O (n²) 
2. Plantear una solución al problema cuya complejidad sea O (n ∗ log(n)) 
3. Plantear una solución al problema cuya complejidad sea O (n)

## 🚀 Reporte The Animal Show <a name="id5"></a>
### Análisis general de la implementación <a name="id6"></a>
The animal show app hace uso lenguaje de programación Python que permite un paradigma orientados a objetos, además es un lenguaje interpretado, dinámico y su filosofía hace hincapié en la legibilidad de su código.

#### Clases <a name="id7"></a>
##### Animal
##### Escena
##### Parte
##### Espectáculo


### Solución O (n²)  <a name="id8"></a>
#### Análisis <a name="id9"></a>
#### Resultados <a name="id10"></a>
#### Aplicativo <a name="id11"></a>
#### Instrucciones de uso<a name="id12"></a>
#### Testing <a name="id13"></a>

### Solución O (n log n)  <a name="id14"></a>
#### Análisis <a name="id15"></a>
#### Resultados <a name="id16"></a>
#### Aplicativo <a name="id17"></a>
#### Instrucciones de uso <a name="id18"></a>
#### Testing <a name="id19"></a>


### Solución O (n) <a name="id20"></a>
#### Análisis <a name="id21"></a>
#### Resultados <a name="id22"></a>
#### Aplicativo <a name="id23"></a>
#### Instrucciones de uso <a name="id24"></a>
#### Testing <a name="id25"></a>

### Análisis general de resultados  <a name="id26"></a>


### Conclusiones del proyecto <a name="id27"></a>

