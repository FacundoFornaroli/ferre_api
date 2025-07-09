from database import engine, get_db
from sqlalchemy import text
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def test_database_connection():
    """Prueba la conexión a la base de datos"""
    try:
        print("Probando conexión a la base de datos...")
        print(f"URL de conexión: {os.getenv('SQLSERVER_CONN')}")
        
        # Probar la conexión
        with engine.connect() as connection:
            print(" Conexión exitosa!")
            
            # Ejecutar una consulta simple
            result = connection.execute(text("SELECT @@VERSION as version"))
            version = result.fetchone()
            print(f"Versión de SQL Server: {version[0]}")
            
            # Verificar que la base de datos existe
            result = connection.execute(text("SELECT DB_NAME() as current_db"))
            db_name = result.fetchone()
            print(f"Base de datos actual: {db_name[0]}")
            
            # Listar algunas tablas
            result = connection.execute(text("""
                SELECT TABLE_NAME 
                FROM INFORMATION_SCHEMA.TABLES 
                WHERE TABLE_TYPE = 'BASE TABLE'
                ORDER BY TABLE_NAME
            """))
            
            tables = result.fetchall()
            print(f" Tablas encontradas ({len(tables)}):")
            for table in tables[:10]: 
                print(f"   - {table[0]}")
            
            if len(tables) > 10:
                print(f"   ... y {len(tables) - 10} más")
                
    except Exception as e:
        print(f" Error de conexión: {str(e)}")
        print("Posibles soluciones:")
        print("1. Verifica que SQL Server esté ejecutándose")
        print("2. Revisa la cadena de conexión en el archivo .env")
        print("3. Asegúrate de que el ODBC Driver esté instalado")
        print("4. Verifica que la base de datos 'Ferreteriadb' exista")

def test_models():
    """Prueba que los modelos se pueden usar"""
    try:
        print(" Probando modelos...")
        import models
        
        # Verificar que los modelos se importan correctamente
        print(" Modelos importados correctamente")
        
        # Listar los modelos disponibles
        model_names = [name for name in dir(models) if not name.startswith('_')]
        print(f"Modelos disponibles: {model_names}")
        
    except Exception as e:
        print(f"Error con los modelos: {str(e)}")

if __name__ == "__main__":
    print("Iniciando pruebas de conexión...\n")
    test_database_connection()
    test_models()
    print("Pruebas completadas!")