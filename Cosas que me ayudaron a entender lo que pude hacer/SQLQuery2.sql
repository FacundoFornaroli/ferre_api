

-- Crear la base de datos si no existe
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'ferreteria_db')
BEGIN
    CREATE DATABASE ferreteria_db;
END
GO

USE ferreteria_db;
GO

-- 1. Crear tabla Categorias
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Categorias')
BEGIN
    CREATE TABLE Categorias (
        ID_Categoria INT IDENTITY(1,1) PRIMARY KEY,
        Nombre VARCHAR(100) NOT NULL UNIQUE
    );
END
GO

-- 2. Crear tabla Unidades_de_medida
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Unidades_de_medida')
BEGIN
    CREATE TABLE Unidades_de_medida (
        ID_Unidad_de_medida INT IDENTITY(1,1) PRIMARY KEY,
        Nombre VARCHAR(50) NOT NULL UNIQUE
    );
END
GO

-- 3. Crear tabla Sucursales
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Sucursales')
BEGIN
    CREATE TABLE Sucursales (
        ID_Sucursal INT IDENTITY(1,1) PRIMARY KEY,
        Nombre VARCHAR(100) NOT NULL UNIQUE
    );
END
GO

-- 4. Crear tabla Usuarios
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Usuarios')
BEGIN
    CREATE TABLE Usuarios (
        ID_Usuario INT IDENTITY(1,1) PRIMARY KEY,
        Nombre VARCHAR(100) NOT NULL UNIQUE,
        Rol VARCHAR(50) NOT NULL UNIQUE,
        Email VARCHAR(120) NOT NULL UNIQUE,
        Contraseña VARCHAR(255) NOT NULL UNIQUE,
        Estado BIT NOT NULL DEFAULT 1,
        Creado_el DATETIME NOT NULL DEFAULT GETDATE(),
        Actualizado_el DATETIME NOT NULL DEFAULT GETDATE()
    );
END
GO

-- 5. Crear tabla Productos
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Productos')
BEGIN
    CREATE TABLE Productos (
        ID_Producto INT IDENTITY(1,1) PRIMARY KEY,
        Nombre VARCHAR(150) NOT NULL UNIQUE,
        Descripcion TEXT NOT NULL,
        Precio FLOAT NOT NULL,
        Costo FLOAT NOT NULL,
        ID_Categoria INT NOT NULL,
        ID_Unidad_de_medida INT NOT NULL,
        CONSTRAINT FK_Productos_Categoria FOREIGN KEY (ID_Categoria) REFERENCES Categorias(ID_Categoria),
        CONSTRAINT FK_Productos_Unidad FOREIGN KEY (ID_Unidad_de_medida) REFERENCES Unidades_de_medida(ID_Unidad_de_medida),
        CONSTRAINT CK_Productos_Precio CHECK (Precio > 0),
        CONSTRAINT CK_Productos_Costo CHECK (Costo > 0)
    );
END
GO

-- 6. Crear tabla Clientes
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Clientes')
BEGIN
    CREATE TABLE Clientes (
        ID_Cliente INT IDENTITY(1,1) PRIMARY KEY,
        Nombre VARCHAR(150) NOT NULL UNIQUE,
        Direccion VARCHAR(200) NOT NULL,
        Telefono VARCHAR(40) NOT NULL,
        Email VARCHAR(120) NOT NULL,
        Fecha_Alta DATETIME NOT NULL DEFAULT GETDATE(),
        Limite_Credito FLOAT NOT NULL DEFAULT 0
    );
END
GO

-- 7. Crear tabla Proveedores
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Proveedores')
BEGIN
    CREATE TABLE Proveedores (
        ID_Proveedor INT IDENTITY(1,1) PRIMARY KEY,
        Nombre VARCHAR(150) NOT NULL,
        Direccion VARCHAR(200) NOT NULL,
        Telefono VARCHAR(40) NOT NULL,
        Email VARCHAR(120) NOT NULL
    );
END
GO

