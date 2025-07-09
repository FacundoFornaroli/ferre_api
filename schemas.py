from pydantic import BaseModel, EmailStr # BASE MODEL ES UNA CLASE QUE SE USA PARA DEFINIR LOS SCHEMAS DE EN ESTE CASO MODELS.PY Y EMAILSTR ES UNA CLASE QUE SE USA PARA DEFINIR LOS EMAILS
from typing import Optional, List # OPTIONAL ES UNA CLASE QUE SE USA PARA DEFINIR LOS OPCIONALES Y LIST ES UNA CLASE QUE SE USA PARA DEFINIR LAS LISTAS
from datetime import datetime 
from pydantic import validator


# ====== ESQUEMAS PARA LA TABLA CATEGORIAS ======

# ESQUEMA BASE DE CATEGORIAS
class CategoriaBase(BaseModel): # crea una 'plantilla' y es la base para los otros schemas
    Nombre: str # es el nombre de la categoria

# ESQUEMA CREATE DE CATEGORIAS
class CategoriaCreate(CategoriaBase): # se usa cuando quiera crear una nueva categoria (por ahora no, mas adelante la cambiare)
    pass

#ESQUEMA UPDATE DE CATEGORIAS
class CategoriaUpdate(BaseModel): # por si queremos actualizar pero como por ahora es la tabla de categoria es la unica que necesitaria actualizar
    Nombre: Optional[str] = None

# ESQUEMA RESPUESTA DE CATEGORIAS
class Categorias(CategoriaBase): # hereda los deatos de la base y 'class Config' es para que pueda convertir los datos a este schema automaticamente
    ID_Categoria: int

    class Config:
        from_attributes = True

# ESQUEMA BASE DE UNIDADES DE MEDIDAS
class UnidadMedidaBase(BaseModel):
    Nombre: str

# ESQUEMA CREATE DE UNIDADES DE MEDIDAS
class UnidadMedidaCreate(UnidadMedidaBase):
    pass

#ESQUEMA DE ACTUALIZACION DE UNIDADES DE MEDIDAS
class UnidadMedidaUpdate(BaseModel):
    Nombre: Optional[str] = None

# ESQUEMA RESPUESTA DE UNIDADES DE MEDIDAS
class UnidadesMedidas(UnidadMedidaBase):
    ID_Unidad_Medida: int

    class Config:
        from_attributes = True

# ESQUEMA BASE DE SUCURSALES
class SucursalesBase(BaseModel):
    Nombre: str

# ESQUEMA CREATE DE SUCURSALES
class SucursalCreate(SucursalesBase):
    pass

# ESQUEMA DE ACTUALIZACION DE SUCURSALES
class SucursalUpdate(BaseModel):
    Nombre: Optional[str] = None

# ESQUEMA RESPUESTA DE SUCURSALES
class Sucursales(SucursalesBase):
    ID_Sucursal: int

    class Config:
        from_attributes = True

# ESQUEMA BASE DE USUARIOS
class UsuariosBase(BaseModel):
    Nombre: str
    Rol: str
    Email: str
    Contraseña: str
    Estado: bool = True

# ESQUEMA CREATE DE USUARIOS
class UsuariosCreate(UsuariosBase):
    @validator('Email')
    def validar_email(cls, v):
        if '@' not in v:
            raise ValueError('El email es incorrecto')
        return v


@validator('Contraseña')
def validar_contraseña(cls, v):
    if len(v) < 6:
        raise ValueError('La contraseña debe tener al menos 6 caracteres')
    return v

# ESQUEMA DE ACTUALIZACION DE USUARIOS
class UsuariosUpdate(BaseModel):
    Nombre: Optional[str] = None
    Rol: Optional[str] = None
    Email: Optional[str] = None
    Contraseña: Optional[str] = None
    Estado: Optional[bool] = None

