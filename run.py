# run.py
import os
import sys
from colorama import init, Fore, Style

init()

def run_encrypted():
    try:
        # Check if file exists and is readable
        if not os.path.exists('enc_kejar.py'):
            print(f"{Fore.RED}[-] Error: enc_kejar.py file not found{Style.RESET_ALL}")
            sys.exit(1)
            
        print(f"{Fore.CYAN}[*] Starting script execution...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Attempting to import enc_kejar.py...{Style.RESET_ALL}")
        
        # Force reload if already imported
        if 'enc_kejar' in sys.modules:
            del sys.modules['enc_kejar']
            
        try:
            # Import with more detailed error catching
            import enc_kejar
            print(f"{Fore.GREEN}[+] Successfully imported enc_kejar.py{Style.RESET_ALL}")
            
        except SyntaxError as se:
            print(f"{Fore.RED}[-] Syntax error in enc_kejar.py: {str(se)}{Style.RESET_ALL}")
            return
        except IndentationError as ie:
            print(f"{Fore.RED}[-] Indentation error in enc_kejar.py: {str(ie)}{Style.RESET_ALL}")
            return
            
        # Check for main function
        if hasattr(enc_kejar, 'main'):
            print(f"{Fore.CYAN}[*] Executing main function...{Style.RESET_ALL}")
            enc_kejar.main()
        elif hasattr(enc_kejar, 'run'):
            print(f"{Fore.CYAN}[*] Executing run function...{Style.RESET_ALL}")
            enc_kejar.run()
        else:
            print(f"{Fore.RED}[-] No main() or run() function found in enc_kejar.py{Style.RESET_ALL}")
            
    except ImportError as ie:
        print(f"{Fore.RED}[-] Import error: {str(ie)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Python path: {sys.path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Runtime error: {str(e)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Error details: {type(e).__name__}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Error line: {sys.exc_info()[2].tb_lineno}{Style.RESET_ALL}")

if __name__ == "__main__":
    run_encrypted()