from Crypto.Hash import HMAC, MD5, SHA256, SHA512, MD2, MD4, SHA384



def _Hash_Encryption(plaintext, key, algo):
    d_algo = {
        'MD5': MD5,
        'MD2': MD2,
        'MD4': MD4,
        'SHA-256': SHA256,
        'SHA-512': SHA512,
        'SHA-384': SHA384
    }
    #h = HMAC.new(key, digestmod= d_algo[algo])
    h = d_algo[algo].new()
    h.update(plaintext)
    return h.hexdigest().upper()





