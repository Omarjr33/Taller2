"""Crea un programa que solicite al usuario
ingresar una serie de números positivos y
luego calcule e imprima el promedio de los
números ingresados utilizando un bucle while.
El programa debe terminar cuando el usuario
ingrese un número negativo."""

def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

if __name__ == '__main__':
    numeros = []
    while True:
        numero = float(input("Ingresa un número positivo (o un número negativo para terminar): "))
        
        if numero < 0:
            break
        
        numeros.append(numero)
    
    promedio = calcular_promedio(numeros)
    
    print(f"El promedio de los números ingresados es: {promedio:.2f}")