#!/usr/bin/env python

# The script needs to be executed as superuser.
import scapy.all as scapy
from optparse import OptionParser


def get_arguments():
    parser = OptionParser()
    parser.add_option("-t", "--target", dest="ip_targets", help="Range of IPs to check out")
    return parser.parse_args()[0]


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # with this function, scapy.srp() we send packets and receive the answer
    # [0] is set as we need just the first list only.
    #  With verbose=false the top of the information is not printed out
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        # clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        # clients_list.append(clients_dict)
        clients_list.append({"ip": element[1].psrc, "mac": element[1].hwsrc})  # short way
    return clients_list


def print_result(results_list):
    print("Network: " + options.ip_targets)
    print("-----------------------------------------")
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
print_result(scan(options.ip_targets))

