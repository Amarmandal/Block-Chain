import socket
import lib.prime_generator as prime_generator
import lib.generate_key as generate_key
import lib.generate_symmetric_key as generate_symmetric_key
import json

PUBLIC_KEY = '!PUBLIC_KEY'
YOUR_KEY = 'YOUR_KEY'

def server_program():
    pub_pvt_key = {}
    my_decryption_key = {}

    host = socket.gethostname()
    port = 4001

    server_socket = socket.socket() #socket object

    server_socket.bind((host, port))

    server_socket.listen(2)

    conn, address = server_socket.accept()

    print("Connection from: " + str(address))

    while True:

        msg_from_client  = conn.recv(1024).decode()
        
        if not msg_from_client:
            break

        if msg_from_client == PUBLIC_KEY:  #if client requests for public key
            p1 = prime_generator.generate_random_prime(100, 200)
            p2 = prime_generator.generate_random_prime(100, 200)
            
            if p1 != p2:
                #public/private key pair is created using the generated primes
                pub_pvt_key = generate_key.generate_key(p1, p2) 
            else: 
                #if p1 and p2 are same, a new prime number is generated
                p2 = prime_generator.generate_random_prime(100, 200) 

            #send public key to the connected user
            conn.send(json.dumps({"public_key": pub_pvt_key["public_key"]}).encode())
            continue

        if YOUR_KEY in my_decryption_key:
            print("#ENCRYPTED msg received from client: ", msg_from_client)
            msg_from_client = generate_symmetric_key.decrypt_msg(my_decryption_key[YOUR_KEY], msg_from_client)
            print("From connected user: " + str(msg_from_client))
            data = input(' -> ')
            data = generate_symmetric_key.encrypt_msg(my_decryption_key[YOUR_KEY], data)
            conn.send(data)
        else:
            #check private key exists in a dictionary containing a public/private key pair 
            if "private_key" in pub_pvt_key:
                #message received from the client is decrypted using the private key
                msg_from_client = json.loads(msg_from_client)[YOUR_KEY]
                msg_from_client = generate_key.decrypt_msg(msg_from_client, pub_pvt_key["private_key"]) 
                my_decryption_key = {YOUR_KEY: msg_from_client}
                pub_pvt_key = {}
    
            print("From connected user: " + msg_from_client)
            data = input(' -> ')
            conn.send(data.encode())

    conn.close()


if __name__ == "__main__":
    server_program()


