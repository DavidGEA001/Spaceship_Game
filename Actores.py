import time
import random

if __name__ == "__main__":
    print("Este archivo no se puede utilizar tal cual, debes importarlo en main.py")


class ObjetoDelJuego:
    x = 10
    y = 8
    dibujo = "x"
    velocidad_x = 1
    __id = 0

    def pintar(self, escena):
        for num_fila, fila in enumerate(escena):
            for num_columna, columna in enumerate(fila):
                if(num_fila == self.y and num_columna == self.x):
                    escena[num_fila][num_columna] = self.dibujo

    def mover(self):
        decision = random.choice ([True, True, True, False])
        if (decision == False):
            return
        if(self.x == 18):
            self.velocidad_x = -1
        if(self.x == 1):
            self.velocidad_x = 1
        self.x = self.x + self.velocidad_x

    #Getter
    def mostrarID(self):
        return self.__id
    #Setter
    def setearID(self):
        self.__id = time.time()


class Jugador(ObjetoDelJuego):
    dibujo = "^"
    def __init__(self, columna):
        self.x = columna


class Enemigo(ObjetoDelJuego):
    y = 1
    dibujo = "v"
    def __init__(self, columna):
        self.x = columna


class Bala(ObjetoDelJuego):
    __enEspera = True
    velocidad_y = 1
    def __init__(self, columna, fila, caracter = "º"):
        self.x = columna
        self.y = fila
        self.dibujo = caracter

    def mover(self):
        if (self.__enEspera == False):

            self.y = self.y + self.velocidad_y
            if self.y == 9:
                self.y = 10
                self.__enEspera = True
            elif self.y == 0:
                self.y = -1
                self.__enEspera = True

    def estaEnEspera(self):
        return self.__enEspera

    def Disparar(self, ObjetoDelJuego, velocidad_y):
        self.x = ObjetoDelJuego.x
        self.y = ObjetoDelJuego.y + velocidad_y
        self.__enEspera = False
        self.velocidad_y = velocidad_y
