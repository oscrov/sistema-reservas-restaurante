from cliente import Cliente
from mesa import Mesa
from reservacion import Reservacion

def main():
    # Crear un cliente y guardarlo
    cliente1 = Cliente("Oscar Román", "555-1234")
    cliente1.guardar()

    # Listar clientes registrados
    print("\nClientes registrados:")
    for cliente in Cliente.listar_clientes():
        print(cliente)

    # Listar mesas disponibles
    print("\nMesas disponibles:")
    for mesa in Mesa.listar_mesas():
        print(mesa)

    # Crear una reservación y guardarla
    reservacion1 = Reservacion(cliente_id=1, numero_mesa=2, fecha="2024-12-10", hora="20:00")
    reservacion1.guardar()

    # Listar reservaciones registradas
    print("\nReservaciones registradas:")
    for reservacion in Reservacion.listar_reservaciones():
        print(reservacion)

if __name__ == "__main__":
    main()
