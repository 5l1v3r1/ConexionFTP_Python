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
        test = FTP(servidor);  
        #Logearse
        test.login(user,password);      # UserName #Password
        test.quit();                    # Cierra conexión
        return True;                        # Retorna un True == Conexión Exitosa
    except:
        return False;                       # Retorna un False == Error de conexión

# Crea un fichero
def CreateFile():
    # CREA UN ARCHIVO EN EL SERVIDOR
    # Argument[0] = Nombre del Archivo, ejemplo "file.txt"
    # Argument[1] = -rw-r--r-- drwxr-xr-x
    #               w = write
    #               r = read    
    #               rb = ¿?       
    try:
        conexion = FTP(servidor);  
        #Logearse
        conexion.login(user,password);      # UserName #Password
        conexion.retrlines("LIST");
        file = open("FTP.txt", "w");
    
        # éste método escribe dentro del archivo 
        file.writelines("Este texto aparecerá dentro de ese archivo1");
        file.writelines("Este exto aparecerá dentro de ese archivo2");
        file.write("Ver si estó aparece y en donde aparece wee");
        file.close();
        
        
        # Subir el archivo a la nube
        fileR = open("FTP.txt", "rb");
        conexion.storbinary("STOR FTP.txt",fileR);
        fileR.close();
        
        conexion.quit();

        return True;
    except:
        return False;


# Descarga un archivo desde FTP y lo guarda en una direción especifica
#def DownloadFileFTP():

try:
    conexion = FTP(servidor);
    conexion.login(user,password);      # UserName #Password
    conexion.cwd("htdocs");
    conexion.retrlines("LIST");
    # Descaargar el archivo a la nube
    fileR = open("FTP.txt", "wb");
    # Si se desea, puede cambiar de nombre
    conexion.retrbinary("RETR FTP.txt",fileR.write);
    fileR.close();
    conexion.quit();
    #return True;
    print("Exito");
except:
    #return False;
    print("Error");




#print("El resultado fue: "+ str(DownloadFileFTP()));


    """
    conexion = FTP(servidor);  
    #Logearse
    conexion.login(user,password); 
    # Muestra un listado de los archivos
    conexion.cwd("htdocs")
    conexion.retrlines("LIST");

    if(CreateFile()):
        CreateFile();
        print("el archivo fue creado exitosamente");
    else:
        print("Erro al crear el archivo");

    """