# ESQUEMA RESPUESTA DE USUARIOS
class Usuarios(UsuariosBase):
    ID_Usuario: int
    Creado_el: datetime
    Actualizado_el: datetime
    
    class Config:
        from_attributes = True

# ESQUEMA BASE DE PRODUCTOS
class ProductosBase(BaseModel):
    Nombre: str
    Descripcion: str
    Precio: float
    Costo: float
    ID_Categoria: int
    ID_Unidad_Medida: int

# ESQUEMA CREATE DE PRODUCTOS
class ProductosCreate(ProductosBase):
    @validator('Precio')
    def validar_precio(cls, v):
        if v < 0:
            raise ValueError('El precio debe ser mayor o igual a 0')
        return v

    @validator('Costo')
    def validar_costo(cls, v):
        if v < 0:
            raise ValueError('El costo debe ser mayor o igual a 0')
        return v

# ESQUEMA DE ACTUALIZACION DE PRODUCTOS
class ProductosUpdate(BaseModel):
    Nombre: Optional[str] = None
    Descripcion: Optional[str] = None
    Precio: Optional[float] = None
    Costo: Optional[float] = None
    ID_Categoria: Optional[int] = None
    ID_Unidad_Medida: Optional[int] = None

# ESQUEMA RESPUESTA DE PRODUCTOS
class Productos(ProductosBase):
    ID_Productos: int

    class Config:
        from_attributes = True

# ESQUEMA BASE DE CLIENTES
class ClientesBase(BaseModel):
    Nombre: str
    Direccion: str
    Telefono: str
    Email: str
    Fecha_Alta: datetime
    Limite_Credito: float = 0

# ESQUEMA CREATE DE CLIENTES
class ClientesCreate(ClientesBase):
    pass

# ESQUEMA DE ACTUALIZACION DE CLIENTES
class ClientesUpdate(BaseModel):
    Nombre: Optional[str] = None
    Direccion: Optional[str] = None
    Telefono: Optional[str] = None
    Email: Optional[str] = None
    Fecha_Alta: Optional[datetime] = None
    Limite_Credito: Optional[float] = None

# ESQUEMA RESPUESTA DE CLIENTES
class Clientes(ClientesBase):
    ID_Cliente: int
    Fecha_Alta: datetime

    class Config:
        from_attributes = True

# ESQUEMA BASE DE PROVEEDORES
class ProveedoresBase(BaseModel):
    Nombre: str
    Direccion: str
    Telefono: str
    Email: str

# ESQUEMA CREATE DE PROVEEDORES
class ProveedoresCreate(ProveedoresBase):
    @validator('Email')
    def validar_email(cls, v):
        if '@' not in v:
            raise ValueError('El email es incorrecto')
        return v

# ESQUEMA DE ACTUALIZACION DE PROVEEDORES
class ProveedoresUpdate(BaseModel):
    Nombre: Optional[str] = None
    Direccion: Optional[str] = None
    Telefono: Optional[str] = None
    Email: Optional[str] = None

# ESQUEMA RESPUESTA DE PROVEEDORES
class Proveedores(ProveedoresBase):
    ID_Proveedor: int
    
    class Config:
        from_attributes = True

# ESQUEMA BASE DE INVENTARIO
class InventarioBase(BaseModel):
    ID_Producto: int
    ID_Sucursal: int
    Stock_Actual: int
    Stock_Minimo: int
    Stock_Maximo: int

# ESQUEMA CREATE DE INVENTARIO
class InventarioCreate(InventarioBase):
    @validator('Stock_Actual', 'Stock_Minimo', 'Stock_Maximo')
    def validar_stock(cls, v):
        if v < 0:
            raise ValueError('El stock debe ser mayor o igual a 0')
        return v

# ESQUEMA PARA ACTUALIZAR INVENTARIO
class InventarioUpdate(BaseModel):
    ID_Producto: Optional[int] = None
    ID_Sucursal: Optional[int] = None
    Stock_Actual: Optional[int] = None
    Stock_Minimo: Optional[int] = None
    Stock_Maximo: Optional[int] = None

