"""Escribe un programa que solicite al usuario
ingresar un número y luego muestre la tabla
de multiplicar de ese número del 1 al 10"""


def mostrar_tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

if __name__ == '__main__':
    numero = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))
    mostrar_tabla_multiplicar(numero)