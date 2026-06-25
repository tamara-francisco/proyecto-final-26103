#Este programa permite:
# - Agregar productos
# - Ver productos
# - Buscar productos
# - Eliminar productos
# - Salir del programa

import sqlite3
import os

#-----------------------------------------
# CONEXIÓN Y CREACIÓN DE LA BASE DE DATOS
#-----------------------------------------
def conectar_db():
    """
    Conexión a la base de datos SQLite
    """
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    
    # Crear la tabla de productos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL
        )
    """)
    
    conn.commit()
    return conn

#--------------------------------
#       OPERACIONES CRUD
#--------------------------------
def agregar_producto(conn):
    """
    Pide datos al usuario y los agrega a la base de datos
    """
    print("\n--- Nuevo producto")
    while True:
        try:
            nombre = input("Nombre del producto: ").strip()
            if nombre == "":
                print("Error: El nombre del producto no puede estar vacío.")
                continue
            categoria = input("Categoría: ").strip()
            if categoria == "":
                print("Error: La categoría no puede estar vacía.")
                continue
            precio = float(input("Precio: $"))
            if precio > 0:
                break
            else:
                print("Error: El precio debe ser mayor a 0.")
        except ValueError:
            print("Error: Por favor, ingrese un precio válido. Por ejemplo: 10.99")

    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)", (nombre, categoria, precio))
        conn.commit()
        print(f"Producto '{nombre}' agregado exitosamente.")
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Error al agregar el producto: {e}")

def ver_productos(conn):
    """
    Muestra todos los productos en formato tabla
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, categoria, precio FROM productos ORDER BY id")
    filas_productos = cursor.fetchall()
    
    if filas_productos:
        print("\n----- Lista de productos -----")
        
        print("-" * 60)
        print(f"{'ID':<5} {'Nombre':<20} {'Categoría':<20} {'Precio':>10}")
        print("-" * 60)
        
        for producto in filas_productos:
            print(f"{producto[0]:<5} {producto[1]:<20} {producto[2]:<20} ${producto[3]:>9.2f}")
            print("-" * 60)
    else:
        print("No hay productos en la base de datos.")


def buscar_producto(conn, nombre):
    """
    Busca un producto por nombre en la base de datos
    """
    termino_busqueda = input("\nIngrese el nombre del producto a buscar: ").strip()
    if not termino_busqueda:
        print("Error: El nombre del producto no puede estar vacío.")
        return
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, categoria, precio FROM productos WHERE nombre LIKE ? ORDER BY id", ('%' + termino_busqueda + '%',))
    resultados_busqueda = cursor.fetchall()
    
    if resultados_busqueda:
        print(f"\n--- Se encontraron {len(resultados_busqueda)} productos ---")
        for producto in resultados_busqueda:
            print(f"   ID: {producto[0]}, Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: ${producto[3]:.2f}")
    else:
        print("No se encontraron productos con ese nombre.")
     
def eliminar_producto(conn, producto_id):
    """
    Elimina un producto de la base de datos por su ID
    """
    ver_productos(conn)
    try:
        producto_id = int(input("\n Ingresa el ID del producto a eliminar: ").strip())
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM productos WHERE id = ?", (producto_id,))
    fila_producto = cursor.fetchone()
    if not fila_producto:
        print(f"No se encontró ningún producto con ID {producto_id}.")
        return
    nombre_producto = fila_producto[0]
    print(f"\n¿Estás seguro de que deseas eliminar el producto '{nombre_producto}' con ID {producto_id}? (s/n)")
    confirmacion = input().strip().lower()
    if confirmacion == "s":
        cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        conn.commit()
        print(f"Producto '{nombre_producto}' con ID {producto_id} eliminado exitosamente.")
    else:
        print("Operación cancelada.")

#--------------------------------
#       MENU PRINCIPAL
#--------------------------------

def limpiar_pantalla():
    """
    Limpia la pantalla de la terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """
    Pausa la ejecución del programa hasta que el usuario presione Enter
    """
    input("\n Presiona Enter para continuar...")

def main():
    """
    Función principal del programa
    """
    conn = conectar_db()
    
    while True:
        print("-"* 50)
        print("-------- Sistema de Gestión de Productos ---------")
        print("-"* 50)
        print(" 1. Agregar producto")
        print(" 2. Ver productos")
        print(" 3. Buscar producto")
        print(" 4. Eliminar producto")
        print(" 5. Salir")
        print("-"* 50)
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_producto(conn)
            pausar()
        elif opcion == "2":
            ver_productos(conn)
            pausar()        
        elif opcion == "3":   
            buscar_producto(conn, "")
            pausar()
        elif opcion == "4":
            eliminar_producto(conn, 0)
            pausar()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida entre 1 y 5.")
            pausar()

    conn.close()

if __name__ == "__main__":
    main()