import subprocess
from targets_database import save_scan
from termcolor import cprint
from time import ctime
import SimplePool , socket

def nikto_scan(service,ip,port):
    if((port == 80 and service == "http") or (port == 443 and service == "https")):
        url = service+"://"+ip+"/"
        cprint("[-] Nikto Scanning this URL : %s .... Please wait"%url,'yellow')
    else :
        url = service+"://"+ip+":"+port+"/"
        cprint("[-] Nikto Scanning this URL : %s .... Please wait"%url,'yellow')
    cmd = "nikto -h " +url
    pool = SimplePool.ThreadPool()
    background_job = SimplePool.ThreadJob(background_scan,[cmd,ip])
#    foreground_job = SimplePool.ThreadJob(foreground_scan,cmd)
    pool.add_job(background_job)
#    pool.add_job(foreground_job)
    pool.start()
    pool.finish()
    return

#def foreground_scan(cmd):
#    subprocess.call(cmd , stdout= subprocess.PIPE ,stderr = subprocess.PIPE, shell= True)
#    return

def background_scan(cmd,ip):
    scanner =   subprocess.Popen(cmd,stdout= subprocess.PIPE ,stderr = subprocess.PIPE,shell=True)
    (output, err) = scanner.communicate()
    if(err):
        print(err)
    else:
        ip = socket.gethostbyname(ip)
        cprint("[+] Nikto Scan Result")
        cprint(output)
        save_nikto_scan(output,ip)
    return output
def save_nikto_scan(results,ip):
    save = raw_input("[?] Do you want to save this NIKTO Scan [y/n] ? : ")
    if(save.lower() == 'y'):
        now = ctime()
        scan_data = {"time":now, "results":results}
        save_scan(ip,"nikto",scan_data)
    elif(save.lower() == 'n'):
        cprint("[x] Scan is not saved",'red')
    else:
        cprint("[x] Option is not found ... Try again !",'red')
    return