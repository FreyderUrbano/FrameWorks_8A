'''
Developer : Freyder
Date: 14 septiembre 2021
Descripcion: Script Python que permite identificar EL MAYOR DE DOS NUMEROS
''' 

print("CALCULADORA BASICA")

numero1 = int(input("INGRESA EL PRIMER NUMERO: "))
numero2 = int(input("INGRESA EL SEGUNDO NUMERO: "))

print("TIPO DE DATO: ", type(numero1))
print("TIPO DE DATO: ", type(numero2))

suma = numero1 + numero2
print(suma)

#CALCULO DE QUE NUMERO ES MAYOR'

if numero1 > numero2:
    print(numero1," ES MAYOR QUE: ", numero2)
elif numero1 < numero2:
    print(numero2, "ES MAYOR")
else:
    print("LOS NUMEROS SON IGUALES.")
print("Fin.")