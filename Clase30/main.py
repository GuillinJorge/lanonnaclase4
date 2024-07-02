import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.sql import text

def insert_data_into_table(query: str):
    """
    Inserta datos en la tabla especificada dentro de una base de datos SQLite.

    Parameters:
    query (str): La consulta SQL a ejecutar para insertar datos en la tabla.

    Returns:
    None
    """
    engine = create_engine("sqlite:///C:/Users/Jorge Guillin/Desktop/Programación/CodoACodo - Última parte/lanonnaclase4/Clase30/users.db")

    with engine.connect() as conn:
        result = conn.execute(text(query))
        conn.commit()
        print("¡Éxito! Datos insertados.")

def create_database_sqlite(name: str):
    """
    Crea una base de datos SQLite y una tabla llamada 'products' si no existe.

    Parameters:
    name (str): El nombre de la base de datos.

    Returns:
    None
    """
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products
        (
            dni INTEGER PRIMARY KEY, 
            nombre VARCHAR(100),
            apellido VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100)
        );
        """
    )
    conn.commit()

def main():
    """
    Función principal que inserta datos en la tabla 'products'.

    Parameters:
    None

    Returns:
    None
    """
    query = """
    INSERT INTO products
    (
        dni, 
        nombre, 
        apellido, 
        email, 
        password
    )
    VALUES
    (
        9999, 'miguel', 'rasputin', 'rasputin@cac_company.edu.ar', '123'
    );
    """
    insert_data_into_table(query)

if __name__ == "__main__":
    main()
