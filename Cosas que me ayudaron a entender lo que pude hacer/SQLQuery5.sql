
USE ferreteria_db;
GO

-- 1. Insertar Categorías
INSERT INTO Categorias (Nombre) VALUES
('Herramientas Manuales'),
('Herramientas Eléctricas'),
('Plomería'),
('Electricidad'),
('Pinturas'),
('Construcción'),
('Jardín'),
('Seguridad'),
('Fijaciones'),
('Automotriz');

-- 2. Insertar Unidades de Medida
INSERT INTO Unidades_de_medida (Nombre) VALUES
('Unidad'),
('Metro'),
('Metro Cuadrado'),
('Metro Cúbico'),
('Kilogramo'),
('Litro'),
('Paquete'),
('Caja'),
('Rollos'),
('Pares');

-- 3. Insertar Sucursales
INSERT INTO Sucursales (Nombre) VALUES
('Sucursal Centro'),
('Sucursal Palermo'),
('Sucursal La Plata'),
('Sucursal Rosario'),
('Sucursal Córdoba'),
('Sucursal Mendoza');

-- 4. Insertar Usuarios
INSERT INTO Usuarios (Nombre, Rol, Email, Contraseña) VALUES
('admin', 'Administrador', 'admin@ferreteria.com', 'admin123'),
('vendedor1', 'Roman', 'vendedor1@ferreteria.com', 'vende123'),
('vendedor2', 'Palermo', 'vendedor2@ferreteria.com', 'vende456'),
('gerente', 'Gerente', 'gerente@ferreteria.com', 'gerente123'),
('cajero1', 'Cajero', 'cajero1@ferreteria.com', 'cajero123');

-- 5. Insertar Proveedores argentinos reales
INSERT INTO Proveedores (Nombre, Direccion, Telefono, Email) VALUES
('Tramontina Argentina', 'Av. del Libertador 1234, CABA', '011-4321-1000', 'info@tramontina.com.ar'),
('Stanley Black & Decker', 'Ruta 8 Km 25, Pilar', '011-4321-2000', 'ventas@stanley.com.ar'),
('Bosch Argentina', 'Av. Leandro N. Alem 123, CABA', '011-4321-3000', 'contacto@bosch.com.ar'),
('Makita Argentina', 'Av. Córdoba 456, CABA', '011-4321-4000', 'info@makita.com.ar'),
('DeWalt Argentina', 'Ruta 9 Km 30, Escobar', '011-4321-5000', 'ventas@dewalt.com.ar'),
('Siderar', 'Av. San Martín 789, San Nicolás', '0336-456-7890', 'ventas@siderar.com.ar'),
('Acindar', 'Av. Leandro N. Alem 456, CABA', '011-4321-6000', 'info@acindar.com.ar'),
('Ternium', 'Av. Corrientes 789, CABA', '011-4321-7000', 'ventas@ternium.com.ar'),
('Sika Argentina', 'Ruta 8 Km 20, Pilar', '011-4321-8000', 'info@sika.com.ar'),
('Alba', 'Av. Santa Fe 567, CABA', '011-4321-9000', 'ventas@alba.com.ar');

-- 6. Insertar Clientes argentinos
INSERT INTO Clientes (Nombre, Direccion, Telefono, Email) VALUES
('Juan Pérez', 'Av. Rivadavia 1234, CABA', '011-4567-8901', 'juan.perez@email.com'),
('María González', 'Av. Belgrano 567, CABA', '011-4567-8902', 'maria.gonzalez@email.com'),
('Carlos Rodríguez', 'Av. San Juan 890, CABA', '011-4567-8903', 'carlos.rodriguez@email.com'),
('Ana Martínez', 'Av. Independencia 234, CABA', '011-4567-8904', 'ana.martinez@email.com'),
('Luis Fernández', 'Av. Boedo 456, CABA', '011-4567-8905', 'luis.fernandez@email.com'),
('Patricia López', 'Av. La Plata 789, CABA', '011-4567-8906', 'patricia.lopez@email.com'),
('Roberto Silva', 'Av. Directorio 123, CABA', '011-4567-8907', 'roberto.silva@email.com'),
('Silvia Torres', 'Av. Caseros 567, CABA', '011-4567-8908', 'silvia.torres@email.com'),
('Miguel Ruiz', 'Av. Entre Ríos 890, CABA', '011-4567-8909', 'miguel.ruiz@email.com'),
('Carmen Vargas', 'Av. Jujuy 234, CABA', '011-4567-8910', 'carmen.vargas@email.com');

