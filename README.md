# 📇 Agenda de Contactos - Kivy

Aplicación de gestión de contactos desarrollada con Kivy y SQLite.

## 🚀 Características

- ✅ Crear contactos con ID, nombre y teléfono
- 📋 Listar todos los contactos con imagen de perfil
- ✏️ Actualizar información de contactos existentes
- 🗑️ Eliminar contactos
- 🖼️ Imagen de perfil por defecto para todos los contactos
- 🎨 Interfaz gráfica moderna con tema gris oscuro

## 📋 Requisitos Previos

- Python 3.7 o superior instalado en tu sistema
- pip (gestor de paquetes de Python)
- Git

## 🔧 Instalación Paso a Paso

### 1. Clonar el repositorio

Abre tu terminal o línea de comandos y ejecuta:

```bash
git clone https://github.com/VoctorX/Parcial3.git
cd agenda-contactos
```

### 2. Crear el entorno virtual

**En Windows:**
```bash
python -m venv venv
```

**En macOS/Linux:**
```bash
python3 -m venv venv
```

### 3. Activar el entorno virtual

**En Windows:**
```bash
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
source venv/bin/activate
```

> 💡 Cuando el entorno virtual esté activado, verás `(venv)` al inicio de tu línea de comandos.

### 4. Instalar las dependencias

Con el entorno virtual activado, ejecuta:

```bash
pip install -r requirements.txt
```

### 5. Verificar la imagen por defecto

Asegúrate de tener la imagen `contactimg.png` en el directorio raíz del proyecto. Si no la tienes, coloca cualquier imagen PNG con ese nombre.

## ▶️ Ejecutar la Aplicación

Con el entorno virtual activado, ejecuta:

```bash
python main.py
```

## 🎮 Cómo usar la aplicación

1. **Crear contacto**: 
   - Ingresa ID (número único)
   - Ingresa Nombre
   - Ingresa Teléfono
   - Presiona el botón "Crear"

2. **Listar contactos**: 
   - Presiona "Listar" para actualizar y ver todos los contactos

3. **Ver detalles de un contacto**: 
   - Haz clic en cualquier contacto de la lista para ver sus detalles completos en un popup

4. **Actualizar contacto**: 
   - Ingresa el ID del contacto que deseas actualizar
   - Ingresa los nuevos datos (nombre y/o teléfono)
   - Presiona "Actualizar"

5. **Eliminar contacto**: 
   - Ingresa el ID del contacto que deseas eliminar
   - Presiona "Eliminar"

## 📂 Estructura del Proyecto

```
agenda-contactos/
│
├── main.py                 # Archivo principal de la aplicación
├── contactimg.png          # Imagen por defecto de contactos
├── database.db            # Base de datos SQLite (se crea automáticamente)
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
│
├── crud/
│   ├── __init__.py
│   ├── database.py       # Configuración de la base de datos
│   └── operations.py     # Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
│
└── models/
    └── __init__.py
```

## 🗄️ Base de Datos

La aplicación utiliza SQLite con la siguiente estructura:

**Tabla: contactos**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | INTEGER PRIMARY KEY AUTOINCREMENT | Identificador único |
| `name` | TEXT NOT NULL | Nombre del contacto |
| `phone` | TEXT NOT NULL | Teléfono del contacto |
| `image_path` | TEXT | Ruta de la imagen del contacto |

## 🛑 Desactivar el Entorno Virtual

Cuando termines de usar la aplicación, puedes desactivar el entorno virtual con:

```bash
deactivate
```

## 🎨 Personalización

Para cambiar la imagen por defecto de los contactos:
1. Reemplaza el archivo `contactimg.png` en el directorio raíz
2. Asegúrate de que la imagen tenga formato PNG

## 🐛 Solución de Problemas

### La imagen no se muestra
- Verifica que el archivo `contactimg.png` esté en el mismo directorio que `main.py`
- Asegúrate de que el archivo tenga permisos de lectura

### Error al crear contacto con ID duplicado
- Cada contacto debe tener un ID único
- Usa un número diferente para cada nuevo contacto

### Error "ModuleNotFoundError: No module named 'kivy'"
- Asegúrate de que el entorno virtual esté activado
- Ejecuta nuevamente: `pip install -r requirements.txt`

### La aplicación no inicia
- Verifica que tienes Python 3.7 o superior: `python --version`
- Asegúrate de haber activado el entorno virtual

## 📝 Notas Importantes

- Todos los campos (ID, Nombre, Teléfono) son obligatorios al crear un contacto
- El ID debe ser un número único para cada contacto
- La base de datos `database.db` se crea automáticamente la primera vez que ejecutas la aplicación
- Los contactos se guardan localmente en tu computadora

## 🔄 Actualizar el Proyecto

Para obtener las últimas actualizaciones del repositorio:

```bash
git pull origin main
pip install -r requirements.txt
```

## 👨‍💻 Desarrollo

Si quieres contribuir o modificar el proyecto:

1. Crea una rama nueva: `git checkout -b mi-nueva-funcionalidad`
2. Realiza tus cambios
3. Commit: `git commit -am 'Agrego nueva funcionalidad'`
4. Push: `git push origin mi-nueva-funcionalidad`
5. Crea un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Autor ✒️

* **Victor Cordoba** - *Creador y desarrollador principal* - [VoctorX](https://github.com/VoctorX)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir qué te gustaría cambiar.

---

Desarrollado con ❤️ usando Kivy y SQLite
