from datetime import datetime
import re


class Cliente:
    def __init__(self, id_cliente, nombre, email, direccion, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"{self.id_cliente} - {self.nombre}"


class Servicio:
    def __init__(self, id_servicio, nombre, precio):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.id_servicio}. {self.nombre} - ${self.precio}"


# ==========================
# MOTOR DE NOTIFICACIONES
# ==========================
class Notificador:
    @staticmethod
    def enviar_email(cliente, total):
        print("\n NOTIFICACIÓN ENVIADA")
        print(f"Para: {cliente.email}")
        print(f"Hola {cliente.nombre}, su factura por ${total:.2f} fue generada correctamente.\n")


class Factura:
    contador = 1

    def __init__(self, cliente):
        self.numero = Factura.contador
        Factura.contador += 1

        self.cliente = cliente
        self.servicios = []
        self.fecha = datetime.now()

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def calcular_subtotal(self):
        return sum(s.precio for s in self.servicios)

    def calcular_descuento(self):
        if len(self.servicios) >= 2:
            return self.calcular_subtotal() * 0.30
        return 0

    def calcular_total(self):
        return self.calcular_subtotal() - self.calcular_descuento()

    def mostrar_factura(self):
        print("\n=================================")
        print("         TECH SOLUTIONS")
        print("=================================")
        print(f"Factura N°: {self.numero}")
        print(f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}")
        print(f"Cliente: {self.cliente.nombre}")
        print("\nServicios:")

        for s in self.servicios:
            print(f"- {s.nombre}: ${s.precio}")

        print("---------------------------------")
        print(f"Subtotal: ${self.calcular_subtotal():.2f}")
        print(f"Descuento: -${self.calcular_descuento():.2f}")
        print(f"TOTAL: ${self.calcular_total():.2f}")
        print("=================================\n")


class SistemaTechSolutions:
    def __init__(self):
        self.clientes = []
        self.servicios = [
            Servicio(1, "Desarrollo", 2000),
            Servicio(2, "Soporte", 800),
            Servicio(3, "Consultoría", 1500),
            Servicio(4, "Auditoría", 1200)
        ]


    def validar_nombre(self):
        while True:
            nombre = input("Nombre: ").strip()
            if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]{3,}", nombre):
                return nombre
            print(" El nombre debe tener mínimo 3 letras y solo contener letras.")

    def validar_email(self):
        while True:
            email = input("Email: ").strip()
            patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
            if re.fullmatch(patron, email):
                if not any(c.email == email for c in self.clientes):
                    return email
                else:
                    print(" Este correo ya está registrado.")
            else:
                print(" Email inválido.")

    def validar_direccion(self):
        while True:
            direccion = input("Dirección: ").strip()
            if direccion:
                return direccion
            print(" La dirección no puede estar vacía.")

    def validar_telefono(self):
        while True:
            telefono = input("Teléfono: ").strip()
            if telefono.isdigit() and len(telefono) >= 10:
                return telefono
            print(" El teléfono debe tener mínimo 10 números y solo contener dígitos.")

   
    def registrar_cliente(self):
        print("\n--- REGISTRO DE CLIENTE ---")

        nombre = self.validar_nombre()
        email = self.validar_email()
        direccion = self.validar_direccion()
        telefono = self.validar_telefono()

        id_cliente = len(self.clientes) + 1
        cliente = Cliente(id_cliente, nombre, email, direccion, telefono)
        self.clientes.append(cliente)

        print(" Cliente registrado correctamente.\n")

    def listar_servicios(self):
        print("\n--- SERVICIOS DISPONIBLES ---")
        for servicio in self.servicios:
            print(servicio)

    def crear_factura(self):
        if not self.clientes:
            print("⚠ No hay clientes registrados.")
            return

        print("\n--- SELECCIONE CLIENTE ---")
        for cliente in self.clientes:
            print(cliente)

        try:
            id_cliente = int(input("Ingrese ID del cliente: "))
        except ValueError:
            print(" Debe ingresar un número.")
            return

        cliente = next((c for c in self.clientes if c.id_cliente == id_cliente), None)

        if not cliente:
            print(" Cliente no encontrado.")
            return

        factura = Factura(cliente)

        while True:
            self.listar_servicios()
            try:
                opcion = int(input("Seleccione servicio (0 para terminar): "))
            except ValueError:
                print(" Entrada inválida.")
                continue

            if opcion == 0:
                break

            servicio = next((s for s in self.servicios if s.id_servicio == opcion), None)

            if servicio:
                factura.agregar_servicio(servicio)
                print(" Servicio agregado.")
            else:
                print(" Servicio inválido.")

        if not factura.servicios:
            print("No se agregaron servicios.")
            return

        factura.mostrar_factura()
        Notificador.enviar_email(cliente, factura.calcular_total())

    def menu(self):
        while True:
            print("========= TECH SOLUTIONS =========")
            print("1. Registrar Cliente")
            print("2. Crear Factura")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.crear_factura()
            elif opcion == "3":
                print("Saliendo del sistema...")
                break
            else:
                print(" Opción inválida.")



if __name__ == "__main__":
    sistema = SistemaTechSolutions()
    sistema.menu()