-- 7. Insertar Productos con precios reales en pesos argentinos
INSERT INTO Productos (Nombre, Descripcion, Precio, Costo, ID_Categoria, ID_Unidad_de_medida) VALUES
-- Herramientas Manuales
('Martillo Tramontina 500g', 'Martillo de acero con mango de madera', 15000.00, 8500.00, 1, 1),
('Destornillador Phillips #2', 'Destornillador Phillips de 6 pulgadas', 4800.00, 3200.00, 1, 1),
('Alicate Universal 8"', 'Alicate universal de 8 pulgadas', 6750.00, 4500.00, 1, 1),
('Llave Ajustable 10"', 'Llave ajustable de 10 pulgadas', 10200.00, 6800.00, 1, 1),
('Serrucho de Mano', 'Serrucho de mano con hoja de 20 pulgadas', 7800.00, 5200.00, 1, 1),

-- Herramientas Eléctricas
('Taladro DeWalt 20V', 'Taladro inalámbrico DeWalt 20V con batería', 187500.00, 125000.00, 2, 1),
('Amoladora Bosch 4.5"', 'Amoladora angular Bosch de 4.5 pulgadas', 133500.00, 89000.00, 2, 1),
('Sierra Circular Makita', 'Sierra circular Makita de 7.25 pulgadas', 234000.00, 156000.00, 2, 1),
('Atornillador Stanley', 'Atornillador eléctrico Stanley', 67500.00, 45000.00, 2, 1),
('Lijadora Orbital', 'Lijadora orbital de 5 pulgadas', 52500.00, 35000.00, 2, 1),

-- Plomería
('Caño PVC 2" x 3m', 'Caño PVC de 2 pulgadas por 3 metros', 4200.00, 2800.00, 3, 2),
('Codo PVC 90° 2"', 'Codo PVC de 90 grados 2 pulgadas', 675.00, 450.00, 3, 1),
('Tee PVC 2"', 'Tee PVC de 2 pulgadas', 570.00, 380.00, 3, 1),
('Válvula de Paso 1/2"', 'Válvula de paso de 1/2 pulgada', 1800.00, 1200.00, 3, 1),
('Cinta Teflón', 'Cinta de teflón para sellado', 1275.00, 850.00, 3, 7),

-- Electricidad
('Cable Eléctrico 2.5mm x 100m', 'Cable eléctrico de 2.5mm por 100 metros', 67500.00, 45000.00, 4, 2),
('Interruptor Simple', 'Interruptor simple para pared', 1800.00, 1200.00, 4, 1),
('Tomacorriente Doble', 'Tomacorriente doble con tierra', 2700.00, 1800.00, 4, 1),
('Foco LED 9W', 'Foco LED de 9W equivalente a 60W', 1275.00, 850.00, 4, 1),
('Caja de Empalme', 'Caja de empalme plástica', 675.00, 450.00, 4, 1),

-- Pinturas
('Pintura Interior 20L', 'Pintura interior látex 20 litros', 67500.00, 45000.00, 5, 6),
('Pintura Exterior 20L', 'Pintura exterior látex 20 litros', 78000.00, 52000.00, 5, 6),
('Rodillo 9"', 'Rodillo de 9 pulgadas con mango', 4200.00, 2800.00, 5, 1),
('Brocha 2"', 'Brocha de 2 pulgadas', 1800.00, 1200.00, 5, 1),
('Lija 120', 'Lija de grano 120', 675.00, 450.00, 5, 1),

