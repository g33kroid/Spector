from ip_generator import generate_range
from pinger import pinger
from nmap_scanner import scanner
from termcolor import cprint
def scan_hosts():
    try:
        input_ip = raw_input("[?] Enter IP [10.10.10.10] or Range [10.0.10.10/24] : ")
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
    return