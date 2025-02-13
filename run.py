from cryptography.fernet import Fernet
import base64
import sys
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import importlib.util
from colorama import init, Fore, Style
import hashlib
import platform

def get_secure_salt():
    components = [
        bytes([107, 101, 106, 97, 114]), 
        str(os.getenv('NUMBER_OF_PROCESSORS', '')).encode(),
        str(os.getenv('PROCESSOR_IDENTIFIER', '')).encode(),
        platform.node().encode()
    ]
    return hashlib.pbkdf2_hmac(
        'sha256', 
        b''.join(components), 
        hashlib.sha256(platform.machine().encode()).digest(),
        150000
    )[:16]

def generate_key(password):
    salt = get_secure_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def get_secure_key():
    key_components = [
        bytes([98, 111, 116, 75, 101, 106, 97, 114]),
        bytes([73, 68, 50, 48, 50, 53, 33, 64]),       
        bytes([35, 36, 37, 94, 38, 42, 40, 41])       
    ]
    
    hw_id = hashlib.md5(''.join([
        os.name,
        os.getenv('COMPUTERNAME', ''),
        os.getenv('USERNAME', '')
    ]).encode()).hexdigest()
    
    combined = b''.join(key_components) + hw_id.encode()
    return hashlib.sha256(combined).digest()[:32]

def decrypt_and_run():
    try:
        init()
        
        key = base64.urlsafe_b64encode(get_secure_key())
        f = Fernet(key)
        
        with open('encrypted_kejar.bin', 'rb') as file:
            encrypted_data = file.read()
        
        decrypted_code = f.decrypt(encrypted_data)
        
        spec = importlib.util.spec_from_loader('kejar_bot', loader=None)
        module = importlib.util.module_from_spec(spec)
        
        exec(decrypted_code, module.__dict__)
        
        if hasattr(module, 'main'):
            module.main()
        else:
            raise ImportError("Invalid module structure")
            
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    decrypt_and_run()
