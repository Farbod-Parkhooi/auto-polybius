"""
https://www.github.com/Unknow-per/auto-polybius
Code wrote by Unknown Person (https://www.github.com/unknow-per || https://www.github.com/tik-ten)
For suport please star this repo :)
"""
from modules import script
from colorama import init, Fore, Style
from random import randint
from os import system
from platform import uname
reset = Fore.RESET + Style.RESET_ALL
init()
def clear():
    plat = uname()[0].lower()
    if plat.startswith("win"): system("cls")
    else: system("clear")
def random_banner():
    banners = ["""
 ____    _       _____    ____            ____    ____    _      ___  _   ____    _    _       ____ 
/  _ \  / \ /\  /__ __\  /  _ \          /  __\  /  _ \  / \     \  \//  /  __\  / \  / \ /\  / ___\
| / \|  | | ||    / \    | / \|  _____   |  \/|  | / \|  | |      \  /   | | //  | |  | | ||  |    \
| |-||  | \_/|    | |    | \_/|  \____\  |  __/  | \_/|  | |_/\   / /    | |_\\  | |  | \_/|  \___ |
\_/ \|  \____/    \_/    \____/          \_/     \____/  \____/  /_/     \____/  \_/  \____/  \____/
                                                                                                    
""", """
   (                *   )   ( /(          )\ )   ( /(    )\ )    ( /(     (    )\ )           )\ )  
   )\         (   ` )  /(   )\())        (()/(   )\())  (()/(    )\())  ( )\  (()/(      (   (()/(  
((((_)(       )\   ( )(_)) ((_)\    ___   /(_)) ((_)\    /(_))  ((_)\   )((_)  /(_))     )\   /(_)) 
 )\ _ )\   _ ((_) (_(_())    ((_)  |___| (_))     ((_)  (_))   __ ((_) ((_)_  (_))    _ ((_) (_))   
 (_)_\(_) | | | | |_   _|   / _ \        | _ \   / _ \  | |    \ \ / /  | _ ) |_ _|  | | | | / __|  
  / _ \   | |_| |   | |    | (_) |       |  _/  | (_) | | |__   \ V /   | _ \  | |   | |_| | \__ \  
 /_/ \_\   \___/    |_|     \___/        |_|     \___/  |____|   |_|    |___/ |___|   \___/  |___/  
"""]
    clear()
    rand = randint(0, (len(banners)-1))
    print(Fore.CYAN + banners[rand])
def get_info():
    try:
        dir = input(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.GREEN}For decode a text write '{Fore.YELLOW}D{Fore.GREEN}', and for encode a text wirte '{Fore.YELLOW}E{Fore.GREEN}': {reset}").lower()
        if dir == "d": 
            text = input(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.GREEN}Write the text to decode: {reset}")
            out = script.decode(text)
            clear()
            random_banner()
            print(f"{Fore.GREEN}[{Fore.YELLOW}!{Fore.GREEN}] The Decoded Sentences Is: '{out}'")
        elif dir == "e":
            text = input(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.GREEN}Write the text to encode: {reset}")
            out = script.encode(text)
            clear()
            random_banner()
            print(f"{Fore.GREEN}[{Fore.YELLOW}!{Fore.GREEN}] The Encoded Sentences Is: '{out}'")
        else:
            print("Invalid Input.")
    except KeyboardInterrupt: exit(f"\n\n {Fore.CYAN}Good Luck{reset} \n\n")
    except: exit(f"\n\n {Fore.RED}Unknown error{reset} \n\n")
