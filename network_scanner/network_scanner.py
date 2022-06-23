#!/usr/bin/env python

# The script needs to be executed as superuser.
import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())
    scapy.ls(scapy.ARP())  # List all the fields we can set


scan("192.168.180.1/24")
