import socket
import json
from socket_server import PUBLIC_KEY, YOUR_KEY
import lib.generate_key as generate_key
import lib.generate_symmetric_key as generate_symmetric_key



def client_program():

    my_secret = {}
    my_encryption_key = {}


    host = socket.gethostname()
    port = 4001

    client_socket = socket.socket()
    client_socket.connect((host, port))

    messsage = input(" -> ")

    #communication between a client and a server
    while messsage.lower().strip() != 'bye':

        if "encryption_key" in my_encryption_key:
            encrypted_msg = generate_symmetric_key.encrypt_msg(my_encryption_key["encryption_key"], messsage)
            client_socket.send(encrypted_msg) #send encrypted message to the server
        else: 
            #find public key
            if "public_key" in my_secret:
                my_encryption_key = {"encryption_key" : generate_symmetric_key.gen_sym_key().decode("utf-8")}
                encrypted_msg = generate_key.encrypt_msg(my_encryption_key["encryption_key"], my_secret["public_key"])  #encrypt message 
                client_socket.send(json.dumps({YOUR_KEY: encrypted_msg}).encode()) #send encrypted message to the server
                my_secret = {}
            else:
                client_socket.send(messsage.encode())  #message in plain text if no public key


        data = client_socket.recv(1024).decode() #receive data from server

        #if data contains public key, it is loaded into my_secret
        if "public_key" in data:  
            my_secret = json.loads(data)

        try:
            temp = data
            data = generate_symmetric_key.decrypt_msg(my_encryption_key["encryption_key"], data)
            print('###ENCRYPTED MSG FROM SERVER: ' + temp) #print message received from server
        except:
            data = data


        print('Received from server: ' + data) #print message received from server
        messsage = input(" -> ") 

    client_socket.close()


if __name__ == "__main__":
    client_program()


