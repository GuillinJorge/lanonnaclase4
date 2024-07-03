from modules.manager import ManagerSqlite
from modules.pelicula import Pelicula

def main():
    manager = ManagerSqlite("pelis.db")
    
    texto:str = f"""
        Bienvenidos a Gestor de Series ver 0.1
            Elija una opción:
            - 1 : Insertar Pelicula
            - 2 : Borrar Pelicula
            - 3 : Modificar Pelicula
            - 4 : Mostrar Peliculas
            - X : Salir
    """
    flag:bool = True
    
    while flag:
        option:str = input(texto)
        
        if option == '1':
            nombre = input ("Ingrese el nombre de la pelicula:\n")
            duracion = int(input("Ingrese la duración de la pelicula:\n"))
            genero = input ("Ingrese el genero de la pelicula:\n")
            date_release = input("Ingrese la fecha de la pelicula:\nformat: yyyy-mm-dd ")
            pelicula = Pelicula(nombre, duracion, genero, date_release)
            manager.insert_one_pelicula(pelicula)
            option:str = input(texto)
        
        if option == '4':
            for pelicula in manager.get_all_pelicula():
                print(pelicula)
            option:str = input(texto)
        
        else:
            print("Usted ha decidido salir")
            flag = False
            
    
    
    
    #peli = Pelicula("Mision Imposible", 120, "accion", '2010-10-10')
    #peli_dos = Pelicula("Matrix", 120, "Science Fi", '1999-12-10')
    #peli_tres = Pelicula("inception", 130, "Suspense", '2012-04-24')
    
    #manager.insert_one_pelicula(peli)
    #manager.insert_one_pelicula(peli_dos)
    #manager.insert_one_pelicula(peli_tres)
    
    #for pelicula in manager.get_all_pelicula():
    #    print(pelicula)
    
    #for pelicula in manager.get_one_pelicula("E.T.", 91, "Science Fi", '1989-12-10'):
    #    print(pelicula)
    
    #manager.delete_row_in_db("Matrix")
    manager.update_in_database("Inception","duracion",60*2)
    
if __name__ == "__main__":
    main()
    
    