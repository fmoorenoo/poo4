class EjemploExcepciones:
    # ZeroDivisionError
    def dividirEntreCero(self, a:int, b:int) ->int:
        if (b == 0):
            raise ZeroDivisionError

        return a // b


    # ValueError
    def valorIncorrecto(self, valor):
        try:
            return numero
        except ValueError:
            raise ValueError
            

    # FileNotFoundError
    def archivoNoEncontrado(self):
        try:
            with open(archivo, 'r') as file:
                contenido = file.read()
            return contenido

        except FileNotFoundError:
            raise FileNotFoundError("No se pudo encontrar el archivo")


    # TypeError
    def errorDeTipo(self):
        try:
            a * b

        except TypeError:
            raise TypeError("No se puede operar con el tipo de dato proporcionado")

    
    # IndexError

    # KeyboardInterrupt

    # UnicodeDecodeError

    # AttributeError

    pass