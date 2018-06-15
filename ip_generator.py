import netaddr
from termcolor import cprint

#-----------This Function Check if its Single IP return as is 
#-----------If its Range then Return List of IPs
def generate_range(input_ip):
    generated_ips = netaddr.IPNetwork(input_ip)
    ips = []
    if(len(generated_ips)>1):
        cprint("[+] Generating IP List",'green')
        
        broadcast = raw_input("[?] Do you have broadcast IP to discard [y][n] : ")
        if(broadcast == 'y' or broadcast == 'Y'):
            for  ip in generated_ips:
            # Change from IP Object in format IPAddress('192.168.1.1') to String '192.168.1.1'
            # Discarding Broadcast IP from Scan
                if(ip == generated_ips.broadcast):
                    cprint("[-] Discarding Broadcast IP %s"%ip,'yellow')
                    continue
                else:
                    ips.append(str(ip)) 
        else:
            for  ip in generated_ips:
            # Change from IP Object in format IPAddress('192.168.1.1') to String '192.168.1.1'
                ips.append(str(ip)) 
        network = raw_input("[?] Do you have network IP to discard [y][n] : ")
        if(network == "y" or network == 'Y'):
            ips.reverse()
            network_IP = ips.pop()
            ips.reverse()
            cprint("[-] Discarding Network IP : %s"%network_IP,'yellow')
        cprint("[+] %s IPs Ready to ping : "%str(len(ips)))
        return ips # Return IP List
    else:
        cprint("[+] Single IP is Provided")
        ips.append(input_ip)
        return ips # Return List with Single IP
        

