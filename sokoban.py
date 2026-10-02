class Sokoban:
    """ Juego del Sokoban en terminal
    """
    def __init__(self) -> None:
        # Definir elementos del juego
        # Útil si se quieren cambiar la asignación de los elementos
        self.elementos = {
            "personaje":0,
            "caja":1,
            "pared":2,
            "meta":3,
            "camino":4,
            "caja_meta":5,
            "personaje_meta":6
        }

        # Definir el mapa
        self.mapa = [
            [2, 2, 2, 2, 2, 2, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 4, 4, 0, 4, 4, 2],
            [2, 4, 4, 4, 4, 4, 2],
            [2, 2, 2, 2, 2, 2, 2],
        ]
        # Definir la posicion inicial del personaje
        self.personaje_fila = 2
        self.personaje_columna = 3

    def imprmirMapa(self) -> None:
        # Toma cada fila del mapa y la imprime
        for fila in self.mapa:
            # Convierte el array
            print(str(fila).replace("4"," "))

    def derecha(self) -> None:
        try:
            # TODO: 1. Personaje,Camino [0,4] -> [4,0]
            # TODO: 2. Personaje,Meta [0,3] -> [4,6]


            # 1. Personaje,Camino [0,4] -> [4,0]
            if (
                self.mapa[self.personaje_fila][self.personaje_columna] == self.elementos["personaje"]
                and self.mapa[self.personaje_fila][self.personaje_columna + 1] == self.elementos["camino"]
            ):
                # Coloca un camino donde estaba el personaje
                self.mapa[self.personaje_fila][self.personaje_columna] = self.elementos["camino"]
                # Coloca el personaje donde estaba el camino
                self.mapa[self.personaje_fila][self.personaje_columna + 1] =  self.elementos["personaje"]
                # Actuliza la nueva posición del personaje
                self.personaje_columna = self.personaje_columna + 1

        except KeyError as error:
            # Ocurre si no existe el elemento buscado
            print(f"Error: {error.args}")

    def izquierda(self) -> None:
        try:
            # TODO: 1. camino,personaje [4,0] -> [0,4]
            # TODO: 2. Meta,personaje [3,0] -> [6,4]


            # 1. Personaje,Camino [0,4] -> [4,0]
            if (
                self.mapa[self.personaje_fila][self.personaje_columna] == self.elementos["personaje"]
                and self.mapa[self.personaje_fila][self.personaje_columna - 1] == self.elementos["camino"]
            ):
                # Coloca un camino donde estaba el personaje
                self.mapa[self.personaje_fila][self.personaje_columna] = self.elementos["camino"]
                # Coloca el personaje donde estaba el camino
                self.mapa[self.personaje_fila][self.personaje_columna - 1] =  self.elementos["personaje"]
                # Actuliza la nueva posición del personaje
                self.personaje_columna = self.personaje_columna - 1

        except KeyError as error:
            # Ocurre si no existe el elemento buscado en el diccionario elementos
            print(f"Error: {error.args}")

    def jugar(self) -> None:
        """
        a - Izquierda
        d - Derecha
        w - Arriba
        s - Abajo
        """
        while True:
            self.imprmirMapa()
            movimiento = input("Movimiento: ")
            if movimiento == "d":
                self.derecha()
            elif movimiento == "a":
                self.izquierda()
            elif movimiento == "w":
                pass
            elif movimiento == "s":
                pass
            elif movimiento == "q":
                break

soko = Sokoban()
soko.jugar()
