"""Escribe un programa que solicite al usuario ingresar el día, el mes y el año de
una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes
casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
indicando si la fecha es válida o no."""

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False
def es_fecha_valida(dia, mes, anio):
    if mes < 1 or mes > 12:
        return False
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if es_bisiesto(anio):
        dias_en_mes[1] = 29
    if dia < 1 or dia > dias_en_mes[mes - 1]:
        return False

    return True
if __name__ == '__main__':
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))
    if es_fecha_valida(dia, mes, anio):
        print("La fecha es Bisiesto.")
    else:
        print("La fecha no es Bisiesto.")