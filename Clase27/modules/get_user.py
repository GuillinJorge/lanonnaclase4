def get_user() -> dict:
    """
    Solicita al usuario que ingrese su nombre y apellido, y retorna un diccionario con esta información.
    
    La función pide al usuario que ingrese su nombre y apellido a través de la entrada estándar (input).
    Luego, almacena estos valores en un diccionario con las claves 'nombre' y 'apellido' respectivamente.
    
    Returns:
        dict: Diccionario que contiene el nombre y el apellido del usuario.
    
    Ejemplo:
        >>> user = get_user()
        Ingrese su nombre:
        Juan
        Ingrese su apellido:
        Pérez
        >>> print(user)
        {'nombre': 'Juan', 'apellido': 'Pérez'}
    """
    usuario: dict = {}
    usuario["nombre"] = input("Ingrese su nombre:\n")
    usuario["apellido"] = input("Ingrese su apellido:\n")
    return usuario
