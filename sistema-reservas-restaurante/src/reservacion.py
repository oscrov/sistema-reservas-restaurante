from utils import cargar_datos, guardar_datos

RUTA_RESERVACIONES = "../data/reservaciones.json"
RUTA_MESAS = "../data/mesas.json"

class Reservacion:
    def __init__(self, cliente_id, numero_mesa, fecha, hora):
        self.cliente_id = cliente_id
        self.numero_mesa = numero_mesa
        self.fecha = fecha
        self.hora = hora

    def guardar(self):
        reservaciones = cargar_datos(RUTA_RESERVACIONES)
        for reservacion in reservaciones:
            if (reservacion["cliente_id"] == self.cliente_id and
                    reservacion["numero_mesa"] == self.numero_mesa and
                    reservacion["fecha"] == self.fecha and
                    reservacion["hora"] == self.hora):
                print(f"Ya existe una reservación para el cliente {self.cliente_id} en la mesa {self.numero_mesa} a esa hora.")
                return
        nueva_reservacion = {
            "id": len(reservaciones) + 1,
            "cliente_id": self.cliente_id,
            "numero_mesa": self.numero_mesa,
            "fecha": self.fecha,
            "hora": self.hora
        }

        # Actualizar disponibilidad de la mesa
        mesas = cargar_datos(RUTA_MESAS)
        for mesa in mesas:
            if mesa["numero"] == self.numero_mesa:
                if not mesa["disponible"]:
                    print(f"Error: La mesa {self.numero_mesa} no está disponible.")
                    return
                mesa["disponible"] = False
                break
        guardar_datos(RUTA_MESAS, mesas)

        reservaciones.append(nueva_reservacion)
        guardar_datos(RUTA_RESERVACIONES, reservaciones)
        print(f"Reservación para cliente {self.cliente_id} guardada con éxito.")

    @staticmethod
    def listar_reservaciones():
        return cargar_datos(RUTA_RESERVACIONES)
