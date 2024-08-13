from cryptography.fernet import Fernet

def genera_clave():
    clave=Fernet.generate_key()
    with open('clave.txt', 'wb') as archivo_clave:
        archivo_clave.write(clave)

############################################################################################

def carga_clave():
    return open('clave.txt', 'rb').read()

def encriptar(nom_archivo,clave):
    f=Fernet(clave)
    with open(nom_archivo, 'rb') as file:
        archivo_info=file.read()
    encrypted_data=f.encrypt(archivo_info)
    with open(nom_archivo, 'wb') as file:
        file.write(encrypted_data)

def desencriptar(nom_archivo,clave):
    f=Fernet(clave)
    with open(nom_archivo, 'rb') as file:
        encrypted_data=file.read()
    decrypted_data=f.decrypt(encrypted_data)
    with open(nom_archivo, 'wb') as file:
        file.write(decrypted_data)

############################################################################################

