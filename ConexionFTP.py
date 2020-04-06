from ftplib import FTP

# Variables de conexión
servidor = "ftpupload.netf";     # Dominio   // DominioName.com
user = "epiz_25466257";
password = "PzN8oatetZyxe";

#def ConexionTest():
# Test the Conection
try:
    # Instanciamos FTP
    conexion = FTP(servidor);  

    #Logearse
    conexion.login(user,password);      # UserName #Password
    print("[+] Conexión exitosa");
except Exception as e:
     print("[-] Error de Conexión"+ str(e));
        

#ConexionTest();

