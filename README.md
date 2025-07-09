# 🛠️ API de Ferretería Fornaroli

## 📋 Descripción General

Esta es una **API REST** (Interfaz de Programación de Aplicaciones) desarrollada con **FastAPI** y **Python** para gestionar una ferretería. La API permite manejar productos, clientes, ventas, inventario, proveedores y mucho más.

### ¿Qué es una API?
Una API es como un "mesero" que conecta diferentes programas. En este caso, nuestra API permite que aplicaciones web, móviles o de escritorio puedan interactuar con la base de datos de la ferretería de manera segura y organizada.

## 🏗️ Estructura del Proyecto

```
ferre_api/
├── main.py              # 🚀 Archivo principal de la API
├── models.py            # 📊 Modelos de la base de datos
├── schemas.py           # 📝 Esquemas de validación
├── database.py          # 🔌 Configuración de la base de datos
├── requirements.txt     # 📦 Dependencias del proyecto
├── config_ejemplo.txt   # ⚙️ Ejemplo de configuración
├── prueba_coneccion.py  # 🧪 Script de prueba de conexión
└── README.md           # 📖 Este archivo
```

## 🗄️ Base de Datos

### SQL Server
La aplicación utiliza **Microsoft SQL Server** como base de datos. SQL Server es un sistema de gestión de bases de datos robusto y confiable.

### Tablas Principales

| Tabla | Descripción |
|-------|-------------|
| **Categorias** | Categorías de productos (ej: Herramientas, Pinturas) |
| **Productos** | Información de cada producto |
| **Clientes** | Datos de los clientes |
| **Proveedores** | Información de proveedores |
| **Inventario** | Stock de productos por sucursal |
| **Facturas_Venta** | Facturas de venta |
| **Ordenes_Compra** | Órdenes de compra a proveedores |
| **Usuarios** | Usuarios del sistema |
| **Sucursales** | Diferentes ubicaciones de la ferretería |

## 🚀 Cómo Empezar

### 1. Requisitos Previos

Antes de usar esta API, necesitas tener instalado:

- **Python 3.8 o superior**
- **SQL Server** (local o en la nube)
- **ODBC Driver para SQL Server**

### 2. Instalación

#### Paso 1: Clonar o descargar el proyecto
```bash
# Si usas Git:
git clone [URL_DEL_REPOSITORIO]
cd ferre_api

# O simplemente descarga los archivos en una carpeta
```

#### Paso 2: Instalar dependencias
```bash
pip install -r requirements.txt
```

#### Paso 3: Configurar la base de datos

1. **Crear el archivo `.env`** en la carpeta del proyecto
2. **Copiar el contenido** del archivo `config_ejemplo.txt`
3. **Modificar la cadena de conexión** según tu configuración:

```env
# Ejemplo para SQL Server local:
SQLSERVER_CONN=mssql+pyodbc://localhost/BASEDEDATOS?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes
```

#### Paso 4: Probar la conexión
```bash
python prueba_coneccion.py
```

Si todo está bien, verás mensajes de conexión exitosa.

#### Paso 5: Ejecutar la API
```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://localhost:8000`

## 📚 Funcionalidades Principales

### 🔧 Gestión de Productos
- ✅ Crear, leer, actualizar y eliminar productos
- ✅ Buscar productos por nombre
- ✅ Filtrar productos por categoría
- ✅ Gestionar precios y costos

### 👥 Gestión de Clientes
- ✅ Registrar nuevos clientes
- ✅ Actualizar información de clientes
- ✅ Buscar clientes por nombre o email
- ✅ Gestionar límites de crédito

### 📦 Gestión de Inventario
- ✅ Control de stock por sucursal
- ✅ Alertas de stock mínimo
- ✅ Movimientos de inventario (entradas/salidas)
- ✅ Transferencias entre sucursales

### 🛒 Ventas y Facturación
- ✅ Crear facturas de venta
- ✅ Gestionar detalles de facturas
- ✅ Control de pagos
- ✅ Estados de facturas

### 🏪 Gestión de Proveedores
- ✅ Registrar proveedores
- ✅ Crear órdenes de compra
- ✅ Gestionar detalles de compras

## 🌐 Endpoints de la API

### Categorías
- `GET /categorias/` - Obtener todas las categorías
- `POST /categorias/` - Crear nueva categoría
- `PUT /categorias/{id}` - Actualizar categoría
- `DELETE /categorias/{id}` - Eliminar categoría

### Productos
- `GET /productos/` - Obtener todos los productos
- `GET /productos/{id}` - Obtener producto específico
- `POST /productos/` - Crear nuevo producto
- `PUT /productos/{id}` - Actualizar producto
- `DELETE /productos/{id}` - Eliminar producto
- `GET /productos/buscar/{nombre}` - Buscar productos por nombre

### Clientes
- `GET /clientes/` - Obtener todos los clientes
- `POST /clientes/` - Crear nuevo cliente
- `PUT /clientes/{id}` - Actualizar cliente
- `DELETE /clientes/{id}` - Eliminar cliente
- `GET /clientes/buscar/{nombre}` - Buscar clientes por nombre

### Inventario
- `GET /inventario/` - Obtener todo el inventario
- `POST /inventario/` - Crear registro de inventario
- `PUT /inventario/{id}` - Actualizar inventario
- `GET /inventario/producto/{id}` - Inventario por producto

### Facturas de Venta
- `GET /facturas-venta/` - Obtener todas las facturas
- `POST /facturas-venta/` - Crear nueva factura
- `PUT /facturas-venta/{id}` - Actualizar factura
- `GET /facturas-venta/cliente/{id}` - Facturas por cliente

