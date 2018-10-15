import SimplePool
import nmap
from termcolor import cprint
import sys
from targets_database import save_scan

try:
    nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)



def scan_ip(ip):
    cprint("[-] Scanner Started for Target : %s "%ip,'yellow')
    scan_result = nm.scan(hosts=ip,arguments='-A -O -sV ')
    #cprint("[+] Scan %s Complete "%ip,'green')
    for host in nm.all_hosts():
        cprint('----------------------------------------------------')
        cprint('Host : %s \tHostname : %s' % (host, nm[host].hostname()),'green')
        cprint('State : %s' % nm[host].state(),'green')

        for proto in nm[host].all_protocols():
            cprint('----------------------------------------------------')
            cprint('Protocol : %s' % proto,'green')

            lport = list(nm[host][proto].keys())
            lport.sort()
            for port in lport:
                cprint('port : %s\tstate : %s \tService Name: %s \tService Version : %s' \
                % (port, nm[host][proto][port]['state'],nm[host][proto][port]['name'],\
                nm[host][proto][port]['version']),'green')
        
        if nm[host].has_key('osclass'):
            for osclass in nm[host]['osclass']:
                cprint('OsClass.type : {0}'.format(osclass['type']),'green')
                cprint('OsClass.vendor : {0}'.format(osclass['vendor']),'green')
                cprint('OsClass.osfamily : {0}'.format(osclass['osfamily']),'green')
                cprint('OsClass.osgen : {0}'.format(osclass['osgen']),'green')
                cprint('OsClass.accuracy : {0}'.format(osclass['accuracy']),'green')
                # cprint('\n')

        if nm[host].has_key('osmatch'):
            for osmatch in nm[host]['osmatch']:
                cprint('osmatch.name : {0}'.format(osmatch['name']),'green')
                cprint('osmatch.accuracy : {0}'.format(osmatch['accuracy']),'green')
                cprint('osmatch.line : {0}'.format(osmatch['line']),'green')
                # cprint('\n')

        if nm[host].has_key('fingerprint'):
            cprint('Fingerprint : {0}'.format(nm[host]['fingerprint']),'green')
        for mac in nm[host]['vendor'].keys():
            cprint("Mac Address : %s \tName : %s"%(mac,nm[host]['vendor'][mac]),'green')
        cprint('----------------------------------------------------')
    cprint("Scanning %s Complete "%ip,'yellow') 
    cprint("[-] Updating Database Profile ",'yellow')
    save_scan(ip,'nmap',scan_result)           
    return

def scanner(ips):
    if(len(ips)>0):
        cprint("[-] Live IPs to Scan ",'yellow')
        for ip in ips:
            cprint("[+] %s is live"%ip,'green')
        pool = SimplePool.ThreadPool()
        for ip in ips:
            job = SimplePool.ThreadJob(scan_ip,ip)
            pool.add_job(job)
        pool.start()
        pool.finish()
    ips = []
    return