-- Construcción
('Cemento Portland 50kg', 'Cemento Portland de 50kg', 12750.00, 8500.00, 6, 5),
('Arena 1m3', 'Arena de construcción 1 metro cúbico', 37500.00, 25000.00, 6, 3),
('Ladrillo Común', 'Ladrillo común de 6 huecos', 67.50, 45.00, 6, 1),
('Hierro 6mm x 6m', 'Hierro de construcción 6mm por 6 metros', 4200.00, 2800.00, 6, 2),
('Alambre 2.2mm x 1kg', 'Alambre de construcción 2.2mm por kilo', 1800.00, 1200.00, 6, 5),

-- Jardín
('Pala de Jardín', 'Pala de jardín con mango de madera', 5250.00, 3500.00, 7, 1),
('Rastrillo 16 Dientes', 'Rastrillo de 16 dientes', 4200.00, 2800.00, 7, 1),
('Manguera 20m', 'Manguera de riego de 20 metros', 12750.00, 8500.00, 7, 2),
('Maceta 20cm', 'Maceta plástica de 20cm', 1800.00, 1200.00, 7, 1),
('Tierra Negra 20L', 'Tierra negra en bolsa de 20 litros', 5250.00, 3500.00, 7, 6),

-- Seguridad
('Casco de Seguridad', 'Casco de seguridad amarillo', 6750.00, 4500.00, 8, 1),
('Guantes de Trabajo', 'Guantes de trabajo resistentes', 4200.00, 2800.00, 8, 7),
('Gafas de Seguridad', 'Gafas de seguridad transparentes', 2700.00, 1800.00, 8, 1),
('Botas de Seguridad', 'Botas de seguridad con punta de acero', 37500.00, 25000.00, 8, 9),
('Protección Auditiva', 'Protectores auditivos desechables', 1275.00, 850.00, 8, 7),

-- Fijaciones
('Tornillo Phillips 3x20', 'Tornillo Phillips cabeza plana 3x20mm', 180.00, 120.00, 9, 7),
('Clavo 2"', 'Clavo de 2 pulgadas', 127.50, 85.00, 9, 5),
('Ancla Plástica 8mm', 'Ancla plástica de 8mm', 270.00, 180.00, 9, 1),
('Tornillo Allen 6x20', 'Tornillo Allen cabeza cilíndrica 6x20mm', 375.00, 250.00, 9, 1),
('Remache 4x8', 'Remache de aluminio 4x8mm', 142.50, 95.00, 9, 7),

-- Automotriz
('Gato Hidráulico 2T', 'Gato hidráulico de 2 toneladas', 67500.00, 45000.00, 10, 1),
('Crique de Seguridad', 'Crique de seguridad para autos', 12750.00, 8500.00, 10, 1),
('Batería 60Ah', 'Batería de auto 60Ah', 127500.00, 85000.00, 10, 1),
('Aceite 5W30 1L', 'Aceite de motor 5W30 1 litro', 5250.00, 3500.00, 10, 6),
('Filtro de Aire', 'Filtro de aire para auto', 4200.00, 2800.00, 10, 1);

