import sqlite3
from sqlalchemy import create_engine


def insert_data_into_table(
    query:str
):
    engine = create_engine("./users.db")
    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()
        print("Exitoso!!! Data insertada!!!")
    
def create_database_sqlite(name:str):

    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products
        (
            dni INTEGER PRIMARY KEY, 
            nombre VARCHAR (100),
            apellido VARCHAR (100),
            email VARCHAR (100),
            password VARCHAR (100)
        );
        """
    )
    
    conn.commit()
    
def main():
    # create_database_sqlite("users.db")
    query:str = f"""
    INSERT INTO products
   (
        dni 
    ,   nombre
    ,   apellido
    ,   email 
    ,   password)
    VALUES
    (9999, 'miguel', 'rasputin', 'rasputin@cac_company.edu.ar', "123");
    
    """
    insert_data_into_table(query)
    
    if __name__ == "__main__":
        main()

