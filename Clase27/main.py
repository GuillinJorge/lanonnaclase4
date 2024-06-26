from modules import get_user
from modules import add_email_pwd
from modules import save_user_db
from modules import add_custom_msg
from modules import send_email


def main():
    
    database:list = []
    
    user = get_user()
    
    user = add_email_pwd(user)
    
    option:str = input("Desea guardar al usuario? \n>> 'y' por defecto \n")
    
    option:str = None if option == '' else option
    
    save_user_db(user=user, option=option, database=database)
    
    
    custom_msg:str = input("Agrega el mensaje para el nuevo usuario")
    
    user = add_custom_msg(user, custom_msg)
        
    send_email(user)
    
    print(database)
    
if __name__ == "__main__":
    main()
    
