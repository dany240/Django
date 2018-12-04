
#Codigo Utilizado para Fair user en proyecto final
#Creditos originales para https://code.i-harness.com/es/q/2898a46
from Crypto.Cipher import AES  # pip install pycrypto
import base64


def __Contraseña(LLavePrivada, Mensajeaencriptar, encrypt=True):
    # an AES key must be either 16, 24, or 32 bytes long
    # in this case we make sure the key is 32 bytes long by adding padding and/or slicing if necessary
    Tam = len(LLavePrivada) % 16
    LLavemoificada = LLavePrivada.ljust(len(LLavePrivada) + (16 - Tam))[:32]
    # input strings must be a multiple of 16 in length
    # we achieve this by adding padding if necessary
    Tam = len(Mensajeaencriptar) % 16
    textomodiifcado = Mensajeaencriptar.ljust(len(Mensajeaencriptar) + (16 - Tam))
    cifrar = AES.new(LLavemoificada, AES.MODE_ECB)  # use of ECB mode in enterprise environments is very much frowned upon

    if encrypt:
        return base64.b64encode(cifrar.encrypt(textomodiifcado)).strip()

    return cifrar.decrypt(base64.b64decode(textomodiifcado)).strip()
def Encriptar(valor):
    return __Contraseña('Basededatos',valor,encrypt=True)
def Desencriptar(valor_modificado):
    return __Contraseña('Basededatos',valor_modificado,encrypt=True)