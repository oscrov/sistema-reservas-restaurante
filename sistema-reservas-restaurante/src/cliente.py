from utils import cargar_datos, guardar_datos

RUTA_CLIENTES = "../data/clientes.json"

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def guardar(self):
        clientes = cargar_datos(RUTA_CLIENTES)
        for cliente in clientes:
            if cliente["nombre"] == self.nombre and cliente["telefono"] == self.telefono:
                print(f"El cliente {self.nombre} ya está registrado.")
                return
        nuevo_cliente = {
            "id": len(clientes) + 1,
            "nombre": self.nombre,
            "telefono": self.telefono
        }
        clientes.append(nuevo_cliente)
        guardar_datos(RUTA_CLIENTES, clientes)
        print(f"Cliente {self.nombre} guardado con éxito.")

    @staticmethod
    def listar_clientes():
        return cargar_datos(RUTA_CLIENTES)
