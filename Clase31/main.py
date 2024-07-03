from modules.manager import ManagerSqlite
from modules.pelicula import Pelicula

def main():
    manager = ManagerSqlite("pelis.db")
    
    peli = Pelicula("inception", 110, "accion", '2020-10-10')
    peli_dos = Pelicula("Matrix", 120, "Science Fi", '1999-12-10')
    
    #manager.insert_one_pelicula(peli)
    #manager.insert_one_pelicula(peli_dos)
    
    for pelicula in manager.get_all_pelicula():
        print(pelicula)
    
    
if __name__ == "__main__":
    main()
    
    