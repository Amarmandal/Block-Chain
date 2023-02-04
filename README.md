# Running the Server Program

## Requirements

- socket
- prime_generator
- generate_key
- generate_symmetric_key
- json

To install the required packages, run the following command in your terminal:

`pip install -r requirements.txt`

# Running the Code

1. Open your terminal and navigate to the folder where the file is saved.
2. Then run `python socket_server.py`

# Running the Client Code

1. Open your terminal and navigate to the folder where the file is saved.
2. Then run `python socket_client.py`

# From the client Terminal

1. Type `!PUBLIC_KEY` to get server public key
2. Server will send back the public key
3. Type anything to send **secret key** that is encrypted using server public key.
4. Server receive the **secret key**
5. From this point on, your msg will be end to end encrypted
