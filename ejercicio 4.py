#Cree una función es_par(numero) que devuelva True si el número es par y False si es impar.

def es_par(numero):
    return numero % 2 == 0

num = int(input("Escribe un número: "))


print("si es par (true), si es impar (false) : ", es_par(num)) 