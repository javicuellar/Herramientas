import streamlit as st

# Librerias comunes
from Herramientas.variables import leer_variables
config = leer_variables()




# Configuración de la conexión a la base de datos MySQL
def Conexion_mysql(esquema):
    return st.connection("sql", dialect="mysql",
                                host=config['HOST'],
                                port=config['PUERTO'],
                                username=config['USUARIO'],
                                password=config['PASSWORD'],
                                database=esquema)
