import marshal
import base64
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    # Clear terminal screen
    clear_screen()
    
    # Load encrypted file
    with open('kejar_id.py', 'r') as f:
        encrypted_code = f.read()
    
    # Execute decrypted code
    exec(encrypted_code)

except FileNotFoundError:
    print(f"[-] Error: kejar_id.py not found")
except Exception as e:
    print(f"[-] Error executing encrypted code: {str(e)}")
finally:
    input("\nPress Enter to exit...")