from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP

def generateKeyPair(length):
    privatekey = RSA.generate(length)
    publickey = privatekey.publickey()

    return {
        'publickey' : publickey.export_key("PEM"),
        'privatekey': privatekey.export_key("PEM")
    }
    
def encrypt(key_in,plt):
    while True:
        try:
            key = RSA.import_key(key_in)
            break
        except ValueError as VE:
            return 'Caught this error: ' + repr(VE)
    cipher = PKCS1_v1_5.new(key)
   
    ciphertext = cipher.encrypt(plt)
    return ciphertext

def decrypt(key_in,cpt ):
    while True:
        try:
            key = RSA.import_key(key_in)
            break
        except ValueError as VE:
            return 'Caught this error: ' + repr(VE)
    cipher = PKCS1_v1_5.new(key)
   
    plaintext = cipher.decrypt(cpt, "ERROR_DE!")
    return plaintext