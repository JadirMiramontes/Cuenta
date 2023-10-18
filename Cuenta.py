class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def depositar(self, cantidad_a_depositar):
        if cantidad_a_depositar > 0:
            self.cantidad += cantidad_a_depositar

    def retirar(self, cantidad_a_retirar):
        if cantidad_a_retirar > 0:
            if cantidad_a_retirar <= self.cantidad:
                self.cantidad -= cantidad_a_retirar
            else:
                self.cantidad = 0

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.cantidad:.2f}"

# Función para ingresar una cantidad válida desde la consola
def ingresar_cantidad(mensaje):
    while True:
        try:
            cantidad = float(input(mensaje))
            if cantidad >= 0:
                return cantidad
            else:
                print("La cantidad debe ser mayor o igual a cero.")
        except ValueError:
            print("Ingrese una cantidad válida.")

# Ejemplo de uso interactivo:
titular = input("Ingrese el titular de la cuenta: ")
cuenta = Cuenta(titular)

while True:
    print("\nOpciones:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Ver Saldo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("")
        cantidad = ingresar_cantidad("Ingrese la cantidad a depositar: ")
        cuenta.depositar(cantidad)
    elif opcion == "2":
        print("")
        cantidad = ingresar_cantidad("Ingrese la cantidad a retirar: ")
        cuenta.retirar(cantidad)
    elif opcion == "3":
        print("")
        print(cuenta)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intente nuevamente.")