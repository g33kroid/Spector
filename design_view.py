import couchdb
from termcolor import cprint
from socket import error
from sys import exit



import couchdb
from termcolor import cprint
from socket import error
from sys import exit

# Connecting to Local Database
try:
    server = couchdb.Server()
except error:
    cprint("[x] Database Connection Refused\n[x] Please start the couch DB {sudo systemctl start couchdb}",'red')
    cprint("[-] Shutting Down .... ")
    exit(0)

def add_design_view(ip):
    profile = "machine_"+str(ip).replace('.','_')
    cprint("[-] Checking Profile %s for %s "%(profile,ip),'yellow')
    db = server[profile]
    cprint("[-] Profile Exists : %s"%profile,'yellow')
    get_all_ports_view = {
   "_id": "_design/search",
   "language": "javascript",
   "views": {
       "get_all_ports": {
           "map": 'function(doc) {\n  ports = [] \n  port_no = []\n  for (p in doc[\"scan\"]["'+str(ip)+'"][\"tcp\"]) ports.push(p)\t\n  emit(doc[\"nmap\"][\"scanstats\"][\"timestr\"],ports )\n}'
       },
       "get_all_ports_name": {
           "map": 'function(doc) {\n  ports = [] \n  port_no = []\n  for (p in doc[\"scan\"]["'+str(ip)+'"][\"tcp\"]) ports.push(p.toString()+\":\"+doc[\"scan\"]["'+str(ip)+'"][\"tcp\"][p][\"name\"].toString())\t\n  emit(doc[\"nmap\"][\"scanstats\"][\"timestr\"],ports )\n}'
       },
       "get_all_ports_full": {
           "map": 'function(doc) {\n  ports = [] \n  port_no = []\n  for (p in doc[\"scan\"]["'+str(ip)+'"][\"tcp\"]) ports.push(p.toString()+\":\"+doc[\"scan\"]["'+str(ip)+'"][\"tcp\"][p][\"name\"].toString()+\":\"+doc[\"scan\"]["'+str(ip)+'"][\"tcp\"][p][\"version\"].toString())\t\n  emit(doc[\"nmap\"][\"scanstats\"][\"timestr\"],ports )\n}'
       },
       "os_type": {
           "map": 'function(doc) {\n emit(doc[\"nmap\"][\"scanstats\"][\"timestr\"],doc["scan"]["'+str(ip)+'"]["osmatch"])\n}'
       }
   }
}
    cprint("[-] Adding Get All Ports Design View",'yellow')
    try:
        doc_id , doc_rev = db.save(get_all_ports_view)
        cprint("[+] View is added with ID : %s and Rev Number : %s "%(doc_id,doc_rev),"green")
    except couchdb.http.ResourceConflict:
        cprint("[x] Get All Ports Design View already exists ",'red')
    
def get_all_ports_no(ip):
    result = {}
    profile = "machine_"+str(ip).replace('.','_')
    cprint("[-] Checking Profile %s for %s "%(profile,ip),'yellow')
    db = server[profile]
    cprint("[-] Profile Exists : %s"%profile,'yellow')
    cprint("[-] Printing Ports Found on every Scan")
    for item in db.view("search/get_all_ports"):
        cprint("-----------------------------------------")
        cprint("Date \t%s"%item.key,'green')
        cprint("-----------------------------------------")
        cprint("Port",'yellow')
        for data in item.value:
            data = str(data).split(":")
            for i in data:
                print i + "\t",
            print("\n")    
        result[item.key] = item.value
    return result
def get_all_ports_full(ip):
    result = {}
    profile = "machine_"+str(ip).replace('.','_')
    cprint("[-] Checking Profile %s for %s "%(profile,ip),'yellow')
    db = server[profile]
    cprint("[-] Profile Exists : %s"%profile,'yellow')
    cprint("[-] Printing Ports Found on every Scan")
    for item in db.view("search/get_all_ports_full"):
        cprint("-----------------------------------------")
        cprint("Date \t%s"%item.key,'green')
        cprint("-----------------------------------------")
        cprint("Ports\tService Name\tService Version\n",'yellow')
        for data in item.value:
            data = str(data).split(":")
            for i in data:
                print i + "\t",
            print("\n")    
        result[item.key] = item.value
    return result
def get_all_ports_name(ip):
    result = {}
    profile = "machine_"+str(ip).replace('.','_')
    cprint("[-] Checking Profile %s for %s "%(profile,ip),'yellow')
    db = server[profile]
    cprint("[-] Profile Exists : %s"%profile,'yellow')
    cprint("[-] Printing Ports Found on every Scan")
    for item in db.view("search/get_all_ports_name"):
        cprint("-----------------------------------------")
        cprint("Date \t%s"%item.key,'green')
        cprint("-----------------------------------------")
        cprint("Ports\tService Name",'yellow')
        for data in item.value:
            data = str(data).split(":")
            for i in data:
                print i + "\t",
            print("\n")    
        result[item.key] = item.value
    return result
def get_os_type(ip):
    result = {}
    profile = "machine_"+str(ip).replace('.','_')
    cprint("[-] Checking Profile %s for %s "%(profile,ip),'yellow')
    db = server[profile]
    cprint("[-] Profile Exists : %s"%profile,'yellow')
    cprint("[-] Printing OS Matches Found on every Scan")
    for item in db.view("search/os_type"):
        cprint("-----------------------------------------")
        cprint("Date \t%s"%item.key,'green')
        cprint("-----------------------------------------")
        cprint("OS Family\tName\tAccuracy",'yellow')
        data = item.value
        print(data)
    return result
