# run.py
import os
import sys
from colorama import init, Fore, Style

init()

def run_encrypted():
    try:
        if not os.path.exists('kejar_id.py'):
            sys.exit(1)
            
        print(f"{Fore.CYAN}[*] Starting script execution...{Style.RESET_ALL}")
        
        if 'kejar_id' in sys.modules:
            del sys.modules['kejar_id']
            
        import kejar_id
        
        if hasattr(kejar_id, 'main'):
            print(f"{Fore.CYAN}[*] Executing main function...{Style.RESET_ALL}")
            kejar_id.main()
        elif hasattr(kejar_id, 'run'):
            print(f"{Fore.CYAN}[*] Executing run function...{Style.RESET_ALL}")
            kejar_id.run()
            
        print(f"{Fore.GREEN}[+] Script executed successfully{Style.RESET_ALL}")
            
    except ImportError as ie:
        print(f"{Fore.RED}[-] Import error: {str(ie)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Python path: {sys.path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Runtime error: {str(e)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Error details: {type(e).__name__}{Style.RESET_ALL}")

if __name__ == "__main__":
    run_encrypted()