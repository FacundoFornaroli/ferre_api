from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


"""
Este va a ser la tabla de categorias y asi con todas las tablas que tenemos en nuestra base de datos
"""
class Categorias(Base):
    __tablename__ = "Categorias" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Categoria = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    Nombre = Column(String(100), nullable=False, unique=True) # en SQL SERVER esta columna es VARCHAR(100) y es unica osea not null


class Unidades_de_medida(Base):
    __tablename__ = "Unidades_de_medida" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Unidad_de_medida = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    Nombre = Column(String(50), nullable=False, unique=True) # en SQL SERVER esta columna es VARCHAR(50) y es unica osea not null


class Sucursales(Base):
    __tablename__ = "Sucursales" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Sucursal = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    Nombre = Column(String(100), nullable=False, unique=True) # en SQL SERVER esta columna es VARCHAR(100) y es unica osea not null


class Usuarios(Base):
    __tablename__ = "Usuarios" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Usuario = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    Nombre = Column(String(100),nullable=False, unique=True) # en SQL SERVER esta columna es VARCHAR(100) y es unica osea not null
    Rol = Column(String(50), nullable=False, unique=True) # en SQL SERVER esta columna es VARCHAR(50) y es unica osea not null
    Email = Column(String(120), nullable=False, unique=True) # en SQL SERVER esta columna es VARCHAR(120) y es unica osea not null
    Contraseña = Column(String(255), nullable=False, unique=True) # en SQL SERVER esta columna es VARCHAR(255) y es unica osea not null
    Estado = Column(Boolean, nullable=False, default=True) # en SQL SERVER esta columna es BIT y es unica osea not null
    Creado_el = Column(DateTime, nullable=False, default=func.now()) # en SQL SERVER esta columna es DATETIME y es unica osea not null
    Actualizado_el = Column(DateTime, nullable=False, default=func.now()) # en SQL SERVER esta columna es DATETIME y es unica osea not null