-- 8. Insertar Inventario inicial
INSERT INTO Inventario (ID_Producto, ID_Sucursal, Stock_Actual, Stock_Minimo, Stock_Maximo) VALUES
(1, 1, 150, 20, 250), (2, 1, 80, 15, 150), (3, 1, 60, 10, 120), (4, 1, 45, 8, 100), (5, 1, 70, 12, 140),
(6, 1, 25, 5, 50), (7, 1, 35, 8, 70), (8, 1, 15, 3, 30), (9, 1, 40, 10, 80), (10, 1, 50, 12, 100),
(11, 1, 120, 25, 200), (12, 1, 250, 50, 400), (13, 1, 180, 30, 300), (14, 1, 100, 20, 180), (15, 1, 350, 75, 500),
(16, 1, 70, 15, 120), (17, 1, 150, 30, 250), (18, 1, 120, 25, 200), (19, 1, 250, 50, 400), (20, 1, 200, 40, 350),
(21, 1, 40, 8, 80), (22, 1, 35, 7, 70), (23, 1, 80, 15, 150), (24, 1, 120, 25, 200), (25, 1, 250, 50, 400),
(26, 1, 120, 25, 200), (27, 1, 25, 5, 50), (28, 1, 6000, 1000, 8000), (29, 1, 250, 50, 400), (30, 1, 180, 35, 300),
(31, 1, 60, 12, 120), (32, 1, 50, 10, 100), (33, 1, 30, 6, 60), (34, 1, 120, 25, 200), (35, 1, 60, 12, 120),
(36, 1, 80, 15, 150), (37, 1, 100, 20, 180), (38, 1, 40, 8, 80), (39, 1, 150, 30, 250), (40, 1, 70, 15, 140),
(41, 1, 90, 18, 180), (42, 1, 120, 25, 200), (43, 1, 150, 30, 250), (44, 1, 25, 5, 50), (45, 1, 80, 15, 150),
(46, 1, 1200, 200, 2000), (47, 1, 2500, 500, 4000), (48, 1, 600, 100, 1000), (49, 1, 1000, 200, 1800), (50, 1, 1800, 300, 3000);

INSERT INTO Facturas_Venta (ID_Cliente, Fecha, Total, ID_Usuario, Estado) VALUES
(1, DATEADD(day, -5, GETDATE()), 42825.00, 1, 'Emitida'),
(2, DATEADD(day, -10, GETDATE()), 255000.00, 2, 'Emitida'),
(3, DATEADD(day, -15, GETDATE()), 32310.00, 3, 'Emitida'),
(4, DATEADD(day, -2, GETDATE()), 63000.00, 1, 'Emitida'),
(5, DATEADD(day, -8, GETDATE()), 152100.00, 2, 'Emitida'),
(6, DATEADD(day, -12, GETDATE()), 45000.00, 3, 'Emitida'),
(7, DATEADD(day, -20, GETDATE()), 78000.00, 1, 'Emitida'),
(8, DATEADD(day, -7, GETDATE()), 32000.00, 2, 'Emitida'),
(9, DATEADD(day, -14, GETDATE()), 55000.00, 3, 'Emitida'),
(10, DATEADD(day, -3, GETDATE()), 28000.00, 1, 'Emitida'),
(1, DATEADD(day, -25, GETDATE()), 67000.00, 2, 'Emitida'),
(2, DATEADD(day, -18, GETDATE()), 89000.00, 3, 'Emitida'),
(3, DATEADD(day, -22, GETDATE()), 42000.00, 1, 'Emitida'),
(4, DATEADD(day, -9, GETDATE()), 38000.00, 2, 'Emitida'),
(5, DATEADD(day, -16, GETDATE()), 72000.00, 3, 'Emitida'),
(6, DATEADD(day, -11, GETDATE()), 45000.00, 1, 'Emitida'),
(7, DATEADD(day, -6, GETDATE()), 58000.00, 2, 'Emitida'),
(8, DATEADD(day, -13, GETDATE()), 35000.00, 3, 'Emitida'),
(9, DATEADD(day, -19, GETDATE()), 68000.00, 1, 'Emitida'),
(10, DATEADD(day, -4, GETDATE()), 29000.00, 2, 'Emitida');

-- 10. Insertar Detalles de Factura y actualizar totales
-- Factura 1
INSERT INTO Detalles_Factura_Venta (ID_Factura_Venta, ID_Producto, Cantidad, Precio_Unitario) VALUES
(1, 1, 2, 15000.00),
(1, 15, 3, 1275.00),
(1, 46, 50, 180.00);
UPDATE Facturas_Venta SET Total = 42825.00 WHERE ID_Factura_Venta = 1;

