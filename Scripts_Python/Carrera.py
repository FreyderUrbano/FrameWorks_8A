''' 
REQUIERE SCRIPT EL JUEGO DE CARRERA NUMERICA CON DOS PLAYERS
LA CARRERA INICIA EN CERO Y FINALIZA EN POSICION 100
EL JUEGO SE 
EL PRIMERO QUE LLEGUE A 100 GANA
'''
import os
#ra

from random import randint, uniform
os.system("clear")

dado1 = randint(1,6)
dado2 = randint(1,6)

print("DADO 1: ", dado1)
print("DADO 2: ", dado2)