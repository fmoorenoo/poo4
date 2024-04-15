import random
def posicionLista(lista:list, posicion:int):
    try:
        r = lista[posicion]
        return r
    except IndexError:
        print("IndexError!")
    else:
        print(f"Your wishes are my command: {r}")
    finally:
        print("Have a good day!")


if __name__ == "__main__":
    def main()->None:
        lista = ["pera", "uva", "plátano"]
        print(posicionLista(lista, 5))

    main()
    