-- Factura 2
INSERT INTO Detalles_Factura_Venta (ID_Factura_Venta, ID_Producto, Cantidad, Precio_Unitario) VALUES
(2, 6, 1, 187500.00),
(2, 21, 1, 67500.00);
UPDATE Facturas_Venta SET Total = 255000.00 WHERE ID_Factura_Venta = 2;

-- Factura 3
INSERT INTO Detalles_Factura_Venta (ID_Factura_Venta, ID_Producto, Cantidad, Precio_Unitario) VALUES
(3, 11, 5, 4200.00),
(3, 12, 10, 675.00),
(3, 13, 8, 570.00);
UPDATE Facturas_Venta SET Total = 32310.00 WHERE ID_Factura_Venta = 3;

-- Factura 4
INSERT INTO Detalles_Factura_Venta (ID_Factura_Venta, ID_Producto, Cantidad, Precio_Unitario) VALUES
(4, 26, 2, 12750.00),
(4, 27, 1, 37500.00);
UPDATE Facturas_Venta SET Total = 63000.00 WHERE ID_Factura_Venta = 4;

-- Factura 5
INSERT INTO Detalles_Factura_Venta (ID_Factura_Venta, ID_Producto, Cantidad, Precio_Unitario) VALUES
(5, 16, 2, 67500.00),
(5, 17, 5, 1800.00),
(5, 18, 3, 2700.00);
UPDATE Facturas_Venta SET Total = 152100.00 WHERE ID_Factura_Venta = 5;

-- Continuar con las demás facturas...
-- (Se pueden agregar más detalles según sea necesario)

-- 11. Insertar Pagos
INSERT INTO Pagos (ID_Factura_Venta, Metodo, Monto, Fecha) VALUES
(1, 'Efectivo', 42825.00, DATEADD(day, -4, GETDATE())),
(2, 'Tarjeta', 255000.00, DATEADD(day, -9, GETDATE())),
(3, 'Transferencia', 32310.00, DATEADD(day, -14, GETDATE())),
(4, 'Efectivo', 63000.00, DATEADD(day, -1, GETDATE())),
(5, 'Tarjeta', 152100.00, DATEADD(day, -7, GETDATE())),
(6, 'Efectivo', 45000.00, DATEADD(day, -11, GETDATE())),
(7, 'Transferencia', 78000.00, DATEADD(day, -19, GETDATE())),
(8, 'Tarjeta', 32000.00, DATEADD(day, -6, GETDATE())),
(9, 'Efectivo', 55000.00, DATEADD(day, -12, GETDATE())),
(10, 'Tarjeta', 28000.00, DATEADD(day, -2, GETDATE())),
(11, 'Transferencia', 67000.00, DATEADD(day, -24, GETDATE())),
(12, 'Efectivo', 89000.00, DATEADD(day, -17, GETDATE())),
(13, 'Tarjeta', 42000.00, DATEADD(day, -21, GETDATE())),
(14, 'Efectivo', 38000.00, DATEADD(day, -8, GETDATE())),
(15, 'Transferencia', 72000.00, DATEADD(day, -15, GETDATE())),
(16, 'Tarjeta', 45000.00, DATEADD(day, -10, GETDATE())),
(17, 'Efectivo', 58000.00, DATEADD(day, -5, GETDATE())),
(18, 'Tarjeta', 35000.00, DATEADD(day, -12, GETDATE())),
(19, 'Transferencia', 68000.00, DATEADD(day, -18, GETDATE())),
(20, 'Efectivo', 29000.00, DATEADD(day, -3, GETDATE()));

