import random

def lanzar_dado():
    return random.randint(1, 6)

# Lanzar el dado
resultado = lanzar_dado()
print(f"El resultado del lanzamiento es: {resultado}")
