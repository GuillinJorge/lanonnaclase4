def save_user_db(**kwargs) -> None:
    """
    Guarda un diccionario de usuario en una base de datos si se selecciona la opción predeterminada.
    
    La función toma argumentos clave-valor (`kwargs`) que deben incluir:
        - 'user': Diccionario que contiene los datos del usuario.
        - 'database': Lista que representa la base de datos donde se guardarán los datos del usuario.
        - 'option' (opcional): Opción para guardar el usuario en la base de datos. Por defecto es 'y'.
    
    Si la opción proporcionada es 'y', el usuario se agrega a la base de datos.
    
    Args:
        **kwargs: Argumentos clave-valor que incluyen 'user', 'database' y opcionalmente 'option'.
        
    Returns:
        None
    
    Ejemplo:
        >>> user = {'nombre': 'juan'}
        >>> database = []
        >>> save_user_db(user=user, database=database, option='y')
        >>> print(database)
        [{'nombre': 'juan'}]
    """
    user: dict = kwargs["user"]
    database: list = kwargs["database"]
    option: str = kwargs.get("option", "y")

    if option != 'y':
        return
    database.append(user)
