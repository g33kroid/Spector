from ip_generator import generate_range
from pinger import pinger
from check_priv import getprivs
from termcolor import cprint
from nmap_scanner import scanner
from random_banner import welcome_banner
from db_status import db_status
from sys import exit
from interactive import interactive_mode
from loading import loading 
# from update import update
loading()
welcome_banner()
privs = getprivs()
if(privs == "admin"):
    db_status()
    # update()
    interactive_mode()
else:
    cprint("[x] Script need root access",'red')

