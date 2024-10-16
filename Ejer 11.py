"""En su casa le solicitan que
realice un algoritmo en Python,
que permita calcular el valor a
pagar por concepto de energía
eléctrica. Los datos que se
conocen son los siguientes:
-Mes de consumo
-Valorkw

-Totalkwconsumido en el mes-
estrato"""

def obtener_precio_por_kwh(mes):
    precios_por_mes = {
        "enero": 0.20,
        "febrero": 0.18,
        "marzo": 0.22,
        "abril": 0.21,
        "mayo": 0.23,
        "junio": 0.25,
        "julio": 0.24,
        "agosto": 0.26,
        "septiembre": 0.22,
        "octubre": 0.23,
        "noviembre": 0.20,
        "diciembre": 0.19
    }
    return precios_por_mes.get(mes.lower(), 0.20)  

def aplicar_tarifa_por_estrato(costo, estrato):
    tarifas_por_estrato = {
        1: 0.90,  
        2: 1.00,  
        3: 1.10,  
        4: 1.20   
    }
    return costo * tarifas_por_estrato.get(estrato, 1.00)  

if __name__=='__main__':
    try:
        mes = input("Ingrese el mes de consumo: ")
        total_kwh = float(input("Ingrese el total de kWh consumidos en el mes: "))
        estrato = int(input("Ingrese el estrato del usuario (1-4): "))

        precio_por_kwh = obtener_precio_por_kwh(mes)
        
        costo_total = total_kwh * precio_por_kwh
        
        costo_total_ajustado = aplicar_tarifa_por_estrato(costo_total, estrato)
        
        print(f"\nValor a pagar por concepto de energía eléctrica: ${costo_total_ajustado:.2f}")
    
    except ValueError:
        print("Error: Por favor, ingrese valores válidos para kWh y estrato.")