# ESQUEMA RESPUESTA DE INVENTARIO
class Inventario(InventarioBase):
    """Esquema para mostrar inventario"""
    ID_Inventario: int
    
    class Config:
        from_attributes = True

# ESQUEMA BASE DE FACTURAS VENTAS
class FacturasVentasBase(BaseModel):
    ID_Cliente: int
    Total: float
    ID_Usuario: int
    Estado: str = "Emitida"
    """
    No incluimos fecha en el esquema base porque se genera automaticamente
    """

# ESQUEMA CREATE DE FACTURAS VENTAS
class FacturasVentasCreate(FacturasVentasBase):
    @validator('Total')
    def validar_total(cls, v):
        if v < 0:
            raise ValueError('El total debe ser mayor o igual a 0')
        return v

@validator('Estado')
def validar_estado(cls, v):
    estados_validados = ['Emitida', 'Cancelada', 'Pagada']
    if v not in estados_validados:
        raise ValueError(f'El estado debe ser uno de: {estados_validados}')
    return v

# ESQUEMA DE ACTUALIZACION DE FACTURAS VENTAS
class FacturasVentasUpdate(BaseModel):
    ID_Cliente: Optional[int] = None
    Total: Optional[float] = None
    ID_Usuario: Optional[int] = None
    Estado: Optional[str] = None

# ESQUEMA RESPUESTA DE FACTURAS VENTAS
class FacturasVentas(FacturasVentasBase):
    ID_Factura_Venta: int
    Fecha: datetime

    class Config:
        from_attributes = True

# ESQUEMA BASE DE DETALLES DE FACTURAS VENTAS
class DetallesFacturasVentasBase(BaseModel):
    ID_Factura_Venta: int
    ID_Producto: int
    Cantidad: int
    Precio_Unitario: float

# ESQUEMA CREATE DE DETALLES DE FACTURAS VENTAS
class DetallesFacturasVentaCreate(DetallesFacturasVentasBase):
    @validator('Cantidad')
    def validar_cantidad(cls, v):
        if v <= 0:
            raise ValueError('La cantidad debe ser mayor a 0')
        return v
    
    @validator('Precio_Unitario')
    def validar_precio_unitario(cls, v):
        if v <= 0:
            raise ValueError('El precio unitario debe ser mayor a 0')
        return v

# ESQUEMA DE ACTUALIZACION DE DETALLES DE FACTURAS VENTAS
class DetallesFacturaVentaUpdate(BaseModel):
    ID_Factura_Venta: Optional[int] = None
    ID_Producto: Optional[int] = None
    Cantidad: Optional[int] = None
    Precio_Unitario: Optional[float] = None

# ESQUEMA RESPUESTA DE DETALLES DE FACTURAS VENTAS
class DetallesFacturaVenta(DetallesFacturasVentasBase):
    ID_Detalle: int

    class Config:
        from_attributes = True


# ESQUEMA BASE DE PAGOS
class PagosBase(BaseModel):
    ID_Factura_Venta: int
    Metodo: str
    Monto: float

# ESQUEMA CREATE DE PAGOS
class PagosCreate(PagosBase):
    @validator('Monto')
    def validar_monto(cls, v):
        if v <= 0:
            raise ValueError('El monto debe ser mayor a 0')
        return v
    
    @validator('Metodo')
    def validar_metodo(cls, v):
        metodos_validos = ['Efectivo', 'Tarjeta', 'Transferencia', 'Cheque']
        if v not in metodos_validos:
            raise ValueError(f'El metodo debe ser uno de: {metodos_validos}')
        return v

# ESQUEMA DE ACTUALIZACION DE PAGOS
class PagosUpdate(BaseModel):
    ID_Factura_Venta: Optional[int] = None
    Metodo: Optional[str] = None
    Monto: Optional[float] = None

