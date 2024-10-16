"""Crea un programa que solicite al
usuario un número entero positivo y
luego imprima los números desde ese
número hasta 1 utilizando un
buclewhile."""

def numeroEntero (numero:int):
    while numero >= 1:
            print(numero)
            numero -= 1 
    else:
        print("Por favor, ingresa un número entero positivo.")

if (__name__=='__main__'):
   numero = int(input("Ingresa un número entero positivo: "))
   numeroEntero(numero)


