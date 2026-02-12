# Cree una función area_rectangulo(base, altura) que devuelva el área de un rectángulo.

def area_rectangulo(base, altura):
    return base * altura

base = float(input("Escribe la base del rectángulo: "))
altura = float(input("Escribe la altura del rectángulo: "))

print("El área del rectángulo es:", area_rectangulo(base, altura))