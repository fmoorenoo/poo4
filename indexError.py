import random
def posicionLista(lista:list, posicion:int):
    try:
        return lista[posicion]
    except IndexError:
        print("IndexError - Realizamos tarea de control de cierre")

if __name__ == "__main__":
    def main()->None:
        lista = ["pera", "uva", "plátano"]
        print(posicionLista(lista, 5))

    main()
    