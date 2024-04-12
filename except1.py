import random
def intDiv(a:int, b:int) -> int:
    try:
        return a // b
    except:
        print("Realizamos tarea de control de cierre")


if __name__ == "__main__":
    for i in range(30):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        print(f"{a} // {b} = {intDiv(a, b)}")