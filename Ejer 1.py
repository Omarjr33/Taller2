"""Escribe un programa que solicite al usuario ingresar su edad y luego
determine si es mayor de edad o no utilizando una declaración if. Si la edades mayor o igual a 18, 
muestra elmensaje "Eres mayor de edad", de lo contrario, muestra el mensaje "Eres menor de edad"."""
from os import name

def edadMayorMenor (edad:int):

    if (edad >= 18):   
        print ("Eres mayor de edad")
    else:
        print ("Eres menor de edad")

if (__name__=='__main__'):
    edad = int(input("ingrese una edad: "))
    edad = edadMayorMenor (edad)
