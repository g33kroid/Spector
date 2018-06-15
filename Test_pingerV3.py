import pyping
from termcolor import cprint
import SimplePool
import threading
import os

live = []
lock = threading.Lock()
def ping(ip,own_id = None):
    
    cprint('[-] Pinging %s'%ip,'yellow')
    r = pyping.ping(ip,own_id)
    print(ip+"\t"+str(r.ret_code)+"\t"+own_id)
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
    for id,ip in enumerate(ips):
        job = SimplePool.ThreadJob(ping,[ip,id^os.getpid()])
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
