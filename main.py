from database.conexion import conectar_db
import services.funciones as funciones
from utils.helpers import pausar

def main():

    conn = conectar_db()

    while True:

        print("-" * 50)
        print("Sistema de Gestión de Productos")
        print("-" * 50)

        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            funciones.agregar_producto(conn)

        elif opcion == "2":
            funciones.ver_productos(conn)

        elif opcion == "3":
            funciones.buscar_producto(conn)

        elif opcion == "4":
            funciones.eliminar_producto(conn)

        elif opcion == "5":
            break

        else:
            print("Opción inválida")

        pausar()

    conn.close()

if __name__ == "__main__":
    main()