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
def OpenFile():
    # CREA UN ARCHIVO EN EL SERVIDOR
    # Argument[0] = Nombre del Archivo, ejemplo "file.txt"
    # Argument[1] = -rw-r--r-- drwxr-xr-x
    #               w = write
    #               r = read           
    try:
        file = open("htdocs/Prueba servidor FTP.txt", "w");
    
        # éste método escribe dentro del archivo 
        file.writelines("Este exto aparecerá dentro de ese archivo1");
        #file.writelines("Este exto aparecerá dentro de ese archivo2");
        #file.write("Ver si estó aparece y en donde aparece wee");
        file.close();
        return True;
    except:
        return False;




if ConexionTest():      # Si la conexión fue exitosa, continuar
    conexion = FTP(servidor);  
    #Logearse
    conexion.login(user,password); 
    # Muestra un listado de los archivos
    #conexion.retrlines("LIST");
    
    if(OpenFile()):
        print("el archivo fue creado exitosamente");
    else:
        print("Erro al crear el archivo");





else:
    print("Hubo un error en su conexión FTP, usted no puede continuar");

