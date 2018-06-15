from multiping import multi_ping,MultiPingError,MultiPing
from termcolor import cprint
from socket import error
import SimplePool

live = []

def multi_pinger(ips):
    try:
        cprint("[-] Pinging %s"%ips)
        if(ips == "192.168.1.0"):
            return
        mp = MultiPing(ips)
        mp.send()
        response, no_response = mp.receive(1)
        for addr,ttl in response.items():
            cprint("%s is live and responed in %f"%(addr,ttl),'green')
            live.append(addr)
    except MultiPingError:
        cprint("[x] Error "+ MultiPingError,'red')
    #except error:
    #    cprint("[x] Socket Error , Permission Denied",'red')
    # return live

'''
def pinger (ips):
    pool = SimplePool.ThreadPool()
    cprint("[+] Starting Ping Scan ",'green')
    for ip in ips:
        job = SimplePool.ThreadJob(multi_pinger,ip)
        pool.add_job(job)
    pool.start()
    pool.finish()
    return live
'''
def pinger(ips):
    for i in ips:
        ip = []
        ip.append(i)
        multi_pinger(ip)
    return live