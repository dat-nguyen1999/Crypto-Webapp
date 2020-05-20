from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from bitstring import BitArray
import io
from Crypto.Util.Padding import pad, unpad
import os
from Crypto.Hash import MD5



def _TDES_Encryption(key_in,plaintxt,mode, iv=None):
    
    dmode = {
        'ECB': DES3.MODE_ECB,
        'CBC': DES3.MODE_CBC,
        'CFB': DES3.MODE_CFB,
        'OFB': DES3.MODE_OFB
    }
    while True:
        try:
            key = DES3.adjust_key_parity(key_in)
            break
        except ValueError as VE:
            return 'Caught this error: ' + repr(VE)
        #key = DES3.adjust_key_parity(key_in)
    if mode == 'ECB':
        cipher = DES3.new(key,dmode[mode])

    else:
        cipher = DES3.new(key,dmode[mode], iv= iv)
    
    plaintext =  pad(plaintxt,DES3.block_size)
    #print(mode)
    #print(key)

    #print(plaintext)
    return cipher.encrypt(plaintext)

def _TDES_Decryption(key_in,ciphertxt,mode, iv=None):
    
    dmode = {
        'ECB': DES3.MODE_ECB,
        'CBC': DES3.MODE_CBC,
        'CFB': DES3.MODE_CFB,
        'OFB': DES3.MODE_OFB
    }
    while True:
        try:
            key = DES3.adjust_key_parity(key_in)
            break
        except ValueError as VE:
            return 'Caught this error: ' + repr(VE)

    if mode == 'ECB':
        cipher = DES3.new(key,dmode[mode])

    else:
        cipher = DES3.new(key,dmode[mode], iv= iv)
    
    pl = cipher.decrypt(ciphertxt)
    plaintxt = unpad(pl,DES3.block_size)
    #plaintxt =  unpad(cipher.decrypt(ciphertxt),DES3.block_size)
    return plaintxt