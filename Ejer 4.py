"""Crea un programa que solicite al
usuario ingresar una contraseña y
verifique si cumple con los siguientes
requisitos: debe tener al menos 8
caracteres y contener al menos un
número. Si la contraseña cumple con
los requisitos, muestra el
mensaje"Contraseña válida". De lo
contrario, muestra el mensaje
"Contraseña inválida"."""


def tiene_longitud_valida(contraseña):
    return len(contraseña) >= 8

def contiene_numero(contraseña):
    for caracter in contraseña:
        if caracter.isdigit():
            return True
    return False

def validar_contraseña(contraseña):
    if tiene_longitud_valida(contraseña) and contiene_numero(contraseña):
        return "Contraseña válida"
    else:
        return "Contraseña inválida"
if __name__ == '__main__':
    contraseña = input("Ingresa una contraseña: ")
    print(validar_contraseña(contraseña))