class Productos(Base):
    __tablename__ = "Productos" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Producto = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    Nombre = Column(String(150), nullable=False, unique=True) # en SQL SERVER esta columna es VARCHAR(150) y es unica osea not null
    Descripcion = Column(Text, nullable=False) # en SQL SERVER esta columna es TEXT y es unica osea not null
    Precio = Column(Float, nullable=False) # en SQL SERVER esta columna es FLOAT y es unica osea not null y tambien checkea que el precio sea mayor que 0
    Costo = Column(Float, nullable=False) # en SQL SERVER esta columna es FLOAT y es unica osea not null y tambien checkea que el costo sea mayor que 0
    ID_Categoria = Column(Integer, ForeignKey("Categorias.ID_Categoria"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Categorias y es unica osea not null
    ID_Unidad_de_medida = Column(Integer, ForeignKey("Unidades_de_medida.ID_Unidad_de_medida"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Unidades_de_medida y es unica osea not null

class Clientes(Base):
    __tablename__ = "Clientes" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Cliente = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    Nombre = Column(String(150), nullable=False, unique=True) # en SQL SERVER esta columna es VARCHAR(150) y es unica osea not null
    Direccion = Column(String(200), nullable=False)
    Telefono = Column(String(40), nullable=False)
    Email = Column(String(120), nullable=False) # en SQL SERVER esta columna es VARCHAR(120) y es unica osea not null
    Fecha_Alta = Column(DateTime, nullable=False, default=func.now()) # en SQL SERVER esta columna es DATETIME
    Limite_Credito = Column(Float, nullable=False, default=0)

class Proveedores(Base):
    __tablename__ = "Proveedores" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Proveedor = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    Nombre = Column(String(150), nullable=False) # en SQL SERVER esta columna es VARCHAR(150) y es unica osea not null
    Direccion = Column(String(200), nullable=False) # en SQL SERVER esta columna es VARCHAR(200) y es unica osea not null
    Telefono = Column(String(40), nullable=False) # en SQL SERVER esta columna es VARCHAR(40) y es unica osea not null
    Email = Column(String(120), nullable=False) # en SQL SERVER esta columna es VARCHAR(120) y es unica osea not null

class Inventario(Base):
    __tablename__ = "Inventario" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Inventario = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    ID_Producto = Column(Integer, ForeignKey("Productos.ID_Producto"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Productos y es unica osea not null
    ID_Sucursal = Column(Integer, ForeignKey("Sucursales.ID_Sucursal"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Sucursales y es unica osea not null
    Stock_Actual = Column(Integer, nullable=False) # en SQL SERVER esta columna es INT y es unica osea not null y tambien checkea que el stock actual sea mayor que 0
    Stock_Minimo = Column(Integer, nullable=False) # en SQL SERVER esta columna es INT y es unica osea not null y tambien checkea que el stock minimo sea mayor que 0
    Stock_Maximo = Column(Integer, nullable=False) # en SQL SERVER esta columna es INT y es unica osea not null y tambien checkea que el stock maximo sea mayor que 0

class Facturas_Venta(Base):
    __tablename__ = "Facturas_Venta" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Factura_Venta = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    ID_Cliente = Column(Integer, ForeignKey("Clientes.ID_Cliente"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Clientes y es unica osea not null
    Fecha = Column(DateTime, nullable=False, default=func.now()) # en SQL SERVER esta columna es DATETIME
    Total = Column(Float, nullable=False) # en SQL SERVER esta columna es FLOAT y es unica osea not null y tambien checkea que el total sea mayor que 0
    ID_Usuario = Column(Integer, ForeignKey("Usuarios.ID_Usuario"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Usuarios y es unica osea not null
    Estado = Column(String(30), nullable=False, default="Emitida") # en SQL SERVER esta columna es Varchar(30) y es unica osea not null y aparte siempre pone emitida si se crea una factura de venta

class Detalles_Factura_Venta(Base):
    __tablename__ = "Detalles_Factura_Venta" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Detalle = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    ID_Factura_Venta = Column(Integer, ForeignKey("Facturas_Venta.ID_Factura_Venta", ondelete="CASCADE"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Facturas_Venta y es unica osea not null y aparte si se elimina una factura de venta se eliminan los detalles de la factura de venta
    ID_Producto = Column(Integer, ForeignKey("Productos.ID_Producto"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Productos y es unica osea not null
    Cantidad = Column(Integer, nullable=False) # en SQL SERVER esta columna es INT y es unica osea not null y tambien checkea que la cantidad sea mayor que 0
    Precio_Unitario = Column(Float, nullable=False) # en SQL SERVER esta columna es FLOAT y es unica osea not null y tambien checkea que el precio unitario sea mayor que 0

class Pagos(Base):
    __tablename__ = "Pagos" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Pago = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    ID_Factura_Venta = Column(Integer, ForeignKey("Facturas_Venta.ID_Factura_Venta"), nullable=False,) # en SQL SERVER esta columna es INT y es una FK de Facturas_Venta y es unica osea not null y aparte si se elimina una factura de venta se eliminan los pagos de la factura de venta
    Metodo = Column(String(30), nullable=False)
    Monto = Column(Float, nullable=False) # en SQL SERVER esta columna es FLOAT y es unica osea not null y tambien checkea que el monto sea mayor que 0
    Fecha = Column(DateTime, nullable=False, default=func.now()) # en SQL SERVER esta columna es DATETIME

class Ordenes_Compra(Base):
    __tablename__ = "Ordenes_Compra" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_OC = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    ID_Proveedor = Column(Integer, ForeignKey("Proveedores.ID_Proveedor"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Proveedores y es unica osea not null
    Fecha = Column(DateTime, nullable=False, default=func.now()) # en SQL SERVER esta columna es DATETIME
    Total = Column(Float, nullable=False) # en SQL SERVER esta columna es FLOAT y es unica osea not null y tambien checkea que el total sea mayor que 0
    ID_Usuario = Column(Integer, ForeignKey("Usuarios.ID_Usuario"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Usuarios y es unica osea not null

class Detalle_OC(Base):
    __tablename__ = "Detalle_OC" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Detalle_OC = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    ID_OC = Column(Integer, ForeignKey("Ordenes_Compra.ID_OC", ondelete="CASCADE"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Ordenes_Compra y es unica osea not null y aparte si se elimina una orden de compra se eliminan los detalles de la orden de compra
    ID_Producto = Column(Integer, ForeignKey("Productos.ID_Producto"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Productos y es unica osea not null
    Cantidad = Column(Integer, nullable=False) # en SQL SERVER esta columna es INT y es unica osea not null y tambien checkea que la cantidad sea mayor que 0
    Costo_Unitario = Column(Float, nullable=False) # en SQL SERVER esta columna es FLOAT y es unica osea not null y tambien checkea que el costo unitario sea mayor que 0

class Movimientos_Inventario(Base):
    __tablename__ = "Movimientos_Inventario" # Este es el nombre exacto de la tabla en SQLSERVER de la base de datos
    ID_Movimiento = Column(Integer, primary_key=True, autoincrement=True) # IDENTIDAD (1,1) esto es una PK en mi Base de datos, que se autoincrementa
    ID_Producto = Column(Integer, ForeignKey("Productos.ID_Producto"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Productos y es unica osea not null
    ID_Sucursal = Column(Integer, ForeignKey("Sucursales.ID_Sucursal"), nullable=False) # en SQL SERVER esta columna es INT y es una FK de Sucursales y es unica osea not null
    Fecha = Column(DateTime, nullable=False, default=func.now()) # en SQL SERVER esta columna es DATETIME
    Tipo = Column(String(15), nullable=False) # en SQL SERVER esta columna es Varchar(15) y es unica osea not null y aparte checkea que el tipo sea compra o Venta o transferencia o ajuste
    Cantidad = Column(Integer, nullable=False)   
    Costo_Unitario = Column(Float, nullable=True)
    ID_Usuario = Column(Integer,ForeignKey("Usuarios.ID_Usuario"), nullable=False) 


# DIA 1/7 CHECKEAR QUE COINCIDA CON LA BASE DE DATOS QUE CREAMOS EN SQL SERVER

