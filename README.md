# SOKOBAN

## 1. Objetivo

### 1.1 General

Programar el juego Sokoban en una versión retro para consola.

### 1.2 Específicos

- Aplicar los conocimientos básicos de programación orientada a objetos con Python (Clases, Objetos, Métodos, Variables, Arrays, Bucles, Leer desde teclado, Decisiones, etc.).

- Utilizar ingeniería de software para analizar, diseñar y desarrollar el juego.

- Utilizar Kanban para dar seguimiento a las actividades a realizar ToDo, Doing, Done.

- Utilizar Hitos (Milestones) para cada una de las etapas del desarrollo.

- Documentar el código generado.

## 2. Reglas del juego

El juego sokoban consiste en recorrer un mapa en forma de laberinto para empujar cajas que estan repartidas en el mapa, hacia puntos determinados por las metas, y tiene las siguientes reglas:

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja hacia arriba, abjo, izquierda o derecha.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar todas las cajas sobre las metas.
5. El nivel de dificultad no está determinado necesariamente por la cantidad de cajas y metas.

## 3. Elementos del juego

Sokoban tiene 2 partes principales de juego, el mapa donde se va jugar y los elementos (personaje, cajas, metas, paredes y piso).

### 3.1 Mapa de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando números para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

````code
self.mapa = [
            [2, 2, 2, 2, 2, 2, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 4, 4, 0, 4, 4, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 2, 2, 2, 2, 2, 2],
        ]
````

### 3.2 Lista de elementos

Para esta versión del sokoban se utilizarán numeros para representar cada uno de los elementos del juego.

"personaje":0,
            "caja":1,
            "pared":2,
            "meta":3,
            "camino":4,
            "caja_meta":5,
            "personaje_meta":6

| Número | Interpretación |
| --- | --- |
| 0 | Personaje |
| 1 | Caja |
| 2 | Pared |
| 3 | Meta |
| 4 | Camino |
| 5 | Caja_meta |
| 6 | Personaje_meta |

## 4. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover:

| Letra | Dirección del movimiento |
| -- | -- |
| a | Izquierda |
| d | Derecha |
| w | Arriba |
| s | Abajo |

## 5. Modo de juego

El juego consiste mostrar el mapa y solicitar al usuario que escriba la letra hacia donde se quiere mover, despúes de colocar la letra se presiona enter, se evalua el moviento, si es un movimiento valido se realiza el cambio en el array, es decir se actualiza el mapa, y se repite este proceso forma infinita, hasta que se hayan terminado de acomodar todas las cajas sobre las metas.


## 6. Funciones a implementar

Después de realizar un análisis del juego sokoban se identifican funciones necesarias para completarlo, a continuación se crea una tabla con la lista de estas funciones para tener un mejor control sobre el avance del desarrollo del juego.

Para llevar un mejor control del avance del desarrollo se utiliza la metodología Kanban, indicando en que estatus de desarrollo se encuentra cada función del juego

| Valor | Interpretación |
| -- | -- |
| ToDo | Por hacer |
| Doing | Programando y validando |
| Done | Programada y validada con éxito |

### Ejemplo de seguimiento:

| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | ToDo | - |



### Ejemplo de Kanban trabajo en equipo

| No. | Función | Asignación | ToDo | Doing | Done | Fecha inicio | Fecha terminación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | Salvador | - | - | X | 18/Mar/2024 | 19/Mar/2024 |
| 1. | Repetir el juego hasta terminar el nivel. | Salvador | - |X | - | 19/Mar/2024 | - |

### 6.1 Funciones generales
| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | - | - |
| 1. | Repetir el juego hasta terminar el nivel. | - | - |
| 2. | Imprimir mapa.| - | - |
| 3. | Leer el movimiento. | - | - |
| 4. | Evaluar el movimiento del usuario. | - | - |

### 6.2 Derecha

Ejemplo de movimientos Inicio y Fin:

- Personaje, Espacio [0,4] -> Espacio, Personaje [4,0] |


| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 1. | Personaje, espacio  | - | [      ] | [     ] | - |
| 2. | Personaje, meta  | - | [      ] | [      ] |- |
| 3. | Personaje, caja, espacio | - | [      ] | [      ] | - |
| 4. | Personaje, caja,  meta | - | [      ] | [      ] | - |
| 5. | Personaje, caja_meta, espacio | - | [] | [] | - |
| 6. |Personaje, caja_meta, meta | - | [] | [] | - |
| 7. | Personaje_meta, espacio | - | [] | [] | - |
| 8. | Personaje_meta, meta | - | [] | [] | - |
| 9. | Personaje_meta, caja, espacio | - | [] | [] | - |
| 10. | Personaje_meta, caja, meta | - | [] | [] | - |
| 11. | Personaje_meta, caja_meta, espacio | - | [] | [] | - |
| 12. | Personaje_meta, caja_meta, meta | - | [] | [] | - |

### 6.3 Izquierda

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 1. | Personaje, espacio | - | [] | [] | - |
| 2. | Personaje, meta | - | [] | [] | - |
| 3. | Personaje, caja, espacio | - | [] | [] | - |
| 4. | Personaje, caja, meta | - | [] | [] | - |
| 5. | Personaje, caja_meta, espacio | - | [] | [] | - |
| 6. | Personaje, caja_meta, meta | - | [] | [] | - |
| 7. | Personaje_meta, espacio | - | [] | [] | - |
| 8. | Personaje_meta, meta | - | [] | [] | - |
| 9. | Personaje_meta, caja, espacio | - | [] | [] | - |
| 10. | Personaje_meta, caja, meta | - | [] | [] | - |
| 11. | Personaje_meta, caja_meta, espacio | - | [] | [] | - |
| 12. | Personaje_meta, caja_meta, meta | - | [] | [] | - |

### 6.4 Arriba

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 1. | Personaje, espacio | - | [][] | [][] | - |
| 2. | Personaje, meta | - | [][] | [][] | - |
| 3. | Personaje, caja, espacio | - | [][] | [][] | - |
| 4. | Personaje, caja, meta | - | [][] | [][] | - |
| 5. | Personaje, caja_meta, espacio | - | [][] | [][] | - |
| 6. | Personaje, caja_meta, meta | - | [][] | [][] | - |
| 7. | Personaje_meta, espacio | - | [][] | [][] | - |
| 8. | Personaje_meta, meta | - | [][] | [][] | - |
| 9. | Personaje_meta, caja, espacio | - | [][] | [][] | - |
| 10. | Personaje_meta, caja, meta | - | [][] | [][] | - |
| 11. | Personaje_meta, caja_meta, espacio | - | [][] | [][] | - |
| 12. | Personaje_meta, caja_meta, meta | - | [][] | [][] | - |

### 6.5 Abajo

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 1. | Personaje, espacio | - | [][] | [][] | - |
| 2. | Personaje, meta | - | [][] | [][] | - |
| 3. | Personaje, caja, espacio | - | [][] | [][] | - |
| 4. | Personaje, caja, meta | - | [][] | [][] | - |
| 5. | Personaje, caja_meta, espacio | - | [][] | [][] | - |
| 6. | Personaje, caja_meta, meta | - | [][] | [][] | - |
| 7. | Personaje_meta, espacio | - | [][] | [][] | - |
| 8. | Personaje_meta, meta | - | [][] | [][] | - |
| 9. | Personaje_meta, caja, espacio | - | [][] | [][] | - |
| 10. | Personaje_meta, caja, meta | - | [][] | [][] | - |
| 11. | Personaje_meta, caja_meta, espacio | - | [][] | [][] | - |
| 12. | Personaje_meta, caja_meta, meta | - | [][] | [][] | - |

### 6.6 Determina si se completo el nivel

Está función determina si todas las cajas estan en una meta, cuando esto sucede se debe cargar el siguiente nivel de juego.

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 1. | Evaluar si el nivel esta terminado (Esto sucede cuando todas las cajas estan sobre las metas), SI el nivel esta terminado cargar el siguiente nivel (Los niveles de juego estarán en archivos de texto independiente). | - | - |
| 2. | Reiniciar el mapa (Con la letra r, se vuelve a cargar el nivel que se esta jugando) | - | - |
