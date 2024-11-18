import os
from dotenv import load_dotenv



class Variables():
    def __init__(self) -> None:
        load_dotenv('\Python\config.env')

        self.usuario = os.getenv("USER_MAIL")
        self.password = os.getenv("PASSWORD_MAIL")
        self.destinatario = os.getenv("DESTINATARIO_MAIL")