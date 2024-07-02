from sqlalchemy import create_engine, text

class SqliteDataBase:
    def __init__(self, path_cnx:str):
        
        path_cnx = f'sqlite:///{path_cnx}'
        
        self.engine = create_engine(path_cnx) # RUTA DE ACCESO
        query = f"""
        CREATE TABLE IF NOT EXISTS peliculas (
            id_pelicula INTEGER, PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR (254),
            duracion INT,
            genero VARCHAR(100),
            release_date DATE,
        )
        """

        with self.engine.connect() as conn:
            result = conn.execute(text(query))
            conn.commit()
    
        print("¡Éxito! Base de datos creada.")
        
    def insert_one_pelicula(self, Pelicula):