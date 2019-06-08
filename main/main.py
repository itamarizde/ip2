import os
import subprocess as sp
import pyping
def  Ping( ipaddress):
    status, result = sp.getstatusoutput("ping -c1 -w2 " + str(ipaddress))
    if "TTL" and "time" in result:
        print("System " + str(ipaddress) + " is UP !")
    else:
        print("System " + str(ipaddress) + " is DOWN !")


with open('ip_adress.txt') as fname:
    ip_addrs=fname.read().splitlines()

for ip_addr in ip_addrs:
   Ping(ip_addr)