import pytest
from indexError import posicionLista

def test_posicionLista():
    lista = ["fútbol", "baloncesto", "tenis"]
    assert posicionLista(lista, 5) == None
    assert posicionLista(lista, 0) == "fútbol"
    assert posicionLista(lista, 2) == "tenis"
