import random
# from cryptography.fernet import Fernet

#Euclidean algorithm to find the gcd(x, y)
def get_gcd(a, b): 
  largest_num = a if a > b else b
  smallest_num = b if b < a else a

  temp_a = largest_num
  temp_b = smallest_num
  temp_rem = 0

  while (temp_b != 0):
    temp_rem = temp_a % temp_b
    temp_a = temp_b
    temp_b = temp_rem

  return temp_a

#modular inverse 
def mod_inverse(e, z):
  d = 2
  while (d < z):
    if (e * d) % z == 1:
      return d
    else:
      d += 1
  
#algorithm to generate a public-private key pair for use in an RSA encryption system.
def generate_key(p,q):
  n = p * q
  z = (p-1) *( q-1)
  e = random.randint(2, z-1)  #random number "e" between 2 and "z-1"

  while get_gcd(e, z) != 1:   #continue till gcd is 1
    e = random.randint(2, z-1)
    
  d = mod_inverse(e, z)
      
  return {"public_key": (n, e), "private_key": (p, q, d)}

#algorithm to encrypt a message using an RSA encryption system
def encrypt_msg(message, public_key):
  n, e = public_key[0], public_key[1]
  
  encrypted_msg = ''
  for char in message:
    encrypted_msg += chr(pow(ord(char), e, n))

  return encrypted_msg

#decrypt a message encrypted using an RSA encryption system
def decrypt_msg(cipher_text, private_key):
  p, q, d = private_key[0], private_key[1], private_key[2]
  n = p * q
  message = ''

  #calculate the remainder when divided by "n" using the "pow" function with the modulo operator, and converts the result back to a character using the "chr" function.
  for ch in cipher_text:  
    message += chr(pow(ord(ch), d, n))

  return message


if __name__ == "__main__":
  my_key = generate_key(151, 157)
  print(my_key)


  