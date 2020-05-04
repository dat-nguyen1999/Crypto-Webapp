from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from bitstring import BitArray
import io
from Crypto.Util.Padding import pad, unpad
import os
from Crypto.Hash import MD5



cur_path = os.path.dirname(__file__)


#key1 = get_random_bytes(8)
key1 = b'12345678'

# keyfile1 =  os.path.relpath('.\\Pdf\\key1.pdf', cur_path)

# plainfile1 = os.path.relpath('.\\Pdf\\assignment1.pdf', cur_path)

#cipherfile1 = os.path.relpath('.\\Pdf\\cipherfile1.pdf', cur_path)

# _plainfile1 = os.path.relpath('.\\Pdf\\_assignment1.pdf', cur_path)

# if os.path.exists(cipherfile1):
#     os.remove(cipherfile1)
# if os.path.exists(_plainfile1):
#     os.remove(_plainfile1)

# with io.open(keyfile1,'wb') as f:
#         f.write(key1)


def Encryption(key,plainfile):

    iv = get_random_bytes(8)
    cipher = DES.new(key1,DES.MODE_CBC, iv = iv)
    
    pathlist = plainfile.split("\\")

    pathlist[-1] = "Encrypted_" + pathlist[-1]

    cipherfile1 = os.path.relpath('\\'.join(pathlist), cur_path)
    
    if os.path.exists(cipherfile1):
        os.remove(cipherfile1)

    with io.open(plainfile,'rb') as plain, io.open(cipherfile1,'wb') as cip:
        plaintext =  pad(plain.read(),DES.block_size)  
        ciphertext = cipher.iv + cipher.encrypt(plaintext)
        cip.write(ciphertext)
    print("Encrypted!!")
    
    return "\\".join(pathlist)

def Decryption(key,cipherfile):

    pathlist = cipherfile.split("\\")

    pathlist[-1] = "Decrypted_" + pathlist[-1]

    _plainfile1 = os.path.relpath('\\'.join(pathlist), cur_path)

    if os.path.exists(_plainfile1):
        os.remove(_plainfile1)

    with io.open (_plainfile1,'a+b') as _plain, io.open(cipherfile,'rb') as cip:
        iv = cip.read(8)
        cipherdata = cip.read()
        cipher = DES.new(key1, DES.MODE_CBC, iv = iv )
        _plaintext = unpad(cipher.decrypt(cipherdata),DES.block_size)
        _plain.write(_plaintext)
    print("Decrypted!!")

    return '\\'.join(pathlist)


# with io.open(planfile1,'rb') as plan:
#     with io.open(cipherfile1,'a+b') as cip:
#         a = []
#         byte = plan.read(8)
#         a.append(byte)
#         while byte != b'':
#             cip.write(cipher.encrypt(pad(byte,BLOCK_SIZE)))
#             byte = plan.read(8)
#             if byte == b'': break
#             a.append(byte)
#         print("Encrypted!!!")

# with io.open(cipherfile1,'rb') as cip:
#     with io.open("_" + planfile1,'a+b') as _plan:
#         byte = cip.read(8)
#         b = []
#         b.append(byte) 
#         while byte != b'':
#             # _plan.write(cipher.decrypt(unpad(byte,BLOCK_SIZE)))
#             byte = cip.read(8)
#             if byte == b'': break
#             b.append(byte) 
#         print("Decrypted!!!")
def check_integrity(origin_plainfile, output_plainfile):

    h = MD5.new()
    _h = MD5.new()
    with io.open(origin_plainfile,'rb') as plain, io.open(output_plainfile,'rb') as _plain:
        h.update(plain.read())
        print("Hash value from original file: ".ljust(38) + h.hexdigest())
        _h.update(_plain.read())
        print("Hash value from output of decryption: ".ljust(38) + _h.hexdigest())
    return h.hexdigest() == _h.hexdigest()

# cipher = DES.new(key1,DES.MODE_CFB)
# ciphertext = cipher.encrypt(bytes("tiendat",'utf-8'))
# print(ciphertext)

# fi = open("key.txt","rb")
# s = []
# try:
#     byte = fi.read(8)
#     s.append(byte)
#     # c = BitArray(byte)
#     # print(c.bin)
#     # print(len(c))

#     while byte != b'':
#         byte = fi.read(8)
#         s.append(byte)
# finally:
#     fi.close()
# print(s)

# c = BitArray(key)
# print(c.bin)
# print(len("0111100110101101110010110000100101001101101010010001010001011110"))

# with io.open("plc.txt",'rb') as f:
    
# process Unicode text
# with io.open("plc.txt",'a+',encoding='utf8') as f:
#     f.write()
# x = b'sinh tu dau den chet di ve dau'
# x = pad(x,BLOCK_SIZE)
# print(x)
# y = cipher.encrypt(x)
# print(y)
# z = unpad(cipher.decrypt(y),BLOCK_SIZE)
# print(z)
# x = unpad(x,BLOCK_SIZE)
# print(x)


# plainfile1 = os.path.relpath('.\\Office\\power point.pptx', cur_path)


# cipherfile1 = Encryption(key1,plainfile1)



# _plainfile1 = Decryption(key1,cipherfile1)


# print( "is integrity: " + str(check_integrity(plainfile1, _plainfile1)))

def _DES_Encryption(key,plaintxt,mode, iv=None):
    
    dmode = {
        'ECB': DES.MODE_ECB,
        'CBC': DES.MODE_CBC,
        'CFB': DES.MODE_CFB,
        'OFB': DES.MODE_OFB
    }

    if mode == 'ECB':
        cipher = DES.new(key,dmode[mode])

    else:
        cipher = DES.new(key,dmode[mode], iv= iv)
    
    plaintext =  pad(plaintxt,DES.block_size) 
    return cipher.encrypt(plaintext)

def _DES_Decryption(key,ciphertxt,mode, iv=None):
    
    dmode = {
        'ECB': DES.MODE_ECB,
        'CBC': DES.MODE_CBC,
        'CFB': DES.MODE_CFB,
        'OFB': DES.MODE_OFB
    }

    if mode == 'ECB':
        cipher = DES.new(key,dmode[mode])

    else:
        cipher = DES.new(key,dmode[mode], iv= iv)
    
    plaintxt =  unpad(cipher.decrypt(ciphertxt),DES.block_size)
    return plaintxt
