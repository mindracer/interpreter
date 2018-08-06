from datetime import datetime
import json
import ecdsa
import os
import hashlib
from ecdsa import SigningKey, VerifyingKey, NIST192p

keypath = 'C:/Users/Mindracer/Documents/keys/'
def keyCreate():
    sk = SigningKey.generate(curve=NIST192p)
    vk = sk.get_verifying_key()
    with open(keypath + 'private.der', 'wb+') as f:
        f.write(sk.to_der())
    with open(keypath + 'public.der', 'wb+') as f:
        f.write(vk.to_der())

def keyRead():
    with open(keypath + 'private.der', 'rb') as f:
        sk = SigningKey.from_der(f.read())
    with open(keypath + 'public.der', 'rb') as f:
        vk = VerifyingKey.from_der(f.read())
    return [sk,vk]

path = 'C:/Users/Mindracer/Documents/'


filename = "VID_20161206_102730.mp4" # input("name of file: ")

file=path + filename


def fileMD5sign(fileMd5, blockSize):
    with open(path + "/" + filename + ".md5", 'w') as fx:
        with open(fileMd5, 'rb') as f:
            while True:
                data = f.read(blockSize)
                md5_value = hashlib.md5()
                md5_value.update(data)
                MD5HexEncode = md5_value.hexdigest().encode("utf-8")
                signature = sk.sign(MD5HexEncode)
                fx.write(MD5HexEncode.hex() + " " + signature.hex() + "\n" ) # sign the MD5
                if not data:
                    break
    return True


[sk,vk]=keyRead()

fileMD5sign(file, 4194304)