# ESQUEMA RESPUESTA DE PAGOS
class Pagos(PagosBase):
    ID_Pago: int
    Fecha: datetime

    class Config:
        from_attributes = True

# ESQUEMA BASE DE ORDENES DE COMPRA
class OrdenesCompraBase(BaseModel):
    ID_Proveedor: int
    Total: float
    ID_Usuario: int

# ESQUEMA CREATE DE ORDENES DE COMPRA
class OrdenesCompraCreate(OrdenesCompraBase):
    @validator('Total')
    def validar_total(cls, v):
        if v < 0:
            raise ValueError('El total debe ser mayor o igual a 0')
        return v

# ESQUEMA DE ACTUALIZACION DE ORDENES DE COMPRA
class OrdenesCompraUpdate(BaseModel):
    ID_Proveedor: Optional[int] = None
    Total: Optional[float] = None
    ID_Usuario: Optional[int] = None

# ESQUEMA RESPUESTA DE ORDENES DE COMPRA
class OrdenesCompra(OrdenesCompraBase):
    ID_OC: int
    Fecha: datetime
    
    class Config:
        from_attributes = True

# ESQUEMA BASE DE DETALLES DE ORDENES DE COMPRA
class DetalleOCBase(BaseModel):
    ID_OC: int
    ID_Producto: int
    Cantidad: int
    Costo_Unitario: float

# ESQUEMA CREATE DE DETALLES DE ORDENES DE COMPRA
class DetalleOCCreate(DetalleOCBase):
    @validator('Cantidad')
    def validar_cantidad(cls, v):
        if v <= 0:
            raise ValueError('La cantidad debe ser mayor a 0')
        return v
    
    @validator('Costo_Unitario')
    def validar_costo_unitario(cls, v):
        if v <= 0:
            raise ValueError('El costo unitario debe ser mayor a 0')
        return v

# ESQUEMA DE ACTUALIZACION DE DETALLES DE ORDENES DE COMPRA
class DetalleOCUpdate(BaseModel):
    ID_OC: Optional[int] = None
    ID_Producto: Optional[int] = None
    Cantidad: Optional[int] = None
    Costo_Unitario: Optional[float] = None

# ESQUEMA RESPUESTA DE DETALLES DE ORDENES DE COMPRA
class DetalleOC(DetalleOCBase):
    ID_Detalle_OC: int

    class Config:
        from_attributes = True

# ESQUEMA BASE DE MOVIMIENTOS DE INVENTARIO
class MovimientosInventarioBase(BaseModel):
    ID_Producto: int
    ID_Sucursal: int
    Tipo: str
    Cantidad: int
    Costo_Unitario: Optional[float] = None
    ID_Usuario: int

# ESQUEMA CREATE DE MOVIMIENTOS DE INVENTARIO
class MovimientosInventarioCreate(MovimientosInventarioBase):
    @validator('Tipo')
    def validar_tipo(cls, v):
        tipos_validos = ['Compra', 'Venta', 'Transferencia', 'Ajuste']
        if v not in tipos_validos:
            raise ValueError(f'El tipo debe ser uno de: {tipos_validos}')
        return v
    
    @validator('Cantidad')
    def validar_cantidad(cls, v):
        if v == 0:
            raise ValueError('La cantidad no puede ser 0')
        return v

# ESQUEMA DE ACTUALIZACION DE MOVIMIENTOS DE INVENTARIO
class MovimientosInventarioUpdate(BaseModel):
    ID_Producto: Optional[int] = None
    ID_Sucursal: Optional[int] = None
    Tipo: Optional[str] = None
    Cantidad: Optional[int] = None
    Costo_Unitario: Optional[float] = None
    ID_Usuario: Optional[int] = None

# ESQUEMA RESPUESTA DE MOVIMIENTOS DE INVENTARIO
class MovimientosInventario(MovimientosInventarioBase):
    ID_Movimiento: int
    Fecha: datetime

    class Config:
        from_attributes = True

