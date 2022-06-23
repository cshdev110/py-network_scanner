#!/usr/bin/env python

# The script needs to be executed as superuser.
import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    print(broadcast.summary())


scan("192.168.180.9")
