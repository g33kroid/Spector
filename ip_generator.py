import netaddr
from termcolor import cprint

#-----------This Function Check if its Single IP return as is 
#-----------If its Range then Return List of IPs
def generate_range(input_ip):
    generated_ips = netaddr.IPNetwork(input_ip)
    ips = []
    if(len(generated_ips)>1):
        cprint("[+] Generating IP List",'green')
        for  ip in generated_ips:
            # Change from IP Object in format IPAddress('192.168.1.1') to String '192.168.1.1'
            ips.append(str(ip)) 
        cprint("[+] %s IPs Generated"%str(len(ips)))
        return ips # Return IP List
    else:
        cprint("[+] Single IP is Provided")
        ips.append(input_ip)
        return ips # Return List with Single IP
        

