# This Module Interact with Database to Add/Edit Scanned Hosts
import requests
import couchdb
from termcolor import cprint
from design_view import get_all_ports_full, get_all_ports_name, get_all_ports_no
def get_all_scanned_hosts():
    hosts = []
    res = requests.get("http://localhost:5984/_all_dbs")
    if(res.status_code == 200):
        for host in res.json():
            if("machine" in host):
                ip = str(host).split("_")[::-1]
                ip.pop()
                ip = ip[::-1]
                ip = str(".".join(ip))
                cprint("%s"%ip,'white')
                hosts.append(ip)
    else:
        cprint("[x] Can't Get Scanned hosts Error Code :%s "%str(res.status_code),'red')
    return hosts
def get_ports():
    ip = raw_input("spector/host > Enter IP: ")
    options = raw_input("Choose Options\n[1] Port Number Only\n[2] Port Name and Number\n[3] Full Port Details\nspector/hosts > ")
    if(options == "1"):
        get_all_ports_no(ip)
    elif(options == "2"):
        get_all_ports_name(ip)
    elif(options == "3"):
        get_all_ports_full(ip)
    else:
        cprint("[x] No Valid Option Selected ",'red')