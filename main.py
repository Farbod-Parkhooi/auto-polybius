from modules import script
from colorama import init, Fore, Style
reset = Fore.RESET + Style.RESET_ALL
init()
try:
    dir = input(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.GREEN}For decode a text write '{Fore.YELLOW}D{Fore.GREEN}', and for encode a text wirte '{Fore.YELLOW}E{Fore.GREEN}': {reset}").lower()
    if dir == "d": 
        text = input(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.GREEN}Write the text to decode: {reset}")
        out = script.decode(text)
        print(out)
    elif dir == "e":
        text = input(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.GREEN}Write the text to encode: {reset}")
        out = script.encode(text)
        print(out)
    else:
        print("Invalid Input.")
except KeyboardInterrupt: exit(f"\n\n {Fore.CYAN}Good Luck{reset} \n\n")
except: exit(f"\n\n {Fore.RED}Unknown error{reset} \n\n")