-- 8. Crear tabla Inventario
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Inventario')
BEGIN
    CREATE TABLE Inventario (
        ID_Inventario INT IDENTITY(1,1) PRIMARY KEY,
        ID_Producto INT NOT NULL,
        ID_Sucursal INT NOT NULL,
        Stock_Actual INT NOT NULL,
        Stock_Minimo INT NOT NULL,
        Stock_Maximo INT NOT NULL,
        CONSTRAINT FK_Inventario_Producto FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto),
        CONSTRAINT FK_Inventario_Sucursal FOREIGN KEY (ID_Sucursal) REFERENCES Sucursales(ID_Sucursal),
        CONSTRAINT CK_Inventario_Stock_Actual CHECK (Stock_Actual > 0),
        CONSTRAINT CK_Inventario_Stock_Minimo CHECK (Stock_Minimo > 0),
        CONSTRAINT CK_Inventario_Stock_Maximo CHECK (Stock_Maximo > 0)
    );
END
GO

-- 9. Crear tabla Facturas_Venta
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Facturas_Venta')
BEGIN
    CREATE TABLE Facturas_Venta (
        ID_Factura_Venta INT IDENTITY(1,1) PRIMARY KEY,
        ID_Cliente INT NOT NULL,
        Fecha DATETIME NOT NULL DEFAULT GETDATE(),
        Total FLOAT NOT NULL,
        ID_Usuario INT NOT NULL,
        Estado VARCHAR(30) NOT NULL DEFAULT 'Emitida',
        CONSTRAINT FK_FacturasVenta_Cliente FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
        CONSTRAINT FK_FacturasVenta_Usuario FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario),
        CONSTRAINT CK_FacturasVenta_Total CHECK (Total > 0)
    );
END
GO

-- 10. Crear tabla Detalles_Factura_Venta
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Detalles_Factura_Venta')
BEGIN
    CREATE TABLE Detalles_Factura_Venta (
        ID_Detalle INT IDENTITY(1,1) PRIMARY KEY,
        ID_Factura_Venta INT NOT NULL,
        ID_Producto INT NOT NULL,
        Cantidad INT NOT NULL,
        Precio_Unitario FLOAT NOT NULL,
        CONSTRAINT FK_DetallesFactura_Factura FOREIGN KEY (ID_Factura_Venta) REFERENCES Facturas_Venta(ID_Factura_Venta) ON DELETE CASCADE,
        CONSTRAINT FK_DetallesFactura_Producto FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto),
        CONSTRAINT CK_DetallesFactura_Cantidad CHECK (Cantidad > 0),
        CONSTRAINT CK_DetallesFactura_Precio CHECK (Precio_Unitario > 0)
    );
END
GO

-- 11. Crear tabla Pagos
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Pagos')
BEGIN
    CREATE TABLE Pagos (
        ID_Pago INT IDENTITY(1,1) PRIMARY KEY,
        ID_Factura_Venta INT NOT NULL,
        Metodo VARCHAR(30) NOT NULL,
        Monto FLOAT NOT NULL,
        Fecha DATETIME NOT NULL DEFAULT GETDATE(),
        CONSTRAINT FK_Pagos_Factura FOREIGN KEY (ID_Factura_Venta) REFERENCES Facturas_Venta(ID_Factura_Venta),
        CONSTRAINT CK_Pagos_Monto CHECK (Monto > 0)
    );
END
GO

-- 12. Crear tabla Ordenes_Compra
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Ordenes_Compra')
BEGIN
    CREATE TABLE Ordenes_Compra (
        ID_OC INT IDENTITY(1,1) PRIMARY KEY,
        ID_Proveedor INT NOT NULL,
        Fecha DATETIME NOT NULL DEFAULT GETDATE(),
        Total FLOAT NOT NULL,
        ID_Usuario INT NOT NULL,
        CONSTRAINT FK_OrdenesCompra_Proveedor FOREIGN KEY (ID_Proveedor) REFERENCES Proveedores(ID_Proveedor),
        CONSTRAINT FK_OrdenesCompra_Usuario FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario),
        CONSTRAINT CK_OrdenesCompra_Total CHECK (Total > 0)
    );
END
GO

