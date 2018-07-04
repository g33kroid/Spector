from ip_generator import generate_range
from pinger import pinger
from check_priv import getprivs
from termcolor import cprint
from nmap_scanner import scanner
from random_banner import welcome_banner
from db_status import db_status
from sys import exit
from interactive import interactive_mode

welcome_banner()
privs = getprivs()
if(privs == "admin"):
    db_status()
    try:
        input_ip = raw_input("Enter IP [10.10.10.10] or Range [10.0.10.10/24] : ")
    except KeyboardInterrupt:
        cprint("\n[x] Exiting Script",'red')
        cprint(""" 
  ______     ________ 
 |  _ \ \   / /  ____|
 | |_) \ \_/ /| |__   
 |  _ < \   / |  __|  
 | |_) | | |  | |____ 
 |____/  |_|  |______|
                      
        """,'red')
        exit()
    ips = generate_range(input_ip)
    live = pinger(ips)
    scanner(live)
    interactive_mode()
else:
    cprint("[x] Script need root access",'red')

