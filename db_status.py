from subprocess import check_output
from termcolor import cprint
from check_priv import getprivs
from sys import exit
def db_status():
    result = check_output('systemctl status couchdb | grep "Active" ',shell = True)
    if "inactive" in result:
        cprint("[x] Databse is not Running",'red')
        cprint("[-] Checking Privileges to start Database",'yellow')
        privs = getprivs()
        if(privs == 'admin'):
            cprint("[-] You have root privileges\n[-] Starting Couchdb",'yellow')
            result = check_output("sudo systemctl start couchdb > /dev/null",shell=True)
            cprint("[-] Checking Database Status",'yellow')
            result = check_output('systemctl status couchdb | grep "Active" ',shell = True)
            if("active" in result):
                cprint("[+] Database is running ",'green')
            else:
                cprint("[x] Printing Status : %s"%result,'red')
                exit()
        else:
            cprint("[x] Root Privileges needed ",'red')
            exit()
    elif "active" in result:
        cprint("[+] Database is running",'green')
    else:
        cprint("[x] Unknown Error Please send the Following to saluslablive@gmail.com",'red')
        cprint(result,'red')
        exit()