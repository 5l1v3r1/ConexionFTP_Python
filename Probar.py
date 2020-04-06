# Importamos librería
from ftplib import FTP

# Variables de Conexión
#servidor = "ftpupload.net";     # Nombre del Dominio
#user = "epiz_25466257";         # Usuario
#password = "PzN8oatetZyxe";     # Contraseña

# Ésta función devolverá un True si la conexión fue exitosa o un False si hubo un error
def TestConexionFTP(server,user,password):
    # Instanciamos FTP
    try:
        test = FTP(servidor);  
        #Logearse
        test.login(user,password);      # UserName #Password
        test.quit();                    # Cierra conexión
        return True;                    # Retorna un True == Conexión Exitosa
    except:
        return False;         

