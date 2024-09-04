from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import json

def encrypt_func(a, key, iv):
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    if isinstance(a, str):
        data = a.encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    elif isinstance(a, dict):
        data = json.dumps(a).encode('utf-8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return encrypted_data.hex()

# Example usage
key = "bFQHVOUNt36YEE8g"
iv = "pqrstuvwxyz{|}~"
data_string = "{"dataObj":{"username":"admin","password":"Ae9HE"},"ajaxmethod":"DO_WEB_LOGIN","sessionid":"bFQHVOUNt36YEE8g16DXuPs86R6908Rp"}"
encrypted_data_string = encrypt_func(data_string, key, iv)
print(encrypted_data_string)
