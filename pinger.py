from termcolor import cprint
import SimplePool
import subprocess

live = []
def ping_ip (ip):
    result = subprocess.check_output('ping -c 3 %s | grep "3 received"'%ip , shell = True)
    if(result != ''):
        global live 
        live.append(ip)
        cprint("[+] %s is live"%ip,'green')
    return

def pinger (ips):
    pool = SimplePool.ThreadPool()
    cprint("[+] Starting Ping Scan ",'green')
    for ip in ips:
        job = SimplePool.ThreadJob(ping_ip,ip)
        pool.add_job(job)
    pool.start()
    pool.finish()
    return live
