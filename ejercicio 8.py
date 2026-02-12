#Cree una función agregar_numero(lista, numero) que agregue un número a una lista existente.

def agregar_numero(lista, numero):
    lista.append(numero)
    return lista

mi_lista = [10, 20, 30]
print("Lista inicial:", mi_lista)

num = int(input("Escribe un número para agregar a la lista: "))
mi_lista = agregar_numero(mi_lista, num)

print("Lista actualizada:", mi_lista)
