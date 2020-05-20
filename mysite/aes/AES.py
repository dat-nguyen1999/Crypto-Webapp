from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from bitstring import BitArray
import io
from Crypto.Util.Padding import pad, unpad
import os
from Crypto.Hash import MD5



def _AES_Encryption(key_in,plaintxt,mode, iv=None):
    
    dmode = {
        'ECB': AES.MODE_ECB,
        'CBC': AES.MODE_CBC,
        'CFB': AES.MODE_CFB,
        'OFB': AES.MODE_OFB,
        'EAX': AES.MODE_EAX,

    }
    if mode != "EAX":
        if mode == "ECB":
            cipher = AES.new(key_in, dmode[mode])
        else:    
            cipher = AES.new(key_in, dmode[mode], iv =  iv )
        plaintext =  pad(plaintxt,AES.block_size) 
        return cipher.encrypt(plaintext)
    else:
        cipher = AES.new(key_in, dmode[mode], nonce =  iv )
        plaintext =  pad(plaintxt,AES.block_size) 
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        return tag + ciphertext



def _AES_Decryption(key_in,ciphertxt,mode, iv=None):
    
    dmode = {
        'ECB': AES.MODE_ECB,
        'CBC': AES.MODE_CBC,
        'CFB': AES.MODE_CFB,
        'OFB': AES.MODE_OFB,
        'EAX': AES.MODE_EAX,
    }
    if mode != "EAX":
        if mode == "ECB":
            cipher = AES.new(key_in, dmode[mode])
        else:    
            cipher = AES.new(key_in, dmode[mode], iv =  iv )
        pl = cipher.decrypt(ciphertxt)
        plaintxt = unpad(pl,AES.block_size)
        return plaintxt
    else:
        cipher = AES.new(key_in, dmode[mode], nonce =  iv )
        tag = ciphertxt[:16]
        ciphertext = ciphertxt[16:]
        #plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        try:
            plaintxt = cipher.decrypt_and_verify(ciphertext, tag)
            plaintext = unpad(plaintxt, AES.block_size)
            print("The message is authentic!")
            
        except ValueError:
            print("Key incorrect or message corrupted")
        
        return plaintext