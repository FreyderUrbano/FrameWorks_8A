#JUEGO DE DADOS EN PYTON
from random import *
import os
print('==============')
print('JUEGO DE DADOS')
print('==============')

player1 = input("NOMBRE JUGADOR: ")

gameWin_player1 = 0

numgames = 1

continueGame = True

while (gameWin_player1 < 100) and continueGame:
    
    print("=======================")
    print("PARTIDA NRO: ",numgames)
    print("=======================")

    objetivo = randint(1,12)

    print("EL OBJETIVO ES: ", objetivo)

    num1player1 = randint(2,6)
    num2player1 = randint(2,6)
    sumaplayer1 = num1player1 + num2player1

    print("EL JUGADOR ", player1, " HA SACADO ", num1player1," y ",num2player1 )
    
    ganador = 0
    if sumaplayer1 == objetivo:
        ganador = player1
        print(player1, " HA GANADO.")
        gameWin_player1 = gameWin_player1 + 1

    elif num1player1 == num2player1:
        print('LOS DADOS SON IGUALES FIN DEL JUEGO.')
    
    #elif ganador == 1:
     #   if sumaplayer1 == objetivo:
      #      print("Ha ganado el jugador ", player1)
        
    #else:
        #print("EMPATE")

    continueGame = input("DESEAS CONTINUAR (S/N) " ) == "S"
            
    numgames = numgames + 1

print("GAME OVER")
print("SE HAN JUGADO ", numgames, " PATIDAS.")
if gameWin_player1 == 100:
    print("GANADOR: ", player1)
