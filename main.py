import generador
import time
import os
from Actores import Jugador, Enemigo, Bala
import random

if __name__ == "__main__":

    generadordeescenarios = generador.Generadordeescenarios()
    jugador = Jugador(columna= 2)
    enemigo = Enemigo(columna= 5)
    balaEnemiga = Bala(enemigo.x, enemigo.y +1)
    balaJugador = Bala(jugador.x, jugador.y -1)


    while True:
        os.system("cls")
        escenario = generadordeescenarios.generarescenario()
        jugador.pintar(escenario)
        enemigo.pintar(escenario)

        if (balaEnemiga.estaEnEspera() == True):
            desicion = random.choice([True, False])
            if desicion == True:
                balaEnemiga.Disparar(enemigo, 1)

        if (balaEnemiga.estaEnEspera() == False):
            balaEnemiga.pintar(escenario)

        if (balaJugador.estaEnEspera() == True):
            desicion = random.choice([True, False])
            if desicion == True:
                balaJugador.Disparar(jugador, -1)
        if (balaJugador.estaEnEspera() == False):
            balaJugador.pintar(escenario)


        # DIBUJAR ESCENA
        for fila in escenario:
            for columna in fila:
                print(columna, end='')
            print()

        if (balaJugador.x == enemigo.x and balaJugador.y == enemigo.y and balaEnemiga.x == jugador.x and balaEnemiga.y == jugador.y):
            print("Fin del juego")
            input("Haz Empatado")

        elif(balaJugador.x == enemigo.x and balaJugador.y == enemigo.y):
            print("Fin del juego")
            input("¡Haz Ganado!")
        elif (balaEnemiga.x == jugador.x and balaEnemiga.y == jugador.y):
            print("Fin del juego")
            input("Haz Perdido")

        time.sleep(0.05)
        jugador.mover()
        enemigo.mover()
        balaEnemiga.mover()
        balaJugador.mover()