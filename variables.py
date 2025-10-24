import os
from dotenv import dotenv_values



def leer_variables():
    if os.name == 'nt':
        ruta = 'D:\\Python\\'
    else:
        ruta = '/usr/config/'

    #  Lectura de las variables de entorno en un diccionario
    var_env = dotenv_values(ruta + "config.env")
    
    return var_env