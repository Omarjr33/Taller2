from datetime import datetime

def calcular_antiguedad(año_ingreso):
    año_actual = datetime.now().year
    return año_actual - año_ingreso

if __name__=='__main__':
    nombre = input("Ingrese el nombre del empleado: ")
    apellidos = input("Ingrese los apellidos del empleado: ")
    año_ingreso = int(input("Ingrese el año de ingreso a la empresa: "))
    telefono = input("Ingrese el teléfono del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    antigüedad = calcular_antiguedad(año_ingreso)
    print("\nInformación del Empleado:")
    print(f"Nombre: {nombre}")
    print(f"Apellidos: {apellidos}")
    print(f"Antigüedad: {antigüedad} años")
