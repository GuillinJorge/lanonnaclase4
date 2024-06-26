def add_email_pwd(user: dict) -> dict:
    """
    Agrega un correo electrónico y una contraseña a un diccionario de usuario.
    
    La función toma un diccionario de usuario como entrada y agrega/actualiza
    dos claves en el diccionario:
        - 'email': Se genera un correo electrónico basado en el nombre del usuario y el dominio de la empresa.
        - 'pwd': Se agrega una contraseña predeterminada.
    
    Args:
        user (dict): Diccionario que contiene los datos del usuario.
        
    Returns:
        dict: Diccionario de usuario actualizado con las claves 'email' y 'pwd'.
    
    Ejemplo:
        >>> user = {'nombre': 'juan'}
        >>> add_email_pwd(user)
        {'nombre': 'juan', 'email': 'juan@cac_company.edu.ar', 'pwd': 'Pass123!'}
    """
    empresa: str = "cac_company"
    nombre_user = user.get('nombre', 'nuevo_ingresante')
    user["email"] = f"{nombre_user}@{empresa}.edu.ar"
    user['pwd'] = 'Pass123!'

    return user