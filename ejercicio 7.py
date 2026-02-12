#Cree una función cuadrado_y_cubo(n) que devuelva el cuadrado y el cubo del número.

def cuadrado_y_cubo(n):
    return n ** 2, n ** 3

num = int(input("Escribe un número: "))
cuadrado, cubo = cuadrado_y_cubo(num)

print(f"El cuadrado de {num} es: {cuadrado}")
print(f"El cubo de {num} es: {cubo}")
