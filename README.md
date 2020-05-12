#  🐧 The animal show

Este proyecto se basa en la construcción de un software de ordenamiento que permita gestionar el itinerario y orden de prestación para el The animal show. La construcción del software está fundamentada en el análisis de complejidad de las escenas y partes del show, haciendo que en cada escena esta ordenada, tal que la aparición de los animales sea según su grandeza, además las partes del show también estarán ordenadas de forma ascendente, permitiendo que cada escena será mas grande que la anterior. Tomando en cuenta esto, disponemos de un espectáculo maravilloso.

**Índice**   
- [Lineamentos The animal show](#id1)
  - [Descripción](#id2)
  - [Características adicionales](#id3)
  - [Requerimientos de optimización](#id4)
  
- [Reporte The animal show](#id5)
  - [Análisis general de la implementación ](#id6)
    - [Clases](#id7)
    
  - [Solución O (n²)](#id6)
    - [Análisis](#id7)
    - [Resultados](#id7)
    - [Aplicativo](#id7)
    - [Instrucciones de uso](#id7)
    - [Testing](#id7)

 - [Solución O (n log n) ](#id6)
    - [Análisis](#id7)
    - [Resultados](#id7)
    - [Aplicativo](#id7)
    - [Instrucciones de uso](#id7)
    - [Testing](#id7)

 - [Solución O (n)](#id6)
    - [Análisis](#id7)
    - [Resultados](#id7)
    - [Aplicativo](#id7)
    - [Instrucciones de uso](#id7)
    - [Testing](#id7)

 - [Análisis general de resultados ](#id6)
 - [Conclusiones del proyecto](#id6)


## Lineamentos The animal show
### Descripción
- The animal show contará con n animales como participantes del espectáculo. Además, el evento consistir a en m partes.
- Una primera parte: Una gran apertura del evento, que consiste en (m−1) ∗k escenas, donde en cada escena participan 3 animales distintos.

- Seguido de la apertura: se presentarán m − 1 partes de k escenas cada una, donde, al igual que en la apertura, en cada escena participan 3 animales distintos. 

- Una escena es un conjunto de 3 elementos (animales).

Es decir, el evento tiene m partes, de las cuales 1 parte es la Gran apertura y que se presenta primero, y luego de ella se presentan las siguientes m − 1 partes, para completar el Gran espectáculo.

> Nota: el criterio de desempate entre dos escenas que tengan la misma grandeza total de escena, se hace tomando la máxima grandeza individual de cada una de las escenas en empate, y se presentan las escenas en orden ascendente según la máxima grandeza individual de las escenas.

### Características adicionales
Adicionalmente, el gerente del The animal show desea saber ciertos datos acerca de su espectáculo: 
- El animal que participo en más escenas dentro del espectáculo y en cuantas participo. (En caso de haber empate entre animales, se deben mostrar todos) 
- El animal que menos participo en escenas dentro del espectáculo y en cuantas participo. (En caso de haber empate entre animales, se deben mostrar todos) 
- La escena de menor grandeza total. 
- La escena de mayor grandeza total. 
- El promedio de grandeza de todo el espectáculo (se tienen en cuenta todas las escenas, incluidas las de la apertura y las de los m−1 bloques siguientes).

### Requerimientos de optimización 

1. Plantear una solución al problema cuya complejidad sea O (n²) 
2. Plantear una solución al problema cuya complejidad sea O (n ∗ log(n)) 
3. Plantear una solución al problema cuya complejidad sea O (n)

## Reporte The animal show 
### Análisis general de la implementación 
The animal show app hace uso lenguaje de programación Python que permite un paradigma orientados a objetos, además es un lenguaje interpretado, dinámico y su filosofía hace hincapié en la legibilidad de su código.

#### Clases
##### Animal
##### Escena
##### Parte
##### Espectáculo


### Solución O (n²) 
#### Análisis 
#### Resultados
#### Aplicativo 
#### Instrucciones de uso
#### Testing

### Solución O (n log n) 
#### Análisis 
#### Resultados
#### Aplicativo 
#### Instrucciones de uso
#### Testing


### Solución O (n) 
#### Análisis 
#### Resultados
#### Aplicativo 
#### Instrucciones de uso
#### Testing

### Análisis general de resultados 


### Conclusiones del proyecto

