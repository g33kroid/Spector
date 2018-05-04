from ip_generator import generate_range
from pinger import pinger
from check_priv import getprivs
from termcolor import cprint

privs = getprivs()
if(privs == "admin"):
    input_ip = raw_input("Enter IP [10.10.10.10] or Range [10.0.10.10/24] : ")
    ips = generate_range(input_ip)
    live = pinger(ips)
else:
    cprint("[x] Script need root access",'red')

