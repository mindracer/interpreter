import hashlib

import rsa
#rsa加密
def rsaEncrypt(str):
    # Generate public key, private key
    (pubkey, privkey) = rsa.newkeys(512)
    #明文编码格式
    content = str.encode('utf-8')
    #公钥加密
    crypto = rsa.encrypt(content,pubkey)
    print(pubkey)
    print(privkey)
    return (crypto,privkey)


#rsa解密
def rsaDecrypt(str,pk):
    #私钥解密
    content = rsa.decrypt(str,pk)
    con=content.decode('utf-8')
    return con


word = "Life is about experience and how to improve it."  # Document text to be stored.
word = word.encode("utf-8")
SHA = hashlib.sha1(word).hexdigest()
print("SHA: ", SHA)


(a,b) = rsaEncrypt(SHA)

print('加密后密文：')
print("size: ", len(a), "\n", a)
content = rsaDecrypt(a,b)
print('解密后明文：')
print("size: ", len(content), "\n", content)


