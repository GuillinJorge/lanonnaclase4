def add_custom_msg(user: dict, msg: str = "Bienvenido") -> dict:
    """
    Agrega un mensaje personalizado a un diccionario de usuario.
    
    La función toma un diccionario de usuario y una cadena de mensaje opcional.
    Si no se proporciona un mensaje, se usa "Bienvenido" como valor predeterminado.
    El mensaje se agrega al diccionario de usuario con la clave 'msg'.
    
    Args:
        user (dict): Diccionario que contiene los datos del usuario.
        msg (str, opcional): Mensaje personalizado a agregar al diccionario de usuario. Por defecto es "Bienvenido".
        
    Returns:
        dict: Diccionario de usuario actualizado con la clave 'msg'.
    
    Ejemplo:
        >>> user = {'nombre': 'juan'}
        >>> add_custom_msg(user)
        {'nombre': 'juan', 'msg': 'Bienvenido'}
        >>> add_custom_msg(user, 'Hola, Juan!')
        {'nombre': 'juan', 'msg': 'Hola, Juan!'}
    """
    user["msg"] = msg
    return user
