class EjemploExcepciones:
    # ZeroDivisionError
    def dividirEntreCero(self, a:int, b:int) ->int:
        if (b == 0):
            raise ZeroDivisionError

        return a // b


    # ValueError
    def valorIncorrecto(self, a:int, b:int):
        try:
            return a / b

        except ValueError:
            raise ValueError
            

    # FileNotFoundError
    def archivoNoEncontrado(self, archivo):
        try:
            with open(archivo, 'r') as file:
                contenido = file.read()
            return contenido

        except FileNotFoundError:
            raise FileNotFoundError


    # TypeError
    def errorDeTipo(self):
        try:
            a * b

        except TypeError:
            raise TypeError

    
    # IndexError
    def errorDePosicion(self, lista, posicion):
        try:
            return lista[posicion]

        except IndexError:
            raise IndexError
    

    # KeyboardInterrupt
    def interrupcionTeclado(self):
        try:
            while True:
                pass

        except KeyboardInterrupt:
            raise KeyboardInterrupt

    # UnicodeDecodeError

    # AttributeError