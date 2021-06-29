from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad


class AESCrypt:
    @staticmethod
    def encrypt(raw: bytes, key: bytes):
        cipher = AES.new(key, AES.MODE_CBC)
        return cipher.iv + cipher.encrypt(pad(raw, AES.block_size))

    @staticmethod
    def decrypt(cipher: bytes, key: bytes):
        iv = cipher[:16]
        text = AES.new(key, AES.MODE_CBC, iv)
        return unpad(text.decrypt(cipher[16:]), AES.block_size)
