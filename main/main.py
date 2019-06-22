import subprocess as sp


def ping(ip_address):
    status, result = sp.getstatusoutput("ping -c1 -w2 " + str(ip_address))
    if "Received = 4" in result:
        print("System " + str(ip_address) + " is UP !")
    elif "Received = 0" in result:
        print("System " + str(ip_address) + " is DOWN !")
    else:
        print("System " + str(ip_address) + " is Unstable !")


with open('ip_address.txt') as file_name:
    ip_addrs = file_name.read().splitlines()

for ip_addr in ip_addrs:
    ping(ip_addr)
