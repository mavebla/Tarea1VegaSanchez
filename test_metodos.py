import metodos
import string
# se crea una lista con todas las letras en minuscula
abc = list(string.ascii_lowercase)
# se crea una lista con todas las letras en mayuscula
ABC = list(string.ascii_uppercase)


# funcion que comprueba los casos de exito de la funcion check_char
def test_check_char1():
    # se comprueba que con cada letra en minsucula, la funcion retorne 0
    for letra in abc:
        result = metodos.check_char(letra)
        assert result == 0
    # se comprueba que con cada letra en mayuscula, la funcion retorne 0
    for letra in ABC:
        result = metodos.check_char(letra)
        assert result == 0


# funcion que comprueba los casos de exito de la funcion caps_switch
def test_caps_switch1():
    # se comprueba que la funcion haya convertido
    # a todas las letras en mayusculas:
    for letra in abc:
        result = metodos.caps_switch(letra)
        assert result == letra.upper()
    # por cada letra de la lista abc,
    # se comprueba que la funcion las haya hecho minusculas
    for letra in ABC:
        result = metodos.caps_switch(letra)
        assert result == letra.lower()


# funcion que comprueba los casos negativos de la funcion check_char
def test_check_char2():
    # se prueba la funcion con un string de mas de un caracter
    result = metodos.check_char("Hola")
    # se comprueba que se haya retornado el codigo de error correcto
    assert result == "Error 289: Se recibió más de un carácter"
    # se crea una lista con caracteres que no son letras
    listnum = ['1', '2', '3']
    # se comprueba que con cada elemento de la listnum se de
    # el codigo de error correspondiente
    for num in listnum:
        result = metodos.check_char(num)
        assert result == "Error 463: El carácter recibido no es una letra"
    # se comprueba que al introducir un entero a la funcion,
    # se ejecute el codigo de error correcto
    assert metodos.check_char(1) == "Error 701: No se introdujo un string"
