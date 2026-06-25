import sqlite3


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


def buscar_producto(conn):
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
     
def eliminar_producto(conn):
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