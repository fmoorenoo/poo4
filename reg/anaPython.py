import re
import rich
from rich import console, table


console = console.Console()
table = table.Table(header_style="green")
table.add_column("Funciones", style="dim", width=12)
table.add_column("Variables", style="dim", width=12)


class AnaPython:
    @staticmethod
    def countDef(codigo: str) -> int:
        patron = "def\\s+\\w+\\(.*\\)\\s*(->\\s*\\w+)?\\s*:"
        resultado = re.findall(patron, codigo)
        return len(resultado)

if __name__ == '__main__':
    funciones = '''
        def suma(a, b):
        def multipli(a: int, b: int) -> int:
        def error espacios():
        def imprimir():
        def sinDosPuntos()
        def sin_argumentos():
        defmalformada: '''
    cant = AnaPython.countDef(funciones)
    table.add_row(f"{cant} ", "0")
    console.print(table)
