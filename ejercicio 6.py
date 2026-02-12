#Cree una función tabla(numero) que muestre la tabla de multiplicar del número del 1 al 10.

def tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Escribe un número: "))
tabla(num)