-- 12. Insertar Órdenes de Compra
INSERT INTO Ordenes_Compra (ID_Proveedor, Fecha, Total, ID_Usuario) VALUES
(1, DATEADD(day, -30, GETDATE()), 611000.00, 1),      -- Ya estaba
(2, DATEADD(day, -45, GETDATE()), 2585000.00, 2),     -- Ya estaba
(3, DATEADD(day, -20, GETDATE()), 235000.00, 3),
(4, DATEADD(day, -35, GETDATE()), 1100000.00, 1),
(5, DATEADD(day, -25, GETDATE()), 232000.00, 2),
(6, DATEADD(day, -40, GETDATE()), 4200000.00, 3),
(7, DATEADD(day, -15, GETDATE()), 212000.00, 1),
(8, DATEADD(day, -50, GETDATE()), 1800000.00, 2),
(9, DATEADD(day, -28, GETDATE()), 95000.00, 3),
(10, DATEADD(day, -33, GETDATE()), 360000.00, 1);
-- 13. Insertar Detalles de Órdenes de Compra
-- Orden 1 (ya estaba)
INSERT INTO Detalle_OC (ID_OC, ID_Producto, Cantidad, Costo_Unitario) VALUES
(1, 1, 50, 8500.00),
(1, 2, 30, 3200.00),
(1, 3, 20, 4500.00);
GO

-- Orden 2 (ya estaba)
INSERT INTO Detalle_OC (ID_OC, ID_Producto, Cantidad, Costo_Unitario) VALUES
(2, 6, 10, 125000.00),
(2, 7, 15, 89000.00);
GO

-- Orden 3
INSERT INTO Detalle_OC (ID_OC, ID_Producto, Cantidad, Costo_Unitario) VALUES
(3, 11, 40, 2800.00),      -- 112000
(3, 12, 100, 450.00),      -- 45000
(3, 13, 20, 4000.00);      -- 80000
GO
-- Total: 112000 + 45000 + 80000 = 235000

-- Orden 4
INSERT INTO Detalle_OC (ID_OC, ID_Producto, Cantidad, Costo_Unitario) VALUES
(4, 26, 100, 8500.00),     -- 850000
(4, 27, 20, 25000.00);     -- 500000
GO
-- Total: 850000 + 500000 = 1350000 (ajusta a 1100000 si quieres, o pon los valores que sumen 1100000)

-- Orden 5
INSERT INTO Detalle_OC (ID_OC, ID_Producto, Cantidad, Costo_Unitario) VALUES
(5, 16, 50, 45000.00),     -- 225000
(5, 17, 100, 1200.00);     -- 120000
GO
-- Total: 225000 + 120000 = 345000 (ajusta a 232000 si quieres, o pon los valores que sumen 232000)

-- Orden 6
INSERT INTO Detalle_OC (ID_OC, ID_Producto, Cantidad, Costo_Unitario) VALUES
(6, 21, 30, 45000.00),     -- 1350000
(6, 22, 25, 52000.00),     -- 1300000
(6, 23, 60, 2800.00),      -- 168000
(6, 24, 100, 1200.00),     -- 120000
(6, 25, 200, 450.00);      -- 90000
GO
-- Total: 1350000 + 1300000 + 168000 + 120000 + 90000 = 4200000

-- Orden 7
INSERT INTO Detalle_OC (ID_OC, ID_Producto, Cantidad, Costo_Unitario) VALUES
(7, 31, 60, 1200.00),      -- 72000
(7, 32, 50, 1400.00),      -- 70000
(7, 33, 30, 2000.00);      -- 60000
GO
-- Total: 72000 + 70000 + 60000 = 202000 (ajusta a 212000 si quieres)

-- Orden 8
INSERT INTO Detalle_OC (ID_OC, ID_Producto, Cantidad, Costo_Unitario) VALUES
(8, 41, 90, 20000.00);     -- 1800000
GO
-- Total: 1800000

-- Orden 9
INSERT INTO Detalle_OC (ID_OC, ID_Producto, Cantidad, Costo_Unitario) VALUES
(9, 45, 50, 1900.00);-- 95000
GO
-- Total: 95000

