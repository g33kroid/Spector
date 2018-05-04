import pyping
from termcolor import cprint
import SimplePool
import threading

live = []
lock = threading.Lock()
def ping(ip):
    
    cprint('[-] Pinging %s'%ip,'yellow')
    r = pyping.ping(ip)
    print(ip+"\t"+str(r.ret_code))
    if(r.ret_code == 0):
        lock.acquire()
        cprint("%s is live"%r.destination_ip,'green')
        global live
        live.append(ip)
        lock.release()
    return



def pinger (ips):
    pool = SimplePool.ThreadPool()
    cprint("[+] Starting Ping Scan ",'green')
    for ip in ips:
        job = SimplePool.ThreadJob(ping,ip)
        pool.add_job(job)
    pool.start()
    pool.finish()
    return live
'''
def pinger(ips):
    for i in ips:
        ping(i)
    return live
'''
