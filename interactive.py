# This Module allow user to interact with DB and Tool
from termcolor import cprint
from sys import exit 
from hosts import get_all_scanned_hosts
from targets_database import save_scan
from hosts import get_ports
def interactive_mode():
    try:
        cprint("[?] What do you want to do next ? (help) to show commands",'yellow')
        cmd = raw_input("spector > ")
        while(cmd !="exit"):
            if(cmd.lower() == "help"):
                cprint("[?] Showing Command list \n[-] scan\n[-] hosts\n[-] update\n[-] exploit\n[-] exit",'white')   
            elif(cmd.lower() == "scan"):
                cprint("[?] Enumeration Tools:\n[-] NMAP\n[-] NIKTO\n[-] WPSCAN\n[-] Exit",'white')
            elif(cmd.lower() == 'hosts'): # Read all the Hosts in DB you can add push JSONs for IPs
                cprint("---------------------Scanned Host IPs-------------------",'white')
                get_all_scanned_hosts()
                cmd = raw_input("spector/hosts > ")
                while(cmd.lower() !="back"):
                    if(cmd.lower() == "help"):
                        cprint("[-] get_ports\n[-] add_data",'white')
                    elif(cmd.lower() == "back"):
                        break
                    elif(cmd.lower() == "get_ports"):
                        get_ports()
                    elif(cmd.lower() == "add_data"):
                        doc_name = raw_input("spector/hosts > Enter Document Name : ")
                        target_ip = raw_input("spector/hosts > Enter Target IP : ")
                        doc = raw_input("spector/hosts > Enter JSON String here {key1:value,key2:value} : ")
                    cmd = raw_input("spector/hosts > ")
            elif(cmd.lower() == 'update'):# Update the script from new version on Github
                cprint("[-] Checking for new Updated",'yellow')
            elif(cmd.lower() == 'exploit'):# Use MSF Console and other framework if they have one line
                cprint("---------------Exploit Frameworks Integrated-----------",'white')
            elif(cmd.lower() == 'shells'):# Use Python interactive shell or Bash Shell 
                cprint("----------------Interactive Shells Integrated------------",'yellow')
            else:
                cprint("[x] Command Not Found ",'red')
                cprint("[?] Showing Command list \n[-] scan\n[-] hosts\n[-] update\n[-] exploit\n[-] exit",'white')
            cmd = raw_input("spector > ")
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