## 🔍 Documentación Automática

Una vez que ejecutes la API, puedes acceder a:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

Estas herramientas te permiten:
- Ver todos los endpoints disponibles
- Probar la API directamente desde el navegador
- Ver ejemplos de datos de entrada y salida
- Entender la estructura de cada endpoint

## 🛡️ Seguridad y Validación

### Validaciones Implementadas
- ✅ Emails válidos
- ✅ Contraseñas con mínimo 6 caracteres
- ✅ Precios y costos mayores a 0
- ✅ Cantidades positivas
- ✅ Estados válidos para facturas

### Manejo de Errores
- ✅ Códigos de error HTTP apropiados
- ✅ Mensajes de error descriptivos
- ✅ Validación de datos de entrada
- ✅ Manejo de registros no encontrados

## 🧪 Pruebas

### Script de Prueba de Conexión
El archivo `prueba_coneccion.py` te permite verificar:

1. **Conexión a la base de datos**
2. **Versión de SQL Server**
3. **Nombre de la base de datos actual**
4. **Tablas disponibles**
5. **Importación correcta de modelos**

Para ejecutar las pruebas:
```bash
python prueba_coneccion.py
```

## 🔧 Configuración Avanzada

### Variables de Entorno
El archivo `.env` puede contener:

```env
# Conexión a SQL Server
SQLSERVER_CONN=mssql+pyodbc://usuario:contraseña@servidor/base_datos?driver=ODBC+Driver+17+for+SQL+Server

# Configuración de la aplicación
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

### Diferentes Tipos de Conexión

1. **Autenticación de Windows**:
```env
SQLSERVER_CONN=mssql+pyodbc://localhost/ferreteria_db?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes
```

2. **SQL Server Express**:
```env
SQLSERVER_CONN=mssql+pyodbc://localhost\SQLEXPRESS/ferreteria_db?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes
```

3. **Con usuario y contraseña**:
```env
SQLSERVER_CONN=mssql+pyodbc://usuario:contraseña@localhost/ferreteria_db?driver=ODBC+Driver+17+for+SQL+Server
```

## 📦 Dependencias Principales

| Librería | Versión | Propósito |
|----------|---------|-----------|
| **FastAPI** | 0.115.14 | Framework web para crear la API |
| **SQLAlchemy** | 2.0.41 | ORM para trabajar con la base de datos |
| **Pydantic** | 2.11.7 | Validación de datos y serialización |
| **PyODBC** | 5.2.0 | Conector para SQL Server |
| **Uvicorn** | 0.35.0 | Servidor ASGI para ejecutar FastAPI |
| **Python-dotenv** | 1.1.1 | Manejo de variables de entorno |

## 🚨 Solución de Problemas Comunes

### Error de Conexión a la Base de Datos
**Problema**: No se puede conectar a SQL Server
**Solución**:
1. Verificar que SQL Server esté ejecutándose
2. Revisar la cadena de conexión en `.env`
3. Asegurar que el ODBC Driver esté instalado
4. Verificar que la base de datos exista

### Error de Importación de Módulos
**Problema**: No se pueden importar las librerías
**Solución**:
```bash
pip install -r requirements.txt
```

### Error de Permisos
**Problema**: No se puede acceder a la base de datos
**Solución**:
1. Verificar credenciales de usuario
2. Asegurar permisos en SQL Server
3. Usar autenticación de Windows si es posible

## 📈 Próximos Pasos

- 🔐 Implementar autenticación JWT
- 📊 Agregar reportes y estadísticas
- 🖼️ Subir imágenes de productos
- 📧 Notificaciones por email
- 📱 Crear aplicación móvil
- 🔄 Sincronización en tiempo real

### Funcionalidades que se van a agregar
- 🏷️ Gestión de descuentos
- 📋 Historial de precios
- 🚚 Gestión de envíos
- 💳 Integración con pasarelas de pago
- 📊 Dashboard administrativo

## 🤝 Contribución

Si quieres contribuir al proyecto:

1. **Fork** el repositorio
2. Crea una **rama** para tu funcionalidad
3. Realiza tus **cambios**
4. **Prueba** que todo funcione
5. Crea un **Pull Request**

## 📞 Soporte

Si tienes problemas o preguntas:

1. Revisa la **documentación** en `/docs`
2. Ejecuta el **script de pruebas**
3. Verifica la **configuración** de la base de datos
4. Consulta los **logs** de error

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo libremente para fines educativos y comerciales.

---

## 🎯 Resumen para Principiantes

### ¿Qué hace esta API?
Esta API es como un "cerebro digital" para una ferretería que:
- 📝 Guarda información de productos, clientes y ventas
- 🔍 Permite buscar y organizar datos
- 💰 Calcula precios y totales
- 📦 Controla el inventario
- 👥 Gestiona clientes y proveedores

### ¿Por qué usar FastAPI?
- ⚡ **Rápido**: Muy veloz para procesar peticiones
- 📚 **Fácil**: Sintaxis simple y clara
- 🔍 **Automático**: Genera documentación automáticamente
- 🛡️ **Seguro**: Validación automática de datos
- 🧪 **Probado**: Muy estable y confiable

### ¿Cómo funciona?
1. **Recibe peticiones** de aplicaciones web/móviles
2. **Valida los datos** que llegan
3. **Se conecta** a la base de datos SQL Server
4. **Procesa la información** (crear, leer, actualizar, eliminar)
5. **Devuelve respuestas** en formato JSON

¡Es como tener un asistente digital que maneja toda la información de tu ferretería de manera organizada y eficiente! 🛠️✨ 