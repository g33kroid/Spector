from termcolor import cprint
import SimplePool
import subprocess
from scapy.all import *


live = []
def ping_ip (ip):
    try:
        result = subprocess.check_output('ping -c 3 %s | grep "3 received" ; exit '%ip , shell = True)
        if(result != ''):
            global live 
            live.append(ip)
            cprint("[+] %s is live"%ip,'green')
        else:
            cprint("[x] %s is down"%ip,'red')
    except subprocess.CalledProcessError:
        cprint("[x] Ping Error for %s"%ip,'red')
        cprint("[-] Testing Ping Again for %s"%ip,'yellow')
        TIMEOUT = 2
        packet = IP(dst=ip, ttl=20)/ICMP()
        reply = sr1(packet, timeout=TIMEOUT)
        if not (reply is None):
            #global live 
            live.append(ip)
            cprint("[+] %s is live"%ip,'green')
        else:
            cprint("[x] %s is down"%ip,'red')
            #print "Timeout waiting for %s" % packet[IP].dst
    return

def pinger (ips):
    if(len(ips)>1):
        pool = SimplePool.ThreadPool()
        cprint("[+] Starting Ping Scan ",'green')
        for ip in ips:
            job = SimplePool.ThreadJob(ping_ip,ip)
            pool.add_job(job)
        pool.start()
        pool.finish()
    else:
        for ip in ips:
            cprint("Pinging %s"%ip,'yellow')
            ping_ip(ip)
    cprint("[-] Live IP Report",'yellow')
    
    return live
