import couchdb
from termcolor import cprint
from socket import error
from sys import exit
from uuid import uuid4

# Connecting to Local Database
try:
    server = couchdb.Server()
except error:
    cprint("[x] Database Connection Refused\n[x] Please start the couch DB {sudo systemctl start couchdb}",'red')
    cprint("[-] Shutting Down .... ")
    exit(0)

def check_db(ip):
    try:
        profile = "machine_"+str(ip).replace('.','_')
        cprint("[-] Checking Profile %s for %s "%(profile,ip),'yellow')
        db = server[profile]
        cprint("[-] Profile Exists : %s"%profile,'yellow')
    except couchdb.http.ResourceNotFound:
        profile = "machine_"+str(ip).replace('.','_')
        cprint('[+] Creating New Profile for %s : %s'%(ip,profile) , 'green')
        try:
            db = server.create(profile)
            cprint("[-] Profile Created",'yellow')
        except couchdb.http.ServerError:
            cprint("[x] Profile Name Error ",'red')
    return db

def save_scan(ip,scan_name,results):
    db = check_db(ip)
    try:
        doc_id = scan_name + "-" + str(uuid4())
        db[doc_id] = results
        cprint("[+] %s scan saved for %s \n[+] Scan ID : %s "%(scan_name,ip,doc_id),'green')
    except couchdb.http.ResourceConflict:
        doc_id = scan_name + "-" + str(uuid4)
        db[doc_id] = results
        cprint("[+] %s scan saved for %s \n[+] Scan ID : %s "%(scan_name,ip,doc_id),'green')