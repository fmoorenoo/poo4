import pytest
from ejemploExcepciones import EjemploExcepciones

def test_dividirEntreCero():
    ejemplo = EjemploExcepciones()
    with pytest.raises(ZeroDivisionError):
        ejemplo.dividirEntreCero(a=2, b=0)

    assert ejemplo.dividirEntreCero(a = 4, b = 2) == 2


def test_valorIncorrecto():
    ejemplo = EjemploExcepciones()
    with pytest.raises(ValueError):
        ejemplo.valorIncorrecto(a=2, b=0.5)

    assert ejemplo.valorIncorrecto(a = 4, b = 2) == 2


def test_archivoNoEncontrado():
    ejemplo = EjemploExcepciones()
    with pytest.raises(FileNotFoundError):
        ejemplo.dividirEntreCero()


def test_errorDeTipo():
    ejemplo = EjemploExcepciones()
    with pytest.raises(TypeError):
        ejemplo.errorDeTipo(a=2, b="0")

    assert ejemplo.errorDeTipo(a = 4, b = 2) == 8


def test_errorDePosicion():
    ejemplo = EjemploExcepciones()
    with pytest.raises(IndexError):
        ejemplo.errorDePosicion(["a", "b", "c"], 5)


def test_interrupcionTeclado():
    ejemplo = EjemploExcepciones()
    with pytest.raises(KeyboardInterrupt):
        ejemplo.interrupcionTeclado()

    assert ejemplo.interrupcionTeclado(a = 4, b = 2) == 2