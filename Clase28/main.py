class Usuario:
    nombre:str 
    edad:int
    sexo:str
    
    
def saludar(self, saludo_especial:str) -> None:
    print(f"{saludo_especial} {self.nombre}!")
    
def main():
    marcos: Usuario = Usuario()
    marcos.nombre = "Marco Aurelio"
    marcos.edad = 37
    marcos.sexo = "masc"
    
    
    mariela: Usuario = Usuario()
    mariela.nombre = "Mariela Lopez"
    mariela.edad = 40
    mariela.sexo = "fem"

    marcos.saludar("Hola mundo, soy: -> ") 
    mariela.saludar("Hi, I am ->")
    

    if __name__ == "__main__":
        main()