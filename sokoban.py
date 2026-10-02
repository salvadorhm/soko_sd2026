class Sokoban:
    """
    0 - personaje
    1 - caja
    2 - pared
    3 - meta
    4 - camino
    5 - caja_meta
    6 - personaje_meta
    """

    def __init__(self) -> None:
        # Definir el mapa
        self.mapa = [
            [2, 4, 4, 0, 4, 4, 2],
        ]
        # Definir la posicion inicial del personaje
        self.personaje_fila = 0
        self.personaje_columna = 3

    def imprmirMapa(self) -> None:
        # Toma cada fila del mapa y la imprime
        for fila in self.mapa:
            print(fila)

    def derecha(self) -> None:
        # TODO: 1. Personaje,Camino [0,4] -> [4,0]
        # TODO: 2. Personaje,Meta [0,3] -> [4,6]


        # 1. Personaje,Camino [0,4] -> [4,0]
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.personaje_columna = self.personaje_columna + 1

    def jugar(self) -> None:
        """
        a - Izquierda
        d - Derecha
        w - Arriba
        s - Abajo
        """

        self.imprmirMapa()
        movimiento = input("Movimiento: ")
        if movimiento == "d":
            self.derecha()
        elif movimiento == "a":
            pass
        elif movimiento == "w":
            pass
        elif movimiento == "s":
            pass


soko = Sokoban()
soko.jugar()
