#!/usr/bin/env python

# The script needs to be executed as superuser.
import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # with this function we send packets and receive the answer
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(unanswered.summary())


scan("192.168.180.1/24")
