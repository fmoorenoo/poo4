import re

class RegExample:
    def __init__(self) -> None:
        pass

    @staticmethod
    def buscar(texto:str) -> list:
        patron = "\\b[aeiou]\\w*"
        resultado = re.findall(patron, texto)
        return resultado

    @staticmethod
    def validURL(url: str) -> bool:
        patron = "^https?://.+(\\w+[.#]\\w+[.#]?)"
        resultado = re.search(patron, url)
        if resultado is None:
            return False
        else:
            return True

        


if __name__ == '__main__':
    text = '''El auténtico mojo se elabora en mortero o almirez, lo que permite que cada ingrediente conserve su personalidad, y con todos los ingredientes en crudo, lo que hace que éstos conserven todas sus vitaminas y resultando por ello muy sanos. Aunque siempre hay una excepción a la regla, en este caso es el mojo palmero que lleva el ajo frito.
    No obstante, existe una manera de preparar el mojo rojo que es más fácil y, sobre todo, que requiere de cero esfuerzo físico. El único requisito es contar con una batidora de mano y seguir la receta que os damos a continuación. En cinco minutos tendréis la salsa lista para su consumo.'''
        
    print(RegExample.buscar(text))
    
    
    
