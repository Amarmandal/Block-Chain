#Fernet is used to generate the key or use random key generator
#Importing the fernet library
from cryptography.fernet import Fernet

def gen_sym_key():
    #Generating a encryption key using library
    key = Fernet.generate_key()

    return key
    # Instanciate the class with the encryption key 

def encrypt_msg(encryption_key, message):
    fernet = Fernet(encryption_key)
    #Encrypting the string using fernet. 
    #First, need to encode to byte string before encryption
    encryptMessage = fernet.encrypt(message.encode())

    return encryptMessage

def decrypt_msg(key, msg):
    fernet = Fernet(key)
    decryptMessage = fernet.decrypt(msg).decode()

    return decryptMessage

