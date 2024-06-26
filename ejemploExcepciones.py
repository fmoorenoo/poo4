class EjemploExcepciones:
    # ZeroDivisionError
    def zeroDivisionError(self, num: int, den: int) -> int:
        if den == 0:
            raise ZeroDivisionError
        return num // den


    # ValueError
    def valueError(self, a=0.5) -> int:
        if isinstance(a, int):
            return a
        raise ValueError


    # FileNotFoundError
    def fileNotFoundError(self) -> str:
        archivo = "archivoImaginario.txt" 
        try:
            with open(archivo, 'r') as file:
                contenido = file.read()
            return contenido
        except FileNotFoundError:
            raise FileNotFoundError


    # TypeError
    def typeError(self, a: int, b: int) -> int:
        try:
            return a * "b"
        except TypeError:
            raise TypeError


    # PermissionError
    def permissionError(self) -> None:
        try:
            archivo = open("archivoPrueba.txt", "r")
            archivo.write("hola")
        except:
            raise PermissionError
        

    # IndexError
    def indexError(self):
        lista = ["a", "b", "c"]
        posicion = 5
        try:
            return lista[posicion]
        except IndexError:
            raise IndexError
    

    # KeyboardInterrupt
    def keyboardInterrupt(self) -> None:
        try:
            for x in range(10):
                input()
                if not KeyboardInterrupt:
                    pass
        except:
            raise KeyboardInterrupt


    # UnicodeDecodeError
    def unicodeDecodeError(self):
        try:
            texto = b'\xff'
            decodificador = texto.decode('utf-8')
        except UnicodeDecodeError as e:
            raise UnicodeDecodeError(e.encoding, e.object, e.start, e.end, e.reason)


    # AttributeError
    def attributeError(self) -> None:
        try:
            objeto = None
            objeto.atributo
        except AttributeError:
            raise AttributeError