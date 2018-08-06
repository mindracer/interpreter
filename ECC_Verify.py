import hashlib
from ecdsa import SigningKey, VerifyingKey, NIST192p
import binascii
keypath = 'C:/Users/Mindracer/Documents/keys/'

def keyRead():
    with open(keypath + 'private.der', 'rb') as f:
        sk = SigningKey.from_der(f.read())
    with open(keypath + 'public.der', 'rb') as f:
        vk = VerifyingKey.from_der(f.read())
    return [sk,vk]

[sk,vk]=keyRead()

path = 'C:/Users/Mindracer/Documents/'

filename = "VID_20161206_102730.mp4" # input("name of file: ")
file=path + filename

def Verify():
    i=0
    with open(path + "/" + filename, 'r') as fx:
        for line in fx.readlines():
            md5_value, signature= line.split()
            if( vk.verify(bytes.fromhex(signature), bytes.fromhex(md5_value))):
                print("good line " + str(i))
                i=i+1
            else: print("Bad Signature!")


#Verify()

# with open(path + "/" + filename, 'r') as fx:
#     md5_value, signature = fx.readline().split()
#
#     print(md5_value,signature)
#    # if (vk.verify(signature, bytes(md5_value).decode())):
#    #     print("good line")
#     print(signature)

Verify()
