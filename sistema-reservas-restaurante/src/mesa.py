from utils import cargar_datos

RUTA_MESAS = "../data/mesas.json"

class Mesa:
    @staticmethod
    def listar_mesas():
        return cargar_datos(RUTA_MESAS)
