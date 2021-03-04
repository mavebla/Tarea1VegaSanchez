# Función check_char
def check_char(char):
    string = isinstance(char, str)
    if not string:
        return("Error 701: No se introdujo un string")
    # comprobar que sea solo un carácter
    if len(char) == 1:
        if char.isalpha() is True:
            # retorna 0 si es solo una letra
            return(0)
        else:
            # si no es una letra retorna este error
            return("Error 463: El carácter recibido no es una letra")
    else:
        # si contiene más de un carácter retorna este error
        return("Error 289: Se recibió más de un carácter")


def caps_switch(char):
    # si la función check_char retornó 0, se cambia a mayúsculas o minúsculas
    if check_char(char) == 0:
        return(char.swapcase())
    # se comprueba el código de error que retornó la función anterior
    elif check_char(char) == "Error 701: No se introdujo un string":
        return("Error 701: No se introdujo un string")
    elif check_char(char) == "Error 463: El carácter recibido no es una letra":
        return("Error 463: El carácter recibido no es una letra")
    elif check_char(char) == "Error 289: Se recibió más de un carácter":
        return("Error 289: Se recibió más de un carácter")