-- 13. Crear tabla Detalle_OC
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Detalle_OC')
BEGIN
    CREATE TABLE Detalle_OC (
        ID_Detalle_OC INT IDENTITY(1,1) PRIMARY KEY,
        ID_OC INT NOT NULL,
        ID_Producto INT NOT NULL,
        Cantidad INT NOT NULL,
        Costo_Unitario FLOAT NOT NULL,
        CONSTRAINT FK_DetalleOC_Orden FOREIGN KEY (ID_OC) REFERENCES Ordenes_Compra(ID_OC) ON DELETE CASCADE,
        CONSTRAINT FK_DetalleOC_Producto FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto),
        CONSTRAINT CK_DetalleOC_Cantidad CHECK (Cantidad > 0),
        CONSTRAINT CK_DetalleOC_Costo CHECK (Costo_Unitario > 0)
    );
END
GO

-- 14. Crear tabla Movimientos_Inventario
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Movimientos_Inventario')
BEGIN
    CREATE TABLE Movimientos_Inventario (
        ID_Movimiento INT IDENTITY(1,1) PRIMARY KEY,
        ID_Producto INT NOT NULL,
        ID_Sucursal INT NOT NULL,
        Fecha DATETIME NOT NULL DEFAULT GETDATE(),
        Tipo VARCHAR(15) NOT NULL,
        Cantidad INT NOT NULL,
        Costo_Unitario FLOAT NULL,
        ID_Usuario INT NOT NULL,
        CONSTRAINT FK_MovimientosInventario_Producto FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto),
        CONSTRAINT FK_MovimientosInventario_Sucursal FOREIGN KEY (ID_Sucursal) REFERENCES Sucursales(ID_Sucursal),
        CONSTRAINT FK_MovimientosInventario_Usuario FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario),
        CONSTRAINT CK_MovimientosInventario_Tipo CHECK (Tipo IN ('Compra', 'Venta', 'Transferencia', 'Ajuste'))
    );
END
GO

-- índices para mejorar el rendimiento
-- Índices en Productos
CREATE INDEX IX_Productos_Categoria ON Productos(ID_Categoria);
CREATE INDEX IX_Productos_Unidad ON Productos(ID_Unidad_de_medida);

-- Índices en Inventario
CREATE INDEX IX_Inventario_Producto ON Inventario(ID_Producto);
CREATE INDEX IX_Inventario_Sucursal ON Inventario(ID_Sucursal);

-- Índices en Facturas_Venta
CREATE INDEX IX_FacturasVenta_Cliente ON Facturas_Venta(ID_Cliente);
CREATE INDEX IX_FacturasVenta_Usuario ON Facturas_Venta(ID_Usuario);
CREATE INDEX IX_FacturasVenta_Fecha ON Facturas_Venta(Fecha);

-- Índices en Detalles_Factura_Venta
CREATE INDEX IX_DetallesFactura_Factura ON Detalles_Factura_Venta(ID_Factura_Venta);
CREATE INDEX IX_DetallesFactura_Producto ON Detalles_Factura_Venta(ID_Producto);

-- Índices en Pagos
CREATE INDEX IX_Pagos_Factura ON Pagos(ID_Factura_Venta);
CREATE INDEX IX_Pagos_Fecha ON Pagos(Fecha);

-- Índices en Ordenes_Compra
CREATE INDEX IX_OrdenesCompra_Proveedor ON Ordenes_Compra(ID_Proveedor);
CREATE INDEX IX_OrdenesCompra_Usuario ON Ordenes_Compra(ID_Usuario);
CREATE INDEX IX_OrdenesCompra_Fecha ON Ordenes_Compra(Fecha);

-- Índices en Detalle_OC
CREATE INDEX IX_DetalleOC_Orden ON Detalle_OC(ID_OC);
CREATE INDEX IX_DetalleOC_Producto ON Detalle_OC(ID_Producto);

-- Índices en Movimientos_Inventario
CREATE INDEX IX_MovimientosInventario_Producto ON Movimientos_Inventario(ID_Producto);
CREATE INDEX IX_MovimientosInventario_Sucursal ON Movimientos_Inventario(ID_Sucursal);
CREATE INDEX IX_MovimientosInventario_Fecha ON Movimientos_Inventario(Fecha);
CREATE INDEX IX_MovimientosInventario_Usuario ON Movimientos_Inventario(ID_Usuario);
GO 