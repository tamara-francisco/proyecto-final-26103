# 🛒 Sistema de Gestión de Productos

Aplicación de consola desarrollada en Python para la administración de inventario, utilizando SQLite para la persistencia de datos y una arquitectura modular orientada a buenas prácticas de desarrollo.

## 🎯 Objetivo

Este proyecto fue desarrollado como trabajo final del programa Talento Tech con el objetivo de aplicar conceptos fundamentales de desarrollo de software:

✅ Programación estructurada  
✅ Modularización de código  
✅ Persistencia de datos con SQLite  
✅ Manejo de excepciones  
✅ Validación de entradas  
✅ Control de versiones con Git y GitHub  

Más allá de cumplir con los requisitos funcionales, el foco estuvo en construir una solución organizada, mantenible y escalable.


## 🚀 Funcionalidades

### 📦 Gestión de productos

- ➕ Alta de productos
- 📋 Consulta de inventario
- 🔍 Búsqueda por nombre
- 🗑️ Eliminación de productos
- 💾 Persistencia automática en SQLite

### 🛡️ Validaciones implementadas

- ✔️ Control de campos obligatorios
- ✔️ Validación de precios numéricos
- ✔️ Prevención de registros inválidos
- ✔️ Confirmación antes de eliminar registros

### 👤 Experiencia de usuario

- 🖥️ Menú interactivo por consola
- 💬 Mensajes descriptivos para errores y confirmaciones
- 🎨 Visualización de productos en formato tabla
- ⚡ Navegación simple e intuitiva


## 🏗️ Arquitectura del proyecto

```text
proyecto-final-26103/
│
├── main.py
│
├── database/
│   └── conexion.py
│
├── services/
│   └── productos.py
│
├── utils/
│   └── helpers.py
│
└── inventario.db
```

### 📚 Responsabilidades por módulo

| Módulo | Responsabilidad |
|---------|---------|
| `main.py` | Control del flujo principal y menú |
| `database` | Conexión y creación de la base de datos |
| `services` | Operaciones CRUD y lógica de negocio |
| `utils` | Funciones auxiliares reutilizables |

💡 Esta separación permite mantener un código más limpio, escalable y fácil de mantener.


## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----|
| 🐍 Python 3 | Desarrollo de la aplicación |
| 🗄️ SQLite3 | Persistencia de datos |
| 🌿 Git | Control de versiones |
| 🐙 GitHub | Gestión y publicación del proyecto |
| 💻 VS Code | Entorno de desarrollo |


## 📸 Ejemplo de uso

```text
--------------------------------------------------
Sistema de Gestión de Productos
--------------------------------------------------
1. Agregar producto
2. Ver productos
3. Buscar producto
4. Eliminar producto
5. Salir
--------------------------------------------------
```

<img width="363" height="356" alt="image" src="https://github.com/user-attachments/assets/f9b8301b-0cf5-4681-a24b-149f6a8f75c5" />


## 💡 Desafíos abordados

Durante el desarrollo trabajé sobre situaciones comunes en proyectos reales:

- 🧩 Diseño de una estructura modular.
- ⚠️ Manejo de errores y excepciones.
- 🔒 Validación de datos ingresados por el usuario.
- 🗄️ Persistencia de información mediante SQLite.
- 🌿 Uso de Git para control de versiones.
- 📖 Documentación técnica del proyecto.
- 

## 🔮 Próximas mejoras

- ✏️ Edición de productos.
- 📊 Reportes y estadísticas.
- 📄 Exportación a CSV y Excel.
- 📦 Gestión de stock.
- 🖼️ Interfaz gráfica con Tkinter.
- 🧪 Implementación de pruebas automatizadas.
