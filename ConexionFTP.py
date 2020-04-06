from ftplib import FTP

# Variables de conexión
servidor = "ftpupload.net";     # Nombre del Dominio
user = "epiz_25466257";         # Usuario
password = "PzN8oatetZyxe";     # Contraseña

# Ésta función devolverá un True si la conexión fue exitosa o un False si hubo un error
def ConexionTest():
    # Test the Conexión
    try:
        # Instanciamos FTP
        conexion = FTP(servidor);  

        #Logearse
        conexion.login(user,password);      # UserName #Password
        #print("[+] Conexión exitosa");
        return True;                        # Retorna un True == Conexión Exitosa
    except: #Exception as e:
        #print("[-] Error de Conexión "); #+ str(e));
        return False;                       # Retorna un False == Error de conexión
        

print (str(ConexionTest()));