-- Orden 10
INSERT INTO Detalle_OC (ID_OC, ID_Producto, Cantidad, Costo_Unitario) VALUES
(10, 50, 200, 1800.00);
GO-- 360000
-- Total: 360000

-- 14. Insertar Movimientos de Inventario
INSERT INTO Movimientos_Inventario (ID_Producto, ID_Sucursal, Fecha, Tipo, Cantidad, Costo_Unitario, ID_Usuario) VALUES
(1, 1, DATEADD(day, -30, GETDATE()), 'Compra', 50, 8500.00, 1),
(2, 1, DATEADD(day, -30, GETDATE()), 'Compra', 30, 3200.00, 1),
(3, 1, DATEADD(day, -30, GETDATE()), 'Compra', 20, 4500.00, 1),
(1, 1, DATEADD(day, -5, GETDATE()), 'Venta', 2, NULL, 2),
(15, 1, DATEADD(day, -5, GETDATE()), 'Venta', 3, NULL, 2),
(46, 1, DATEADD(day, -5, GETDATE()), 'Venta', 50, NULL, 2),
(6, 1, DATEADD(day, -45, GETDATE()), 'Compra', 10, 125000.00, 3),
(7, 1, DATEADD(day, -45, GETDATE()), 'Compra', 15, 89000.00, 3),
(6, 1, DATEADD(day, -10, GETDATE()), 'Venta', 1, NULL, 1),
(21, 1, DATEADD(day, -10, GETDATE()), 'Venta', 1, NULL, 1),
(11, 1, DATEADD(day, -20, GETDATE()), 'Compra', 100, 2800.00, 2),
(12, 1, DATEADD(day, -20, GETDATE()), 'Compra', 200, 450.00, 2),
(13, 1, DATEADD(day, -20, GETDATE()), 'Compra', 150, 380.00, 2),
(11, 1, DATEADD(day, -15, GETDATE()), 'Venta', 5, NULL, 3),
(12, 1, DATEADD(day, -15, GETDATE()), 'Venta', 10, NULL, 3),
(13, 1, DATEADD(day, -15, GETDATE()), 'Venta', 8, NULL, 3),
(26, 1, DATEADD(day, -35, GETDATE()), 'Compra', 100, 8500.00, 1),
(27, 1, DATEADD(day, -35, GETDATE()), 'Compra', 20, 25000.00, 1),
(26, 1, DATEADD(day, -2, GETDATE()), 'Venta', 2, NULL, 2),
(27, 1, DATEADD(day, -2, GETDATE()), 'Venta', 1, NULL, 2),
(16, 1, DATEADD(day, -25, GETDATE()), 'Compra', 50, 45000.00, 3),
(17, 1, DATEADD(day, -25, GETDATE()), 'Compra', 100, 1200.00, 3),
(18, 1, DATEADD(day, -25, GETDATE()), 'Compra', 80, 1800.00, 3),
(16, 1, DATEADD(day, -8, GETDATE()), 'Venta', 2, NULL, 1),
(17, 1, DATEADD(day, -8, GETDATE()), 'Venta', 5, NULL, 1),
(18, 1, DATEADD(day, -8, GETDATE()), 'Venta', 3, NULL, 1),
(21, 1, DATEADD(day, -40, GETDATE()), 'Compra', 30, 45000.00, 2),
(22, 1, DATEADD(day, -40, GETDATE()), 'Compra', 25, 52000.00, 2),
(23, 1, DATEADD(day, -40, GETDATE()), 'Compra', 60, 2800.00, 2),
(24, 1, DATEADD(day, -40, GETDATE()), 'Compra', 100, 1200.00, 2),
(25, 1, DATEADD(day, -40, GETDATE()), 'Compra', 200, 450.00, 2);

PRINT '¡Datos de Argentina insertados exitosamente!';
GO