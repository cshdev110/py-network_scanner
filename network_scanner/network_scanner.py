#!/usr/bin/env python

# The script needs to be executed as superuser.
import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # with this function, scapy.srp() we send packets and receive the answer
    # [0] is set as we need just the first list only.
    #  With verbose=false the top of the information is not printed out
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("-----------------------------------------")
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        print("-----------------------------------------")


scan("192.168.180.1/24")
