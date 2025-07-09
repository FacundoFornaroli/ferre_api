from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la cadena de conexión desde las variables de entorno
DATABASE_URL = os.getenv("SQLSERVER_CONN")

# Crear el motor de la base de datos
# Este es como el "conductor" que maneja la conexión
engine = create_engine(DATABASE_URL)

# Crear una sesión local para interactuar con la base de datos
# Es como abrir una "conversación" con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base para los modelos
# Esto nos permite crear "plantillas" para nuestras tablas
Base = declarative_base()

# Función para obtener la sesión de la base de datos
def get_db():
    """
    Esta función crea una nueva sesión de base de datos
    y la cierra automáticamente cuando termina
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
