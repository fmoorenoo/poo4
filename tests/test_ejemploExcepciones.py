import pytest
from ejemploExcepciones import EjemploExcepciones

def test_dividirPorCero():
    ejemplo = EjemploExcepciones()
    with pytest.raises(ZeroDivisionError):
        ejemplo.dividirEntreCero(a=2, b=0)

    assert ejemplo.dividirEntreCero(a = 4, b = 2) == 2