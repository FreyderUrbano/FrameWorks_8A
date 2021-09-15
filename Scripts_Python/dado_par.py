"""
Descripcion: script que permita lanzar los dados de manera indefinida y solo 
finalizara cuando se genere un PAR de DADOS (1,1 2,2 3,3 4,4 5,5)
"""
"""
UN SOLO JUGADOR LANZA LOS dados
DEBE RECORRER DE CERO A 100
EL PUEDE TERMINAR CUANDO:
    -- EL JUGADOR OPTENGA DOS PARES CONCECUTIVOS
    -- CUANDO LLEGUE A LA META DE 100+
"""
import os
from random import randint

#Funciones
def dados():
    status = True

    while status:    #WHILE STATUS == TRUE
        os.system("clear")
        dado1 = randint(1,6)
        dado2 = randint(1,6)
    
        print("D1", dado1)
        print("D2", dado2)

        if dado1 == dado2:
            status = False
            print("SON PARES.FIN DEL JUEGO")
        else:
            key = input("LANZAR NUEVAMENTE")
#Main
d = dados()

"""
'''
    Description: Script en Python que permita lanzar los dados de manera indefinida Y sólo 
    finalizará cuando se genere un PAR de DADOS (1,1 - 2,2 - 3,3 - 4,4 - 5,5 - 6,6)
'''
import os
from random import randint

#Functions
def dices() :
    status = True

    while status :     #while status ==> while status == True
        os.system("clear")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("D1: ", dice1)
        print("D2: ", dice2)

        if dice1 == dice2 :
            status = False
            print("::: Los dados son pares. El lanzamiento ha finalizado :::")
        else :
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")    

#Main
dices()
"""
