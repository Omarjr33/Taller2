"""Crea un programa que pida al usuario ingresar el nombre de un país y luego
determine en qué continente se encuentra.Utiliza estructuras condicionales para
asociar cada país con su respectivo continente y muestra un mensaje con el
continente correspondiente."""

def continentes (conti):
    asia = ("Japón", "China","Mongolia", "Corea del Norte", "Corea del Sur", "Filipinas", "Vietnam")
    africa = ("Angola", "Luanda", "Argelia", "Argel", "Benín", "Porto Novo", "Botsuana", "Gaborone")
    américaDelNorte = ("Antigua y Barbuda", "Bahamas", "Barbados","Canadá","Costa Rica","Cuba","Dominica","Granda")
    américaDelSur = ("Argentina","Bolivia","Brasil","Chile","Colombia","Ecuador","Guyana","Perú")
    antártida = ("Argentina", "Australia", "Chile","Nueva Zelanda")
    europa = ("Bélgica", "Bulgaria", "Chequia", "Dinamarca", "Alemania", "Estonia", "Irlanda", "Grecia", "España", "Francia")
    oseania = ("Estados Unidos","Reino Unido","Francia","Nueva Zelanda","Australia")
    if conti in africa:
        return "África"
    elif conti in asia:
        return "asia"
    elif conti in américaDelNorte:
        return "America del norte"
    elif conti in américaDelSur:
        return "América america del sur"
    elif conti in europa:
        return "Europa"
    elif conti in antártida:
        return "Antartida"
    elif conti in oseania:
        return "Oseania"
    else:
        return continentes 
if (__name__=='__main__'):
    conti = input("Coloca el nombre del pais: ")
    continente = continentes(conti)
    print (f'El pais de {conti} se encuentra en {continente}')
