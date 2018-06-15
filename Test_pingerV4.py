from icmp_ping import verbose_ping
from termcolor import cprint
import SimplePool



def pinger (ips):
    pool = SimplePool.ThreadPool()
    cprint("[+] Starting Ping Scan ",'green')
    for id,ip in enumerate(ips):
        job = SimplePool.ThreadJob(verbose_ping,ip)
        pool.add_job(job)
    pool.start()
    pool.finish()
    #return live
