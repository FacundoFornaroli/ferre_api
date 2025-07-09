from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas
from database import engine, get_db
from datetime import datetime
from pydantic import BaseModel, validator
from sqlalchemy import Column, Integer, String, Float, DateTime, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Crear las tablas en la base de datos
# Esto es como "construir" las tablas si no existen
# models.Base.metadata.create_all(bind=engine)  # COMENTADO:| Ya tienes las tablas en SQL Server

# Crear la aplicación FastAPI
app = FastAPI(
    title="API de Ferreteria Fornaroli",
    description="API para gestionar una ferretería con productos, clientes y ventas",
    version="1.0.0"
)

# ====== RUTAS PARA CATEGORIAS ======

@app.get("/categorias/", response_model=List[schemas.Categorias])
def obtener_categorias(db: Session = Depends(get_db)):
    """Obtener todas las categorías"""
    categorias = db.query(models.Categorias).all()
    return categorias

@app.get("/categorias/{categoria_id}", response_model=schemas.Categorias)
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    """Obtener una categoría específica por ID"""
    categoria = db.query(models.Categorias).filter(models.Categorias.ID_Categoria == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@app.post("/categorias/", response_model=schemas.Categorias)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    """Crear una nueva categoría"""
    db_categoria = models.Categorias(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@app.put("/categorias/{categoria_id}", response_model=schemas.Categorias)
def actualizar_categoria(categoria_id: int, categoria: schemas.CategoriaUpdate, db: Session = Depends(get_db)):
    """Actualizar una categoría existente"""
    db_categoria = db.query(models.Categorias).filter(models.Categorias.ID_Categoria == categoria_id).first()
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    # Actualizar solo los campos proporcionados
    for field, value in categoria.dict(exclude_unset=True).items():
        setattr(db_categoria, field, value)
    
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@app.delete("/categorias/{categoria_id}")
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    """Eliminar una categoría"""
    db_categoria = db.query(models.Categorias).filter(models.Categorias.ID_Categoria == categoria_id).first()
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    db.delete(db_categoria)
    db.commit()
    return {"message": "Categoría eliminada exitosamente"}


# ====== RUTAS PARA UNIDADES DE MEDIDA ======

@app.get("/unidades-medidas/", response_model=List[schemas.UnidadesMedidas])
def obtener_unidades_medidas(db: Session = Depends(get_db)):
    """Obtener todas las unidades de medida"""
    unidades = db.query(models.Unidades_de_medida).all()
    return unidades

@app.get("/unidades-medidas/{unidad_id}", response_model=schemas.UnidadesMedidas)
def obtener_unidad_medida(unidad_id: int, db: Session = Depends(get_db)):
    """Obtener una unidad de medida específica por ID"""
    unidad = db.query(models.Unidades_de_medida).filter(models.Unidades_de_medida.ID_Unidad_Medida == unidad_id).first()
    if not unidad:
        raise HTTPException(status_code=404, detail="Unidad de medida no encontrada")
    return unidad

@app.post("/unidades-medidas/", response_model=schemas.UnidadesMedidas)
def crear_unidad_medida(unidad: schemas.UnidadMedidaCreate, db: Session = Depends(get_db)):
    """Crear una nueva unidad de medida"""
    db_unidad = models.Unidades_de_medida(**unidad.dict())
    db.add(db_unidad)
    db.commit()
    db.refresh(db_unidad)
    return db_unidad

@app.put("/unidades-medidas/{unidad_id}", response_model=schemas.UnidadesMedidas)
def actualizar_unidad_medida(unidad_id: int, unidad: schemas.UnidadMedidaUpdate, db: Session = Depends(get_db)):
    """Actualizar una unidad de medida existente"""
    db_unidad = db.query(models.Unidades_de_medida).filter(models.Unidades_de_medida.ID_Unidad_Medida == unidad_id).first()
    if not db_unidad:
        raise HTTPException(status_code=404, detail="Unidad de medida no encontrada")
    
    # Actualizar solo los campos proporcionados
    for field, value in unidad.dict(exclude_unset=True).items():
        setattr(db_unidad, field, value)
    
    db.commit()
    db.refresh(db_unidad)
    return db_unidad

@app.delete("/unidades-medidas/{unidad_id}")
def eliminar_unidad_medida(unidad_id: int, db: Session = Depends(get_db)):
    """Eliminar una unidad de medida"""
    db_unidad = db.query(models.Unidades_de_medida).filter(models.Unidades_de_medida.ID_Unidad_Medida == unidad_id).first()
    if not db_unidad:
        raise HTTPException(status_code=404, detail="Unidad de medida no encontrada")
    
    db.delete(db_unidad)
    db.commit()
    return {"message": "Unidad de medida eliminada exitosamente"}

# ====== RUTAS PARA SUCURSALES ======

@app.get("/sucursales/", response_model=List[schemas.Sucursales])
def obtener_sucursales(db: Session = Depends(get_db)):
    """Obtener todas las sucursales"""
    sucursales = db.query(models.Sucursales).all()
    return sucursales

@app.get("/sucursales/{sucursal_id}", response_model=schemas.Sucursales)
def obtener_sucursal(sucursal_id: int, db: Session = Depends(get_db)):
    """Obtener una sucursal específica por ID"""
    sucursal = db.query(models.Sucursales).filter(models.Sucursales.ID_Sucursal == sucursal_id).first()
    if not sucursal:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    return sucursal

@app.post("/sucursales/", response_model=schemas.Sucursales)
def crear_sucursal(sucursal: schemas.SucursalCreate, db: Session = Depends(get_db)):
    """Crear una nueva sucursal"""
    db_sucursal = models.Sucursales(**sucursal.dict())
    db.add(db_sucursal)
    db.commit()
    db.refresh(db_sucursal)
    return db_sucursal

@app.put("/sucursales/{sucursal_id}", response_model=schemas.Sucursales)
def actualizar_sucursal(sucursal_id: int, sucursal: schemas.SucursalUpdate, db: Session = Depends(get_db)):
    """Actualizar una sucursal existente"""
    db_sucursal = db.query(models.Sucursales).filter(models.Sucursales.ID_Sucursal == sucursal_id).first()
    if not db_sucursal:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    
    # Actualizar solo los campos proporcionados
    for field, value in sucursal.dict(exclude_unset=True).items():
        setattr(db_sucursal, field, value)
    
    db.commit()
    db.refresh(db_sucursal)
    return db_sucursal

@app.delete("/sucursales/{sucursal_id}")
def eliminar_sucursal(sucursal_id: int, db: Session = Depends(get_db)):
    """Eliminar una sucursal"""
    db_sucursal = db.query(models.Sucursales).filter(models.Sucursales.ID_Sucursal == sucursal_id).first()
    if not db_sucursal:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    
    db.delete(db_sucursal)
    db.commit()
    return {"message": "Sucursal eliminada exitosamente"}

# ====== RUTAS PARA PROVEEDORES ======

@app.get("/proveedores/", response_model=List[schemas.Proveedores])
def obtener_proveedores(db: Session = Depends(get_db)):
    """Obtener todos los proveedores"""
    proveedores = db.query(models.Proveedores).all()
    return proveedores

@app.get("/proveedores/{proveedor_id}", response_model=schemas.Proveedores)
def obtener_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    """Obtener un proveedor específico por ID"""
    proveedor = db.query(models.Proveedores).filter(models.Proveedores.ID_Proveedor == proveedor_id).first()
    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return proveedor

@app.post("/proveedores/", response_model=schemas.Proveedores)
def crear_proveedor(proveedor: schemas.ProveedoresCreate, db: Session = Depends(get_db)):
    """Crear un nuevo proveedor"""
    db_proveedor = models.Proveedores(**proveedor.dict())
    db.add(db_proveedor)
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

@app.put("/proveedores/{proveedor_id}", response_model=schemas.Proveedores)
def actualizar_proveedor(proveedor_id: int, proveedor: schemas.ProveedoresUpdate, db: Session = Depends(get_db)):
    """Actualizar un proveedor existente"""
    db_proveedor = db.query(models.Proveedores).filter(models.Proveedores.ID_Proveedor == proveedor_id).first()
    if not db_proveedor:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    
    # Actualizar solo los campos proporcionados
    for field, value in proveedor.dict(exclude_unset=True).items():
        setattr(db_proveedor, field, value)
    
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

@app.delete("/proveedores/{proveedor_id}")
def eliminar_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    """Eliminar un proveedor"""
    db_proveedor = db.query(models.Proveedores).filter(models.Proveedores.ID_Proveedor == proveedor_id).first()
    if not db_proveedor:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    
    db.delete(db_proveedor)
    db.commit()
    return {"message": "Proveedor eliminado exitosamente"}

# ====== RUTAS PARA INVENTARIO ======

@app.get("/inventario/", response_model=List[schemas.Inventario])
def obtener_inventario_lista(db: Session = Depends(get_db)):
    """Obtener todo el inventario"""
    inventario = db.query(models.Inventario).all()
    return inventario

@app.get("/inventario/{inventario_id}", response_model=schemas.Inventario)
def obtener_inventario(inventario_id: int, db: Session = Depends(get_db)):
    """Obtener un registro de inventario específico por ID"""
    inventario = db.query(models.Inventario).filter(models.Inventario.ID_Inventario == inventario_id).first()
    if not inventario:
        raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")
    return inventario

@app.post("/inventario/", response_model=schemas.Inventario)
def crear_inventario(inventario: schemas.InventarioCreate, db: Session = Depends(get_db)):
    """Crear un nuevo registro de inventario"""
    db_inventario = models.Inventario(**inventario.dict())
    db.add(db_inventario)
    db.commit()
    db.refresh(db_inventario)
    return db_inventario

@app.put("/inventario/{inventario_id}", response_model=schemas.Inventario)
def actualizar_inventario(inventario_id: int, inventario: schemas.InventarioUpdate, db: Session = Depends(get_db)):
    """Actualizar un registro de inventario existente"""
    db_inventario = db.query(models.Inventario).filter(models.Inventario.ID_Inventario == inventario_id).first()
    if not db_inventario:
        raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")
    
    # Actualizar solo los campos proporcionados
    for field, value in inventario.dict(exclude_unset=True).items():
        setattr(db_inventario, field, value)
    
    db.commit()
    db.refresh(db_inventario)
    return db_inventario

@app.delete("/inventario/{inventario_id}")
def eliminar_inventario(inventario_id: int, db: Session = Depends(get_db)):
    """Eliminar un registro de inventario"""
    db_inventario = db.query(models.Inventario).filter(models.Inventario.ID_Inventario == inventario_id).first()
    if not db_inventario:
        raise HTTPException(status_code=404, detail="Registro de inventario no encontrado")
    
    db.delete(db_inventario)
    db.commit()
    return {"message": "Registro de inventario eliminado exitosamente"}

# Ruta adicional para obtener inventario por producto
@app.get("/inventario/producto/{producto_id}", response_model=List[schemas.Inventario])
def obtener_inventario_por_producto(producto_id: int, db: Session = Depends(get_db)):
    """Obtener inventario de un producto específico en todas las sucursales"""
    inventario = db.query(models.Inventario).filter(models.Inventario.ID_Producto == producto_id).all()
    return inventario

# ====== RUTAS PARA FACTURAS DE VENTA ======

@app.get("/facturas-venta/", response_model=List[schemas.FacturasVentas])
def obtener_facturas_venta(db: Session = Depends(get_db)):
    """Obtener todas las facturas de venta"""
    facturas = db.query(models.Facturas_Venta).all()
    return facturas

@app.get("/facturas-venta/{factura_id}", response_model=schemas.FacturasVentas)
def obtener_factura_venta(factura_id: int, db: Session = Depends(get_db)):
    """Obtener una factura de venta específica por ID"""
    factura = db.query(models.Facturas_Venta).filter(models.Facturas_Venta.ID_Factura_Venta == factura_id).first()
    if not factura:
        raise HTTPException(status_code=404, detail="Factura de venta no encontrada")
    return factura

@app.post("/facturas-venta/", response_model=schemas.FacturasVentas)
def crear_factura_venta(factura: schemas.FacturasVentasCreate, db: Session = Depends(get_db)):
    """Crear una nueva factura de venta"""
    db_factura = models.Facturas_Venta(**factura.dict())
    db.add(db_factura)
    db.commit()
    db.refresh(db_factura)
    return db_factura

@app.put("/facturas-venta/{factura_id}", response_model=schemas.FacturasVentas)
def actualizar_factura_venta(factura_id: int, factura: schemas.FacturasVentasUpdate, db: Session = Depends(get_db)):
    """Actualizar una factura de venta existente"""
    db_factura = db.query(models.Facturas_Venta).filter(models.Facturas_Venta.ID_Factura_Venta == factura_id).first()
    if not db_factura:
        raise HTTPException(status_code=404, detail="Factura de venta no encontrada")
    
    # Actualizar solo los campos proporcionados
    for field, value in factura.dict(exclude_unset=True).items():
        setattr(db_factura, field, value)
    
    db.commit()
    db.refresh(db_factura)
    return db_factura

@app.delete("/facturas-venta/{factura_id}")
def eliminar_factura_venta(factura_id: int, db: Session = Depends(get_db)):
    """Eliminar una factura de venta"""
    db_factura = db.query(models.Facturas_Venta).filter(models.Facturas_Venta.ID_Factura_Venta == factura_id).first()
    if not db_factura:
        raise HTTPException(status_code=404, detail="Factura de venta no encontrada")
    
    db.delete(db_factura)
    db.commit()
    return {"message": "Factura de venta eliminada exitosamente"}

# Ruta adicional para obtener facturas por cliente
@app.get("/facturas-venta/cliente/{cliente_id}", response_model=List[schemas.FacturasVentas])
def obtener_facturas_por_cliente(cliente_id: int, db: Session = Depends(get_db)):
    """Obtener todas las facturas de un cliente específico"""
    facturas = db.query(models.Facturas_Venta).filter(models.Facturas_Venta.ID_Cliente == cliente_id).all()
    return facturas


# ====== RUTAS PARA DETALLES DE FACTURA VENTA ======

@app.get("/detalles-factura-venta/", response_model=List[schemas.DetallesFacturaVenta])
def obtener_detalles_factura_venta(db: Session = Depends(get_db)):
    """Obtener todos los detalles de facturas de venta"""
    detalles = db.query(models.Detalles_Factura_Venta).all()
    return detalles

@app.get("/detalles-factura-venta/{detalle_id}", response_model=schemas.DetallesFacturaVenta)
def obtener_detalle_factura_venta(detalle_id: int, db: Session = Depends(get_db)):
    """Obtener un detalle de factura de venta específico por ID"""
    detalle = db.query(models.Detalles_Factura_Venta).filter(models.Detalles_Factura_Venta.ID_Detalle == detalle_id).first()
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle de factura no encontrado")
    return detalle

@app.post("/detalles-factura-venta/", response_model=schemas.DetallesFacturaVenta)
def crear_detalle_factura_venta(detalle: schemas.DetallesFacturasVentaCreate, db: Session = Depends(get_db)):
    """Crear un nuevo detalle de factura de venta"""
    db_detalle = models.Detalles_Factura_Venta(**detalle.dict())
    db.add(db_detalle)
    db.commit()
    db.refresh(db_detalle)
    return db_detalle

@app.put("/detalles-factura-venta/{detalle_id}", response_model=schemas.DetallesFacturaVenta)
def actualizar_detalle_factura_venta(detalle_id: int, detalle: schemas.DetallesFacturaVentaUpdate, db: Session = Depends(get_db)):
    """Actualizar un detalle de factura de venta existente"""
    db_detalle = db.query(models.Detalles_Factura_Venta).filter(models.Detalles_Factura_Venta.ID_Detalle == detalle_id).first()
    if not db_detalle:
        raise HTTPException(status_code=404, detail="Detalle de factura no encontrado")
    
    # Actualizar solo los campos proporcionados
    for field, value in detalle.dict(exclude_unset=True).items():
        setattr(db_detalle, field, value)
    
    db.commit()
    db.refresh(db_detalle)
    return db_detalle

@app.delete("/detalles-factura-venta/{detalle_id}")
def eliminar_detalle_factura_venta(detalle_id: int, db: Session = Depends(get_db)):
    """Eliminar un detalle de factura de venta"""
    db_detalle = db.query(models.Detalles_Factura_Venta).filter(models.Detalles_Factura_Venta.ID_Detalle == detalle_id).first()
    if not db_detalle:
        raise HTTPException(status_code=404, detail="Detalle de factura no encontrado")
    
    db.delete(db_detalle)
    db.commit()
    return {"message": "Detalle de factura eliminado exitosamente"}

# Ruta adicional para obtener detalles por factura
@app.get("/detalles-factura-venta/factura/{factura_id}", response_model=List[schemas.DetallesFacturaVenta])
def obtener_detalles_por_factura(factura_id: int, db: Session = Depends(get_db)):
    """Obtener todos los detalles de una factura específica"""
    detalles = db.query(models.Detalles_Factura_Venta).filter(models.Detalles_Factura_Venta.ID_Factura_Venta == factura_id).all()
    return detalles


# ====== RUTAS PARA PAGOS ======

@app.get("/pagos/", response_model=List[schemas.Pagos])
def obtener_pagos(db: Session = Depends(get_db)):
    """Obtener todos los pagos"""
    pagos = db.query(models.Pagos).all()
    return pagos

@app.get("/pagos/{pago_id}", response_model=schemas.Pagos)
def obtener_pago(pago_id: int, db: Session = Depends(get_db)):
    """Obtener un pago específico por ID"""
    pago = db.query(models.Pagos).filter(models.Pagos.ID_Pago == pago_id).first()
    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return pago

@app.post("/pagos/", response_model=schemas.Pagos)
def crear_pago(pago: schemas.PagosCreate, db: Session = Depends(get_db)):
    """Crear un nuevo pago"""
    db_pago = models.Pagos(**pago.dict())
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)
    return db_pago

@app.put("/pagos/{pago_id}", response_model=schemas.Pagos)
def actualizar_pago(pago_id: int, pago: schemas.PagosUpdate, db: Session = Depends(get_db)):
    """Actualizar un pago existente"""
    db_pago = db.query(models.Pagos).filter(models.Pagos.ID_Pago == pago_id).first()
    if not db_pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    
    # Actualizar solo los campos proporcionados
    for field, value in pago.dict(exclude_unset=True).items():
        setattr(db_pago, field, value)
    
    db.commit()
    db.refresh(db_pago)
    return db_pago

@app.delete("/pagos/{pago_id}")
def eliminar_pago(pago_id: int, db: Session = Depends(get_db)):
    """Eliminar un pago"""
    db_pago = db.query(models.Pagos).filter(models.Pagos.ID_Pago == pago_id).first()
    if not db_pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    
    db.delete(db_pago)
    db.commit()
    return {"message": "Pago eliminado exitosamente"}

# Ruta adicional para obtener pagos por factura
@app.get("/pagos/factura/{factura_id}", response_model=List[schemas.Pagos])
def obtener_pagos_por_factura(factura_id: int, db: Session = Depends(get_db)):
    """Obtener todos los pagos de una factura específica"""
    pagos = db.query(models.Pagos).filter(models.Pagos.ID_Factura_Venta == factura_id).all()
    return pagos


# ====== RUTAS PARA ÓRDENES DE COMPRA ======

@app.get("/ordenes-compra/", response_model=List[schemas.OrdenesCompra])
def obtener_ordenes_compra(db: Session = Depends(get_db)):
    """Obtener todas las órdenes de compra"""
    ordenes = db.query(models.Ordenes_Compra).all()
    return ordenes

@app.get("/ordenes-compra/{orden_id}", response_model=schemas.OrdenesCompra)
def obtener_orden_compra(orden_id: int, db: Session = Depends(get_db)):
    """Obtener una orden de compra específica por ID"""
    orden = db.query(models.Ordenes_Compra).filter(models.Ordenes_Compra.ID_OC == orden_id).first()
    if not orden:
        raise HTTPException(status_code=404, detail="Orden de compra no encontrada")
    return orden

@app.post("/ordenes-compra/", response_model=schemas.OrdenesCompra)
def crear_orden_compra(orden: schemas.OrdenesCompraCreate, db: Session = Depends(get_db)):
    """Crear una nueva orden de compra"""
    db_orden = models.Ordenes_Compra(**orden.dict())
    db.add(db_orden)
    db.commit()
    db.refresh(db_orden)
    return db_orden

@app.put("/ordenes-compra/{orden_id}", response_model=schemas.OrdenesCompra)
def actualizar_orden_compra(orden_id: int, orden: schemas.OrdenesCompraUpdate, db: Session = Depends(get_db)):
    """Actualizar una orden de compra existente"""
    db_orden = db.query(models.Ordenes_Compra).filter(models.Ordenes_Compra.ID_OC == orden_id).first()
    if not db_orden:
        raise HTTPException(status_code=404, detail="Orden de compra no encontrada")
    
    # Actualizar solo los campos proporcionados
    for field, value in orden.dict(exclude_unset=True).items():
        setattr(db_orden, field, value)
    
    db.commit()
    db.refresh(db_orden)
    return db_orden

@app.delete("/ordenes-compra/{orden_id}")
def eliminar_orden_compra(orden_id: int, db: Session = Depends(get_db)):
    """Eliminar una orden de compra"""
    db_orden = db.query(models.Ordenes_Compra).filter(models.Ordenes_Compra.ID_OC == orden_id).first()
    if not db_orden:
        raise HTTPException(status_code=404, detail="Orden de compra no encontrada")
    
    db.delete(db_orden)
    db.commit()
    return {"message": "Orden de compra eliminada exitosamente"}

# Ruta adicional para obtener órdenes por proveedor
@app.get("/ordenes-compra/proveedor/{proveedor_id}", response_model=List[schemas.OrdenesCompra])
def obtener_ordenes_por_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    """Obtener todas las órdenes de compra de un proveedor específico"""
    ordenes = db.query(models.Ordenes_Compra).filter(models.Ordenes_Compra.ID_Proveedor == proveedor_id).all()
    return ordenes


# ====== RUTAS PARA DETALLES DE OC ======

@app.get("/detalle-oc/", response_model=List[schemas.DetalleOC])
def obtener_detalles_oc(db: Session = Depends(get_db)):
    """Obtener todos los detalles de órdenes de compra"""
    detalles = db.query(models.Detalle_OC).all()
    return detalles

@app.get("/detalle-oc/{detalle_id}", response_model=schemas.DetalleOC)
def obtener_detalle_oc(detalle_id: int, db: Session = Depends(get_db)):
    """Obtener un detalle de orden de compra específico por ID"""
    detalle = db.query(models.Detalle_OC).filter(models.Detalle_OC.ID_Detalle_OC == detalle_id).first()
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle de orden de compra no encontrado")
    return detalle

@app.post("/detalle-oc/", response_model=schemas.DetalleOC)
def crear_detalle_oc(detalle: schemas.DetalleOCCreate, db: Session = Depends(get_db)):
    """Crear un nuevo detalle de orden de compra"""
    db_detalle = models.Detalle_OC(**detalle.dict())
    db.add(db_detalle)
    db.commit()
    db.refresh(db_detalle)
    return db_detalle

@app.put("/detalle-oc/{detalle_id}", response_model=schemas.DetalleOC)
def actualizar_detalle_oc(detalle_id: int, detalle: schemas.DetalleOCUpdate, db: Session = Depends(get_db)):
    """Actualizar un detalle de orden de compra existente"""
    db_detalle = db.query(models.Detalle_OC).filter(models.Detalle_OC.ID_Detalle_OC == detalle_id).first()
    if not db_detalle:
        raise HTTPException(status_code=404, detail="Detalle de orden de compra no encontrado")
    
    # Actualizar solo los campos proporcionados
    for field, value in detalle.dict(exclude_unset=True).items():
        setattr(db_detalle, field, value)
    
    db.commit()
    db.refresh(db_detalle)
    return db_detalle

@app.delete("/detalle-oc/{detalle_id}")
def eliminar_detalle_oc(detalle_id: int, db: Session = Depends(get_db)):
    """Eliminar un detalle de orden de compra"""
    db_detalle = db.query(models.Detalle_OC).filter(models.Detalle_OC.ID_Detalle_OC == detalle_id).first()
    if not db_detalle:
        raise HTTPException(status_code=404, detail="Detalle de orden de compra no encontrado")
    
    db.delete(db_detalle)
    db.commit()
    return {"message": "Detalle de orden de compra eliminado exitosamente"}

# Ruta adicional para obtener detalles por orden de compra
@app.get("/detalle-oc/orden/{orden_id}", response_model=List[schemas.DetalleOC])
def obtener_detalles_por_orden(orden_id: int, db: Session = Depends(get_db)):
    """Obtener todos los detalles de una orden de compra específica"""
    detalles = db.query(models.Detalle_OC).filter(models.Detalle_OC.ID_OC == orden_id).all()
    return detalles


# ====== RUTAS PARA MOVIMIENTOS DE INVENTARIO ======

@app.get("/movimientos-inventario/", response_model=List[schemas.MovimientosInventario])
def obtener_movimientos_inventario(db: Session = Depends(get_db)):
    """Obtener todos los movimientos de inventario"""
    movimientos = db.query(models.Movimientos_Inventario).all()
    return movimientos

@app.get("/movimientos-inventario/{movimiento_id}", response_model=schemas.MovimientosInventario)
def obtener_movimiento_inventario(movimiento_id: int, db: Session = Depends(get_db)):
    """Obtener un movimiento de inventario específico por ID"""
    movimiento = db.query(models.Movimientos_Inventario).filter(models.Movimientos_Inventario.ID_Movimiento == movimiento_id).first()
    if not movimiento:
        raise HTTPException(status_code=404, detail="Movimiento de inventario no encontrado")
    return movimiento

@app.post("/movimientos-inventario/", response_model=schemas.MovimientosInventario)
def crear_movimiento_inventario(movimiento: schemas.MovimientosInventarioCreate, db: Session = Depends(get_db)):
    """Crear un nuevo movimiento de inventario"""
    db_movimiento = models.Movimientos_Inventario(**movimiento.dict())
    db.add(db_movimiento)
    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento

@app.put("/movimientos-inventario/{movimiento_id}", response_model=schemas.MovimientosInventario)
def actualizar_movimiento_inventario(movimiento_id: int, movimiento: schemas.MovimientosInventarioUpdate, db: Session = Depends(get_db)):
    """Actualizar un movimiento de inventario existente"""
    db_movimiento = db.query(models.Movimientos_Inventario).filter(models.Movimientos_Inventario.ID_Movimiento == movimiento_id).first()
    if not db_movimiento:
        raise HTTPException(status_code=404, detail="Movimiento de inventario no encontrado")
    
    # Actualizar solo los campos proporcionados
    for field, value in movimiento.dict(exclude_unset=True).items():
        setattr(db_movimiento, field, value)
    
    db.commit()
    db.refresh(db_movimiento)
    return db_movimiento

@app.delete("/movimientos-inventario/{movimiento_id}")
def eliminar_movimiento_inventario(movimiento_id: int, db: Session = Depends(get_db)):
    """Eliminar un movimiento de inventario"""
    db_movimiento = db.query(models.Movimientos_Inventario).filter(models.Movimientos_Inventario.ID_Movimiento == movimiento_id).first()
    if not db_movimiento:
        raise HTTPException(status_code=404, detail="Movimiento de inventario no encontrado")
    
    db.delete(db_movimiento)
    db.commit()
    return {"message": "Movimiento de inventario eliminado exitosamente"}

# Rutas adicionales para movimientos de inventario
@app.get("/movimientos-inventario/producto/{producto_id}", response_model=List[schemas.MovimientosInventario])
def obtener_movimientos_por_producto(producto_id: int, db: Session = Depends(get_db)):
    """Obtener todos los movimientos de un producto específico"""
    movimientos = db.query(models.Movimientos_Inventario).filter(models.Movimientos_Inventario.ID_Producto == producto_id).all()
    return movimientos

@app.get("/movimientos-inventario/sucursal/{sucursal_id}", response_model=List[schemas.MovimientosInventario])
def obtener_movimientos_por_sucursal(sucursal_id: int, db: Session = Depends(get_db)):
    """Obtener todos los movimientos de una sucursal específica"""
    movimientos = db.query(models.Movimientos_Inventario).filter(models.Movimientos_Inventario.ID_Sucursal == sucursal_id).all()
    return movimientos

@app.get("/movimientos-inventario/tipo/{tipo}", response_model=List[schemas.MovimientosInventario])
def obtener_movimientos_por_tipo(tipo: str, db: Session = Depends(get_db)):
    """Obtener todos los movimientos de un tipo específico (Entrada, Salida, etc.)"""
    movimientos = db.query(models.Movimientos_Inventario).filter(models.Movimientos_Inventario.Tipo == tipo).all()
    return movimientos

# ====== RUTAS PARA PRODUCTOS ======

@app.get("/productos/", response_model=List[schemas.Productos])
def obtener_productos(db: Session = Depends(get_db)):
    """Obtener todos los productos"""
    productos = db.query(models.Productos).all()
    return productos

@app.get("/productos/{producto_id}", response_model=schemas.Productos)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    """Obtener un producto específico por ID"""
    producto = db.query(models.Productos).filter(models.Productos.ID_Productos == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.post("/productos/", response_model=schemas.Productos)
def crear_producto(producto: schemas.ProductosCreate, db: Session = Depends(get_db)):
    """Crear un nuevo producto"""
    db_producto = models.Productos(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@app.put("/productos/{producto_id}", response_model=schemas.Productos)
def actualizar_producto(producto_id: int, producto: schemas.ProductosUpdate, db: Session = Depends(get_db)):
    """Actualizar un producto existente"""
    db_producto = db.query(models.Productos).filter(models.Productos.ID_Productos == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # Actualizar solo los campos proporcionados
    for field, value in producto.dict(exclude_unset=True).items():
        setattr(db_producto, field, value)
    
    db.commit()
    db.refresh(db_producto)
    return db_producto

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    """Eliminar un producto"""
    db_producto = db.query(models.Productos).filter(models.Productos.ID_Productos == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(db_producto)
    db.commit()
    return {"message": "Producto eliminado exitosamente"}

# Rutas adicionales para productos
@app.get("/productos/categoria/{categoria_id}", response_model=List[schemas.Productos])
def obtener_productos_por_categoria(categoria_id: int, db: Session = Depends(get_db)):
    """Obtener todos los productos de una categoría específica"""
    productos = db.query(models.Productos).filter(models.Productos.ID_Categoria == categoria_id).all()
    return productos

@app.get("/productos/buscar/{nombre}", response_model=List[schemas.Productos])
def buscar_productos_por_nombre(nombre: str, db: Session = Depends(get_db)):
    """Buscar productos por nombre (búsqueda parcial)"""
    productos = db.query(models.Productos).filter(models.Productos.Nombre.contains(nombre)).all()
    return productos

# ====== RUTAS PARA CLIENTES ======

@app.get("/clientes/", response_model=List[schemas.Clientes])
def obtener_clientes(db: Session = Depends(get_db)):
    """Obtener todos los clientes"""
    clientes = db.query(models.Clientes).all()
    return clientes

@app.get("/clientes/{cliente_id}", response_model=schemas.Clientes)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    """Obtener un cliente específico por ID"""
    cliente = db.query(models.Clientes).filter(models.Clientes.ID_Cliente == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.post("/clientes/", response_model=schemas.Clientes)
def crear_cliente(cliente: schemas.ClientesCreate, db: Session = Depends(get_db)):
    """Crear un nuevo cliente"""
    db_cliente = models.Clientes(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@app.put("/clientes/{cliente_id}", response_model=schemas.Clientes)
def actualizar_cliente(cliente_id: int, cliente: schemas.ClientesUpdate, db: Session = Depends(get_db)):
    """Actualizar un cliente existente"""
    db_cliente = db.query(models.Clientes).filter(models.Clientes.ID_Cliente == cliente_id).first()
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    # Actualizar solo los campos proporcionados
    for field, value in cliente.dict(exclude_unset=True).items():
        setattr(db_cliente, field, value)
    
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    """Eliminar un cliente"""
    db_cliente = db.query(models.Clientes).filter(models.Clientes.ID_Cliente == cliente_id).first()
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    db.delete(db_cliente)
    db.commit()
    return {"message": "Cliente eliminado exitosamente"}

# Rutas adicionales para clientes
@app.get("/clientes/buscar/{nombre}", response_model=List[schemas.Clientes])
def buscar_clientes_por_nombre(nombre: str, db: Session = Depends(get_db)):
    """Buscar clientes por nombre (búsqueda parcial)"""
    clientes = db.query(models.Clientes).filter(models.Clientes.Nombre.contains(nombre)).all()
    return clientes

@app.get("/clientes/email/{email}", response_model=schemas.Clientes)
def obtener_cliente_por_email(email: str, db: Session = Depends(get_db)):
    """Obtener un cliente por email"""
    cliente = db.query(models.Clientes).filter(models.Clientes.Email == email).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

# ====== RUTAS PARA USUARIOS ======

@app.get("/usuarios/", response_model=List[schemas.Usuarios])
def obtener_usuarios(db: Session = Depends(get_db)):
    """Obtener todos los usuarios"""
    usuarios = db.query(models.Usuarios).all()
    return usuarios

@app.get("/usuarios/{usuario_id}", response_model=schemas.Usuarios)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Obtener un usuario específico por ID"""
    usuario = db.query(models.Usuarios).filter(models.Usuarios.ID_Usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.post("/usuarios/", response_model=schemas.Usuarios)
def crear_usuario(usuario: schemas.UsuariosCreate, db: Session = Depends(get_db)):
    """Crear un nuevo usuario"""
    db_usuario = models.Usuarios(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@app.put("/usuarios/{usuario_id}", response_model=schemas.Usuarios)
def actualizar_usuario(usuario_id: int, usuario: schemas.UsuariosUpdate, db: Session = Depends(get_db)):
    """Actualizar un usuario existente"""
    db_usuario = db.query(models.Usuarios).filter(models.Usuarios.ID_Usuario == usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Actualizar solo los campos proporcionados
    for field, value in usuario.dict(exclude_unset=True).items():
        setattr(db_usuario, field, value)
    
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Eliminar un usuario"""
    db_usuario = db.query(models.Usuarios).filter(models.Usuarios.ID_Usuario == usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(db_usuario)
    db.commit()
    return {"message": "Usuario eliminado exitosamente"}

# Rutas adicionales para usuarios
@app.get("/usuarios/email/{email}", response_model=schemas.Usuarios)
def obtener_usuario_por_email(email: str, db: Session = Depends(get_db)):
    """Obtener un usuario por email"""
    usuario = db.query(models.Usuarios).filter(models.Usuarios.Email == email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.get("/usuarios/rol/{rol}", response_model=List[schemas.Usuarios])
def obtener_usuarios_por_rol(rol: str, db: Session = Depends(get_db)):
    """Obtener todos los usuarios de un rol específico"""
    usuarios = db.query(models.Usuarios).filter(models.Usuarios.Rol == rol).all()
    return usuarios

@app.get("/usuarios/activos", response_model=List[schemas.Usuarios])
def obtener_usuarios_activos(db: Session = Depends(get_db)):
    """Obtener todos los usuarios activos"""
    usuarios = db.query(models.Usuarios).filter(models.Usuarios.Estado == True).all()
    return usuarios
