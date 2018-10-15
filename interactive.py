# This Module allow user to interact with DB and Tool
from termcolor import cprint
from sys import exit 
from hosts import get_all_scanned_hosts
from targets_database import save_scan
from hosts import get_ports
from scan_host import scan_hosts
from nikto import nikto_scan
import socket
def interactive_mode():
    try:
        cprint("[?] What do you want to do next ? (help) to show commands",'yellow')
        cmd = raw_input("sp3ctor > ")
        while(cmd !="exit"):
            if(cmd.lower() == "help"):
                cprint("[?] Showing Command list \n[-] scan\n[-] hosts\n[-] update\n[-] exploit\n[-] exit",'white')   
            elif(cmd.lower() == "scan"):
                cprint("[?] Enumeration Tools:\n[-] NMAP\n[-] NIKTO\n[-] WPSCAN\n[-] Exit",'white')
                cmd = raw_input("sp3ctor/scan > ")
                while(cmd.lower() != "back"):
                    if(cmd.lower() == "nmap"):
                        scan_hosts()
                    elif(cmd.lower() == "nikto"):
                        ip = raw_input("Enter IP of host [Single IP/Hostname] : ")
                        port = int(raw_input("Enter the Port Running the Service [Single Port] : "))
                        service = raw_input("Enter the Service type (http/https) : ")
                        nikto_scan(service,ip,port)
                    else:
                        cprint("[x] Under Development")
                    cmd = raw_input("sp3ctor/scan > ")                    
            elif(cmd.lower() == 'hosts'): # Read all the Hosts in DB you can add push JSONs for IPs
                cprint("---------------------Scanned Host IPs-------------------",'white')
                get_all_scanned_hosts()
                cmd = raw_input("sp3ctor/hosts > ")
                while(cmd.lower() !="back"):
                    if(cmd.lower() == "help"):
                        cprint("[-] get_host_data\n[-] add_data",'white')
                    elif(cmd.lower() == "back"):
                        break
                    elif(cmd.lower() == "get_host_data"):
                        get_ports()
                    elif(cmd.lower() == "add_data"):
                        doc_name = raw_input("sp3ctor/hosts > Enter Document Name : ")
                        target_ip = raw_input("sp3ctor/hosts > Enter Target IP : ")
                        doc = raw_input("sp3ctor/hosts > Enter JSON String here {key1:value,key2:value} : ")
                        save_scan(target_ip,doc_name,doc)
                    cmd = raw_input("sp3ctor/hosts > ")
            elif(cmd.lower() == 'update'):# Update the script from new version on Github
                cprint("[-] Checking for new Updated",'yellow')
            elif(cmd.lower() == 'exploit'):# Use MSF Console and other framework if they have one line
                cprint("---------------Exploit Frameworks Integrated-----------",'white')
            elif(cmd.lower() == 'shells'):# Use Python interactive shell or Bash Shell 
                cprint("----------------Interactive Shells Integrated------------",'yellow')
            else:
                cprint("[x] Command Not Found ",'red')
                cprint("[?] Showing Command list \n[-] scan\n[-] hosts\n[-] update\n[-] exploit\n[-] exit",'white')
            cmd = raw_input("sp3ctor > ")
    except KeyboardInterrupt:
        cprint("\n[x] Shutting down system")
        cprint(""" 
        __ __   ____  ____  ____  __ __      __ __   ____    __  __  _  ____  ____    ____ 
        |  |  | /    ||    \|    \|  |  |    |  |  | /    |  /  ]|  |/ ]|    ||    \  /    |
        |  |  ||  o  ||  o  )  o  )  |  |    |  |  ||  o  | /  / |  ' /  |  | |  _  ||   __|
        |  _  ||     ||   _/|   _/|  ~  |    |  _  ||     |/  /  |    \  |  | |  |  ||  |  |
        |  |  ||  _  ||  |  |  |  |___, |    |  |  ||  _  /   \_ |     | |  | |  |  ||  |_ |
        |  |  ||  |  ||  |  |  |  |     |    |  |  ||  |  \     ||  .  | |  | |  |  ||     |
        |__|__||__|__||__|  |__|  |____/     |__|__||__|__|\____||__|\_||____||__|__||___,_|
                                                                                                                
        """,'red')
        exit()
    cprint("[x] Shutting down system")
    cprint(""" 
    __ __   ____  ____  ____  __ __      __ __   ____    __  __  _  ____  ____    ____ 
    |  |  | /    ||    \|    \|  |  |    |  |  | /    |  /  ]|  |/ ]|    ||    \  /    |
    |  |  ||  o  ||  o  )  o  )  |  |    |  |  ||  o  | /  / |  ' /  |  | |  _  ||   __|
    |  _  ||     ||   _/|   _/|  ~  |    |  _  ||     |/  /  |    \  |  | |  |  ||  |  |
    |  |  ||  _  ||  |  |  |  |___, |    |  |  ||  _  /   \_ |     | |  | |  |  ||  |_ |
    |  |  ||  |  ||  |  |  |  |     |    |  |  ||  |  \     ||  .  | |  | |  |  ||     |
    |__|__||__|__||__|  |__|  |____/     |__|__||__|__|\____||__|\_||____||__|__||___,_|
                                                                                                            
    """,'red')
    exit()
